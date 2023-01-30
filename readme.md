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
