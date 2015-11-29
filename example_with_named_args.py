import pandas as pd
import numpy as np
import sys
import os
home = os.path.expanduser("~")
sys.path.append(home + '/code')
import mp_generic as mp
from datetime import datetime
import pytz
import time

EPOCH = datetime(1970, 1, 1, 0, 0, 0, tzinfo=pytz.utc)


def time_now(epoch=EPOCH):
    tt = datetime.utcnow().replace(tzinfo=pytz.utc)
    return (tt - epoch).total_seconds()


def timing(t0):
    t1 = time_now()
    return t1, t1 - t0


def apply_func(df, myStr="defult", wait=0.05, work=0.005):
    time.sleep(wait)
    time.sleep(work * len(df))
    g = pd.DataFrame({'len': [len(df)]})
    return g


df_len = 500
high_1 = 50
high_2 = 100
df = pd.DataFrame({'gb1': np.random.randint(low=0, high=high_1, size=df_len),
                   'gb2': np.random.randint(low=0, high=high_2, size=df_len),
                   'a': np.random.normal(size=df_len)})

gb_cols = ['gb1', 'gb2']

t0 = time_now()
print "######################## No parallel processing = ", t0
z = df.groupby(gb_cols).apply(apply_func, wait=0.01, work=0.001)
tdiff = timing(t0)
print "######################## No parallel processing = ", tdiff


mp_args = {'n_cpus': -1, 'queue': True, 'n_queues': None}

t0 = time_now()
print "############################# With parallel processing = ", t0
z = mp.mp_groupby(df, gb_cols, mp_args, apply_func, wait=0.01,work=0.001)
tdiff = timing(t0)
print "############################# With parallel processing = ", tdiff
