import pandas as pd
import numpy as np

# SERIES
s = pd.Series([1, 2, 3, 4, 5])
print(s)

# Create series from dictionary
s2 = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(s2)

# Create series with custom index
data=[10, 20, 30,]
index=['a', 'b', 'c']
s3=pd.Series(data, index=index)
print(s3)

## DATAFRAME
# Create DataFrame from dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 25, 26],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
print(np.array(df))

# Create DataFrame from list of dictionaries
data2 = [
    {'Name': 'Alice', 'Age': 24, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 26, 'City': 'Chicago'}
]
df2 = pd.DataFrame(data2)
print(df2)  