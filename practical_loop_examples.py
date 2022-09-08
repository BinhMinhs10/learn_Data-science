import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

text = """
- at : is used to access a scaler value so it is lightweight (implementation is fast)
- loc and iloc : are meant to access multiple elements(series/dataframe) at the same time and thus takes more space and time
"""

data = pd.read_csv('datasets/seattleWeather_1948-2017.csv')
# print(data.head(10))
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
print("loc runtime: ", end - start)

# same manipulation by replacing ‘loc’ with ‘at’ (or replacing ‘iloc’ with ‘iat’)
start = time.time()
# Iterating through DataFrame
for index, row in data.iterrows():
    data.at[index, 'c'] = row.TMAX - row.TMIN
end = time.time()
print("at runtime: ", end - start)

print(text)