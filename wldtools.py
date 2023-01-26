#!/usr/bin/env python3
import argparse
import logging
from datetime import datetime

import numpy as np
import pandas as pd
import skimage
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from scipy import signal
import tqdm

logging.basicConfig(
    # level=logging.DEBUG,
    level=logging.INFO,
)


def get_image_path(name):
    return f'./data/train_512/{name}.jpg'
    # return f'./data/train/{name}.jpg'

def get_image(name):
    return skimage.io.imread(get_image_path(name))

def make_segment(image: np.array, *, window_size) -> np.array:
    y_size, x_size, *_ = image.shape
    x_start = (x_size - window_size) // 2
    x_end = x_start + window_size
    y_start = (y_size - window_size) // 2
    y_end = y_start + window_size
    return image[y_start:y_end, x_start:x_end]

def resize_image(image, size=SIZE):
    image = make_segment(image, window_size=min(image.shape[:2]))
    aa = False # True
    image = skimage.transform.resize(image, (size, size), anti_aliasing=aa)
    image = np.around(image * 255).astype(int)
    return image

def equalize_hist(image):
    return np.array([
        skimage.exposure.equalize_hist(image[:, :, 0]),
        skimage.exposure.equalize_hist(image[:, :, 1]),
        skimage.exposure.equalize_hist(image[:, :, 2])
    ]).transpose((1, 2, 0))

def make_greyscale(image):
    # Y = 0.2125 R + 0.7154 G + 0.0721 B
    return 0.2125*image[:,:,0] + 0.7154*image[:,:,1] + 0.0721*image[:,:,2]
    # return skimage.color.rgb2gray(image)

def apply_f00(matrix):
    f00 = np.array([[1,  1,  1],
                    [1, -8,  1],
                    [1,  1,  1]])
    return signal.convolve2d(matrix, f00, mode='valid')

def apply_f01(matrix):
    return matrix[1:-1, 1:-1]

def apply_f10(matrix):
    f10 = np.array([[0, -1,  0],
                    [0,  0,  0],
                    [0,  1,  0]])
    return signal.convolve2d(matrix, f10, mode='valid')

def apply_f11(matrix):
    f11 = np.array([[0,  0,  0],
                    [1,  0, -1],
                    [0,  0,  0]])
    return signal.convolve2d(matrix, f11, mode='valid')

def get_differential_excitation(matrix):
    v00 = apply_f00(matrix)
    v01 = apply_f01(matrix)
    return np.arctan(np.divide(v00, v01))

def get_gradient_orientation(matrix, t_big):
    v11 = apply_f11(matrix)
    v10 = apply_f10(matrix)
    theta = np.arctan2(v11, v10)
    theta_1 = theta + np.pi
    t = np.mod(np.floor(theta_1*t_big/(2*np.pi) + 1/2), t_big)
    theta_t = 2*t*np.pi / t_big
    return theta_t

def get_wld_histogram(image_name, m_big=M, s_big=S, t_big=T, equalize=EQUALIZE, greyscale=GREYSCALE, weights=WEIGHTS):
    image = get_image(image_name)
    image = resize_image(image, SIZE)
    if equalize:
        image = equalize_hist(image)

    if greyscale:
        image = make_greyscale(image)
        image = np.expand_dims(image, 2)
        dims = [0]
    else:
        dims = [0, 1, 2]

    grad_ori = [get_gradient_orientation(image[:, :, dim], t_big) for dim in dims]
    diff_excit = [get_differential_excitation(image[:, :, dim]) for dim in dims]

    grad_range=[0, 2*np.pi]
    excit_range=[-np.pi/2, np.pi/2]

    hists = [np.histogram2d(grad_ori[dim].flatten(),
                            diff_excit[dim].flatten(),
                            bins=[t_big, m_big*s_big],
                            range=[grad_range, excit_range],
                            )[0] # h, x, y
            for dim in dims]

    wlds = [np.array([hists[dim][:, start:start+s_big].flatten()
                      for start in range(0, m_big*s_big, s_big)]).flatten()
            for dim in dims]

    if weights:
        assert(len(weights) == m_big)
        chunk = t_big * s_big
        for m in range(m_big):
            start, end = m*chunk, (m+1)*chunk
            for dim in dims:
                wlds[dim][start:end] *= weights[m]

    wld = np.concatenate(wlds)
    wld = wld / wld.sum()
    return wld

def histogram_intersection(h1, h2):
    return np.minimum(h1, h2).sum()

def histogram_distance(h1, h2):
    return 1 - histogram_intersection(h1, h2)

def str_mean_std(values):
    return f'{np.mean(values):.2}(+-{np.var(values, ddof=1):.1e})'

