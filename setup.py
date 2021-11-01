#!/usr/bin/env python

# Author: Souvik Pratiher
# email: spratiher9@gmail.com

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='sparkdataset',
    description=("Provides instant access to many popular datasets right from "
                 "Pyspark (in dataframe structure)."),
    author='Souvik Pratiher',
    url='https://github.com/Spratiher9/SparkDataset',
    # download_url='https://github.com/Spratiher9/SparkDataset/tarball/0.1.0',
    license = 'MIT',
    author_email='spratiher9@gmail.com',
    version='0.1.0',
    install_requires=['pandas','pyspark==3.1.2'],
    packages=['sparkdataset', 'sparkdataset.utils'],
    package_data={'sparkdataset': ['*.gz', 'resources.tar.gz']}
)