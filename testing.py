import numpy
import pandas as pd
from sympy import false

for df in pd.read_csv('testingdata.csv', chunksize=1):
    print(df['own_goal'].iloc[0] == 0)
