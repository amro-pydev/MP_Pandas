import pandas as pd
import numpy as np
import sys
import os
import MP_Pandas as mp
from datetime import datetime
import time

def apply_func(df, wait, work):
    time.sleep(wait)
    time.sleep(work * len(df))
    g = pd.DataFrame({'len': [len(df)]})
    return g


df_len = 10000
high_1 = 2
high_2 = 3
df = pd.DataFrame({'gb1': np.random.randint(low=0, high=high_1, size=df_len),
                   'gb2': np.random.randint(low=0, high=high_2, size=df_len),
                   'a': np.random.normal(size=df_len)})

gb_cols = ['gb1', 'gb2']
args = [0.01, 0.001]  # wait, work

t0 = time.time()
z = df.groupby(gb_cols).apply(apply_func, *args)
print("## Single thread run time {:f} seconds.".format(time.time() - t0))


mp_args = {'n_cpus': 6, 'queue': True, 'n_queues': None}

t0 = time.time()
z = mp.mp_groupby(df, gb_cols, apply_func, *args, **mp_args)
print("## Parallel run time {:f} seconds.".format(time.time() - t0))
