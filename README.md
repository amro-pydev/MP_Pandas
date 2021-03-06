pandas_multiprocessing
=========

Python package that supports multiprocessing apply command on pandas dataframe. Very helpful for large massive dataframes.

Installation:
=============
To install from Pypi:

     pip install pandas_multiprocessing
     
To install from source:

     git clone https://github.com/amro-pydev/pandas_multiprocessing.git
     cd pandas_multiprocessing
     python setup.py install

Multiprocessing groupby/apply:
===========================================

Original syntax for apply or groupby/apply:
```python
data_frame.groupby(column_list).apply(apply_func, *args, **kwargs)
```

You could multiprocess this apply command by using our package:
```python
import pandas_multiprocessing as pdmp
pdmp.mp_groupby(data_frame, column_list, apply_func, *args, **kwargs)
```

The arguments to mp_groupby() are the same as in the Pandas groupby/apply except for the additional mp_arg argument, which contains multiprocessing information such as the number of CPUs to use and load balancing information.
