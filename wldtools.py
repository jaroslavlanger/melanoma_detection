#!/usr/bin/env python3
import argparse
import logging
from datetime import datetime
import pickle
import random

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

WEIGHTS_PAPER = [0.2688, 0.0852, 0.0955, 0.1000, 0.1018, 0.3487]

logging.basicConfig(
    # level=logging.DEBUG,
    level=logging.INFO,
)


def get_image_path(name):
    return f'./data/train_512/{name}.jpg'
    # return f'./data/train/{name}.jpg'

def get_image(name):
    return skimage.io.imread(get_image_path(name))

def make_segment(image: np.array, *, window_side) -> np.array:
    y_len, x_len, *_ = image.shape
    x_start = (x_len - window_side) // 2
    x_end = x_start + window_side
    y_start = (y_len - window_side) // 2
    y_end = y_start + window_side
    return image[y_start:y_end, x_start:x_end]

def resize_image(image, *, side):
    shape = (side, side)
    image = make_segment(image, window_side=min(image.shape[:2]))
    aa = False # True
    image = skimage.transform.resize(image, shape, anti_aliasing=aa)
    image = np.around(image * 255).astype(int)
    return image

def equalize_hist(image_2d):
    return skimage.exposure.equalize_hist(image_2d)

def make_grayscale(image):
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

def get_wld_histogram(image_name, *, side, grayscale, equalize, excit_groups, group_weights, group_bins, orientations):
    if group_weights: assert(len(group_weights) == excit_groups)
    image = get_image(image_name)
    image = resize_image(image, side=side)

    if grayscale:
        image = make_grayscale(image)
        channels = [image]
    else:
        channels = [image[:, :, ch_idx] for ch_idx in [0, 1, 2]]

    if equalize:
        channels = [equalize_hist(channel) for channel in channels]

    diff_excit = [get_differential_excitation(channel) for channel in channels]
    grad_orien = [get_gradient_orientation(channel, orientations) for channel in channels]

    orien_range = [0, 2*np.pi]
    excit_range = [-np.pi/2, np.pi/2]

    hists = [np.histogram2d(orien.flatten(), excit.flatten(),
                            bins=[orientations, excit_groups*group_bins],
                            range=[orien_range, excit_range],
                            )[0] # h, x, y
            for orien, excit in zip(grad_orien, diff_excit)]

    wlds = [np.array([hist[:, start:start+group_bins].flatten()
                      for start in range(0, excit_groups*group_bins, group_bins)]
                    ).flatten()
            for hist in hists]

    if group_weights:
        # TODO drop segments of zero weight.
        chunk = orientations * group_bins
        for m in range(excit_groups):
            start, end = m*chunk, (m+1)*chunk
            for wld in wlds:
                wld[start:end] *= group_weights[m]

    wld = np.concatenate(wlds)
    wld = wld / wld.sum()
    return wld

def histogram_intersection(h1, h2):
    return np.minimum(h1, h2).sum()

def histogram_distance(h1, h2):
    return 1 - histogram_intersection(h1, h2)

def str_mean_std(values):
    return f'{np.mean(values):.2}(+-{np.var(values, ddof=1):.1e})'

def evaluate(*, feat_train, targ_train, feat_test, targ_test, classifier) -> dict:
    metrics = {}
    classifier.fit(feat_train, targ_train)
    pred_test = classifier.predict(feat_test)
    metrics['BA'] = balanced_accuracy_score(targ_test, pred_test)
    cm = confusion_matrix(targ_test, pred_test)
    metrics['TN'] = cm[0, 0]
    if cm.shape == (2, 2):
        metrics['FP'] = cm[0, 1]
        metrics['FN'] = cm[1, 0]
        metrics['TP'] = cm[1, 1]
    else:
        metrics['FP'] = 0
        metrics['FN'] = 0
        metrics['TP'] = 0
    return metrics

