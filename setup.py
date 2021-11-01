#!/usr/bin/env python

# Author: Souvik Pratiher
# email: spratiher9@gmail.com

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(('README.md'), encoding='utf-8') as readme:
    bdescription = readme.read()


setup(
    name='sparkdataset',
    description=("Provides instant access to many popular datasets right from "
                 "Pyspark (in dataframe structure)."),
    author='Souvik Pratiher',
    url='https://github.com/Spratiher9/SparkDataset',
    download_url='https://github.com/Spratiher9/SparkDataset/archive/refs/tags/1.0.0.tar.gz',
    license = 'MIT',
    author_email='spratiher9@gmail.com',
    version='1.0.0',
    long_description=bdescription,
    long_description_content_type='text/markdown',
    keywords=['Spark', 'Apache Spark', 'benchmarking', 'data', 'datasets', 'standard data'],
    install_requires=['pandas','pyspark==3.1.2'],
    packages=['sparkdataset', 'sparkdataset.utils'],
    package_data={'sparkdataset': ['*.gz', 'resources.tar.gz']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10'
    ]
)