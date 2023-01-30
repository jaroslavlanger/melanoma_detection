import pickle
import sys
import tqdm

col = []

for i in tqdm.tqdm(range(33)):
    with open('./data/images.pickle', 'rb') as pickle_fd:
        images = pickle.load(pickle_fd)
    col.append(images)
