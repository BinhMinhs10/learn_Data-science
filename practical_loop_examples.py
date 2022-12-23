import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

text = """
- at : is used to access a scaler value so it is lightweight (implementation is fast)
- loc and iloc : are meant to access multiple elements(series/dataframe) at the same time and thus takes more space and time
"""

data = pd.read_csv('datasets/seattleWeather_1948-2017.csv')
print(data.shape)
print(data.head(5))

# loc function is used to access columns using column names
# while the iloc function is used to access columns using column indexes
print("Using loc to access data.loc[1,'PRCP']= ", data.loc[1, 'PRCP'])


"""
‘loc’ vs ‘at’ why the difference in the runtime?
"""
start = time.time()
# Iterating through the DataFrame df
for index, row in data.iterrows():
    data.loc[index, 'c'] = row.TMAX - row.TMIN
end = time.time()
print("1. using loc (access multiple elements series/dataframe) runtime: ", end - start)

# same manipulation by replacing ‘loc’ with ‘at’ (or replacing ‘iloc’ with ‘iat’)
start = time.time()
# Iterating through DataFrame
for index, row in data.iterrows():
    data.at[index, 'c'] = row.TMAX - row.TMIN
end = time.time()
print("2. using at (access a scaler) runtime: ", end - start)

# print(text)


# ============  Avoid using iterrows() because itertuples() can be 100 times faster ============
start = time.time()
# Iterating through DataFrame
list_c = []
for (col0, col1, col2, col3, col4, col5) in data.itertuples(index=None):
    list_c.append(col2 - col3)
data['c'] = list_c
# print(data.head())
end = time.time()
print("1. itertuples(index=None) runtime: ", end - start)


start = time.time()
# Iterating through DataFrame
list_c = []
for row in data.itertuples(index=False):
    list_c.append(row.TMAX - row.TMIN)
data['c'] = list_c
# print(data.head())
end = time.time()
print("2. itertuples(index=False) runtime: ", end - start)


start = time.time()
# Iterating through DataFrame
list_c = []
for row in data.itertuples(index=False):
    list_c.append(row[data.columns.get_loc('TMAX')] - row[data.columns.get_loc('TMIN')])
data['c'] = list_c
# print(data.head())
end = time.time()
print("3. Polyvalent Itertuples() (working even with special characters in the column name) runtime: {} seconds".format(end - start))
