import numpy as np
import tqdm

imgs = []

for x in tqdm.tqdm(range(33126)):
    a = np.ones(6*8*20, dtype='B')
    imgs.append(a)
