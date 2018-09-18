from __future__ import division
import os
import json
import numpy as np
import re
import pandas as pd
import seaborn as sns
import matplotlib
from matplotlib import pylab, mlab, pyplot
from IPython.core.pylabtools import figsize, getfigs
plt = pyplot
import seaborn as sns
sns.set_context('poster')
sns.set_style('white')

def convert_numeric(X,col):
    ## make numeric types for aggregation
    X[col] = pd.to_numeric(X[col])
    return X