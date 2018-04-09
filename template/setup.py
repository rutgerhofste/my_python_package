from setuptools import setup

setup(name='rutgerhofste-python-package',
      version='0.0.1',
      description='Test python package with documentation and CI',
      url='http://github.com/rutgerhofste/my-python-package',
      author='Rutger Hofste',
      author_email='rutgerhofste@gmail.com',
      license='MIT',
      packages=['rutgerhofste-python-package'],
      install_requires=['pandas'],
      zip_safe=False)
