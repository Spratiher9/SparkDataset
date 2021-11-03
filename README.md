<a href="https://ibb.co/Lgpwxmq"><img src="https://i.ibb.co/t2CfqgN/sparkdatasets.png" alt="sparkdatasets" class="Center" border="0"></a>

## SparkDataset  [![PyPI version](https://badge.fury.io/py/sparkdataset.svg)](https://badge.fury.io/py/sparkdataset)  [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Spratiher9/SparkDataset/graphs/commit-activity) [![Downloads](https://static.pepy.tech/personalized-badge/sparkdataset?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=PYPI%20Downloads)](https://pepy.tech/project/sparkdataset)


Provides instant access to many datasets right from Pyspark (in Spark DataFrame structure).

*Drop a star if you like the project*.😃 Motivates💪 me to keep working on such projects

### What?

The idea is simple. There are various datasets available out there, but they are scattered in different places over the web.
Is there a quick way (in Pyspark) to access them instantly without going through the hassle of searching, downloading, and reading ... etc?
SparkDataset tries to address that question :)


### Usage:  

Start with importing `data()`:
```python
from sparkdataset import data
```
- To load a dataset:
```python
titanic = data('titanic')
```
- To display the documentation of a dataset:
```python
data('titanic', show_doc=True)
```
- To see the available datasets:
```python
data()
```
- To search for datasets with terms
```python
data('ab')

Did you mean:
crabs, abbey, Vocab
```

That's it.

Go to this [notebook](./how_to_use/sparkdataset.ipynb) for a demonstration of the functionality

### Why?

In `R`, there is a very easy and immediate way to access multiple statistical datasets,
in almost no effort. All it takes is one line ` > data(dataset_name)`.
This makes the life easier for quick prototyping and testing.
Well, I am jealous that Pyspark does not have a similar functionality.
Thus, the aim of `sparkdataset` is to fill that gap.

Currently, `sparkdataset` has about 757 (mostly numerical-based) datasets, that are based on `RDatasets`.
In the future, I plan to scale it to include a larger set of datasets.
For example,
1) include textual data for NLP-related tasks, and
2) allow adding a new dataset to the in-module repository.


### Installation:

`$ pip install sparkdataset`

#### Uninstall:

- `$ pip uninstall sparkdataset`
- `$ rm -rf $HOME/.sparkdataset`

### Changelog

**1.0.0**

- Added search dataset by name similarity.
- Example:

```python
>>> data('heat')
Did you mean:
Wheat, heart, Heating, Yeast, eidat, badhealth, deaths, agefat, hla, heptathlon, azt
```

- Added support to Windows.

### Dependency:
- pandas
- pyspark :: 3.1.2

### Miscellaneous:

- Tested on OSX and Linux (debian).
- Supports both Python 3 (3.8.8 and above).


#### TODO:
- add textual datasets (e.g. NLTK stuff).
- add samples generators.


#### Thanks to:

- [RDatasets](https://github.com/vincentarelbundock/Rdatasets): R's datasets collection.  