def evaluate(feat, targ, *, test_size, classifiers, iterations):
    logging.info('---------- TEST SIZE {}, TRAIN SIZE {} ---------'.format(
        test_size, 1-test_size))

    metrics = {
        'BA': {name: [] for name in classifiers},
        'TN': {name: [] for name in classifiers},
        'FP': {name: [] for name in classifiers},
        'FN': {name: [] for name in classifiers},
        'TP': {name: [] for name in classifiers},
    }

    for iteration in range(iterations):
        feat_train, feat_test, targ_train, targ_test = (
            train_test_split(feat, targ, test_size=test_size,
                             random_state=iteration))
        for name, (classifier_cls, kwargs) in classifiers.items():
            logging.info('{}, round {}, class {}'.format(
                datetime.now().strftime("%H:%M:%S"), iteration, name))

            classifier = classifier_cls(**kwargs)
            classifier.fit(feat_train, targ_train)

            pred_test = classifier.predict(feat_test)

            metrics['BA'][name].append(
                balanced_accuracy_score(targ_test, pred_test))

            cm = confusion_matrix(targ_test, pred_test)
            metrics['TN'][name].append(cm[0, 0])
            if cm.shape == (2, 2):
                metrics['FP'][name].append(cm[0, 1])
                metrics['FN'][name].append(cm[1, 0])
                metrics['TP'][name].append(cm[1, 1])
            else:
                metrics['FP'][name].append(0)
                metrics['FN'][name].append(0)
                metrics['TP'][name].append(0)
    else:
        rows = [
            {
                'test_size': test_size,
                'metric': metric,
                **{name: str_mean_std(values) for name, values in data.items()}
            } for metric, data in metrics.items()
        ]
        logging.info(rows)
        return rows

def parse_arguments():
    parser = argparse.ArgumentParser(
                        prog = 'WLS',
                        description = '...',
                        epilog = '...'
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-i', '--iterations', type=int,
                        default=10, help='number of iterations')
    parser.add_argument('-n', '--samples', type=int,
                        default=2000, help='number of samples')
    parser.add_argument('-r', '--resized-side', type=int,
                        default=128 , help='size to which the image is resized')
    parser.add_argument('-g', '--convert-to-greyscale', action='store_true',
                        default=False, help='combine color channels into one')
    parser.add_argument('-e', '--equalize-histograms', action='store_true',
                        default=False, help='equalize color histograms')
    parser.add_argument('-m', '--excitation-groups', type=int,
                        default=6, help='number of excitation bins')
    parser.add_argument('-w', '--excitation-group-weights', nargs='*', type=float,
                        default=[0.2688, 0.0852, 0.0955, 0.1000, 0.1018, 0.3487],
                        help='use simple -w for now weights, defaults are from the paper')
    parser.add_argument('-s', '--excitation-group-bins', type=int,
                        default=10, help='granularity of excitation per gradient orientation group')
    parser.add_argument('-t', '--orientations', type=int,
                        default=8, help='number of gradient orientations')
    args = parser.parse_args()

    # Check the values
    if args.excitation_group_weights:
        assert(args.excitation_groups == len(args.excitation_group_weights))
    return args

full_df = pd.read_csv('./data/ISIC_2020_Training_GroundTruth.csv')

if __name__ == '__main__':

    args = parse_arguments()
    print('\n'.join(f'{key}={value}' for key, value in vars(args).items()))

    # if SAMPLES:
    #     df = full_df.sample(SAMPLES, random_state=0)
    # else:
    #     df = full_df

    # logging.info('Extracting WLD from images')
    # feat = np.array([get_wld_histogram(name)
    #     for name in tqdm.tqdm(df.image_name)
    # ])
    # targ = df.target

    # classifiers = {
    #     ('KNN', '1'):       (KNeighborsClassifier,
    #                          dict(n_neighbors=1, metric=histogram_distance)),
    #     # ('KNN', '3'):       (KNeighborsClassifier,
    #     #                      dict(n_neighbors=3, metric=histogram_distance)),
    #     # ('SVM', 'poly(3)'): (SVC, dict(kernel='poly', degree=3)),
    #     # ('SVM', 'rbf'):     (SVC, dict(kernel='rbf')),
    # }

    # rows = []

    # for test_size in [0.3, 0.5, 0.7]:
    #     rows.extend(
    #         evaluate(feat, targ,
    #             test_size=test_size,
    #             classifiers=classifiers
    #             iterations=iterations
    #         )
    #     )

    # table = pd.DataFrame(rows)
    # table = table.set_index(['test_size', 'metric'])
    # table.columns = pd.MultiIndex.from_tuples(table.columns)
    # print(table.to_latex())
