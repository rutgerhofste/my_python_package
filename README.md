# my_python_package
cheatsheet and template for a python package

the result is a python package that can be installed using 
`pip install mypackage` and `conda install mypackage` and has proper documentation and testing. For testing we use Travis CI and for the documentation we use readthedocs.

Pre-Requisites:
1. Git and Github
1. Python
1. Basic command line

# Python Package
follow [this](https://python-packaging.readthedocs.io/en/latest/index.html) and [this](https://packaging.python.org/tutorials/distributing-packages/) guide. Do not use sdist to upload your script. Use Twine for a secure way. Summary below:

## Pypi


1. Install requirements  
`pip install wheel`  
`pip install twine`

1. Create an account on the PyPi website (verify email):
https://pypi.org/account/register/

[install-requires-vs-requirements](https://packaging.python.org/discussions/install-requires-vs-requirements/#install-requires-vs-requirements-files)


1. Create a repository.
1. Copy files from template folder of this repor to home of your repo.
1. Rename folders to yourname_python_package
1. Replace rutgerhofste in setup.py with your package name. 
1. cd to repo (folder with setup.py)
1. Create the wheel  
`python setup.py bdist_wheel --universal`
1. Upload built package to pypi
`twine upload dist/*`

## Conda
follow [this](https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html) guide. Summary below:

1. Install [anaconda or miniconda](https://conda.io/docs/user-guide/install/index.html)
1. Install anaconda-client
`conda install anaconda-client`

1. Register at [anaconda cloud](https://anaconda.org/)
1. Login  
`anaconda login`




# Documentation

# Testing