def parse_arguments():
    parser = argparse.ArgumentParser(
                        prog = 'WLS',
                        description = '...',
                        epilog = '...',
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('-i', '--iterations', type=int,
                        default=10, help='number of iterations')
    parser.add_argument('-n', '--samples', type=int,
                        default=2000, help='number of samples')
    parser.add_argument('-r', '--side', type=int,
                        default=128 , help='resized image side length')
    parser.add_argument('-g', '--grayscale', action='store_true',
                        default=False, help='convert to grayscale')
    parser.add_argument('-e', '--equalize', action='store_true',
                        default=False, help='equalize color channel histograms')
    parser.add_argument('-m', '--groups', type=int,
                        default=6, help='number of differential excitation groups')
    parser.add_argument('-w', '--group-weights', nargs='*', type=float,
                        default=WEIGHTS_PAPER,
                        help='excitation group weights,'
                             ' for uniform weights input plain -w,'
                             ' defaults are from the paper')
    parser.add_argument('-s', '--group-bins', type=int,
                        default=20, help='number of bins for each excitation group')
    parser.add_argument('-t', '--orientations', type=int,
                        default=8, help='number of gradient orientations')
    parser.add_argument('-u', '--undersample', action='store_true',
                        default=False,
                        help='Undersample the training majority target class'
                        'to the size of training minority class.')
    args = parser.parse_args()

    # Check the values
    if args.group_weights:
        assert(args.groups == len(args.group_weights))
    return args

def get_feat_and_targ(df, args):
    logging.info('Extracting WLD from images')
    feat = np.array([get_wld_histogram(name,
            side=args.side,
            grayscale=args.grayscale,
            equalize=args.equalize,
            excit_groups=args.groups,
            group_weights=args.group_weights,
            group_bins=args.group_bins,
            orientations=args.orientations,
        )
        for name in tqdm.tqdm(df.image_name)
    ])
    targ = df.target
    return feat, targ

full_df = pd.read_csv('./data/ISIC_2020_Training_GroundTruth.csv')

if __name__ == '__main__':
    random.seed(0)

    args = parse_arguments()
    print('\n'.join(f'{key}={value}' for key, value in vars(args).items()))
    classifiers = {
        'KNN-1':        (KNeighborsClassifier,
                         dict(n_neighbors=1, metric=histogram_distance)),
        'KNN-3':        (KNeighborsClassifier,
                         dict(n_neighbors=3, metric=histogram_distance)),
        'SVM-poly3':    (SVC, dict(kernel='poly', degree=3)),
        'SVM-rbf':      (SVC, dict(kernel='rbf')),
    }

    debug = False
    if debug:
        with open('./data/wlds.pickle', 'rb') as pkl:
            data = pickle.load(pkl)
        feat, targ = data['feat'], data['targ']
    else:
        feat, targ = get_feat_and_targ(full_df, args)

    save = False
    if save:
        name = f"{str(datetime.now()).split('.')[0]}.pickle"
        with open(name, 'wb') as pkl:
            pickle.dump(dict(feat=feat, targ=targ, args=args), pkl)


    result_rows = []
    for iteration in range(args.iterations):

        indices = list(range(len(feat)))
        if args.samples:
            indices = random.sample(indices, args.samples)

        for test_size in [0.3, 0.5, 0.7]:
            feat_train, feat_test, targ_train, targ_test = (
                train_test_split(feat[indices], targ.iloc[indices],
                                 test_size=test_size,
                                 random_state=iteration))

            if args.undersample:
                positive = targ_train == 1
                negative = (targ_train == 0).sample(n=positive.sum(), random_state=iteration)
                sample = (positive | negative)
                feat_train = feat_train[sample]
                targ_train = targ_train[sample]

            for name, (classifier_cls, kwargs) in classifiers.items():

                classifier = classifier_cls(**kwargs)
                metrics = evaluate(feat_train=feat_train, targ_train=targ_train,
                                   feat_test=feat_test, targ_test=targ_test,
                                   classifier=classifier,
                )
                row = {
                    'iteration': iteration,
                    'test_size': test_size,
                    'name': name,
                    **metrics,
                }
                logging.info('{}, {}'.format(datetime.now().strftime("%H:%M:%S"), row))
                result_rows.append(row)

    table = pd.DataFrame(result_rows)
    table = table.groupby(['test_size', 'name']).agg(['mean', 'std']).transpose().drop(('iteration', 'mean')).drop(('iteration', 'std'))
    # table.columns = pd.MultiIndex.from_tuples(table.columns)
    print(table.to_csv())
