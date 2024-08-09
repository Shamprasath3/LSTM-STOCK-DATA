import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
start = '2010-01-01'
end = '2020-01-01'
df = data.DataReader('AAPL', 'yahoo', start, end)
df.head()
