from setuptools import setup

setup(name='rutgerhofstepythonpackage',
      version='0.1.2',
      description='Test python package with documentation and CI',
      url='http://github.com/rutgerhofste/my-python-package',
      author='Rutger Hofste',
      author_email='rutgerhofste@gmail.com',
      license='MIT',
      packages=['rutgerhofstepythonpackage'],
      install_requires=['pandas'],
      zip_safe=False)
