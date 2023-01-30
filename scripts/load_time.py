import pickle
import pandas as pd
import tqdm
import skimage

truth_frame = pd.read_csv('./data/ISIC_2020_Training_GroundTruth.csv')

i = 0
for image_name in tqdm.tqdm(truth_frame.image_name):
    i += 1

    path = f'./data/train/{image_name}.jpg'
    image = skimage.io.imread(path)

    if i == 1000:
        break
