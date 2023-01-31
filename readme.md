Melanoma Detection
==================

Term project of Pattern Recognition course at CTU, Prague.

Installation
------------

```sh
# Create virtual environment for the python packages
python3 -m venv venv
# Activate it
source venv/bin/activate
# Install all required packages into the venv
python3 -m pip install --upgrade -r requirements.txt
# Install jupyter kernel
python -m ipykernel install --user --name=kernelname
```

I personally use jupyter extension for VS Code where I choose the kernelname as jupyter kernel.
Another approach is to install jupyter lab, and open the .ipynb notebook in browser.
```sh
pip3 install jupyterlab
jupyter lab
```

Data
----

*The images are not part of this repository!* In order to run the code, follow:
```sh
mkdir -p data/train
curl https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_JPEG.zip -o data/train/images.zip
curl https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_GroundTruth.csv  -o data/ISIC_2020_Training_GroundTruth.csv
cd data/train
unzip images.zip
```

Then change `IMAGES_PATH` constant at the top of the `wldtools.py` file.

In order to save some time with repeated loading I preprocessed the images with `./scripts/image_loader.py`.
So all the images became square and 512x512 pixels, then I saved them into `./data/train_512`.
You can do it as well, but all should work fine without it, just likely a little slower.

Report
------

The report.pdf is in the root of this repository, check it out.

Implementation
--------------

All the implementation is in the `wldtools.py` file, run:
```sh
python3 wldtools.py --help
```

Analysis
--------

More details and graphs can be seen in the `visualizations.ipynb` notebook.
