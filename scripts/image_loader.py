#!/usr/bin/env python3
import sys

import numpy as np
import pandas as pd
import skimage
import tqdm

def make_segment(image: np.array, *, window_size=64) -> np.array:
    y_size, x_size, *_ = image.shape
    x_start = (x_size - window_size) // 2
    x_end = x_start + window_size
    y_start = (y_size - window_size) // 2
    y_end = y_start + window_size
    return image[y_start:y_end, x_start:x_end]

def resize_image(image, size=128):
    image = make_segment(image, window_size=min(image.shape[:2]))
    aa = False # True
    image = skimage.transform.resize(image, (size, size), anti_aliasing=aa)
    image = np.around(image * 255).astype('B')
    return image

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit()

    proc_num = int(sys.argv[1])

    truth_frame = pd.read_csv('./data/ISIC_2020_Training_GroundTruth.csv')

    chunk_size = 4150
    start = -(proc_num+1)*chunk_size
    end = -proc_num*chunk_size if proc_num != 0 else None
    print(f'Processing data in range {start}:{end}')

    for image_name in tqdm.tqdm(truth_frame.image_name[start:end]):
        path = f'./data/train/{image_name}.jpg'
        image = skimage.io.imread(path)
        image = make_segment(image, window_size=min(image.shape[:2]))
        SIZE = 512
        image = resize_image(image, size=SIZE)

        skimage.io.imsave(f'./data/train_{SIZE}/{image_name}.jpg', image)
