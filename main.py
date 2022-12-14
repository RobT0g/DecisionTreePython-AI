import pandas as pd
import numpy as np

df = pd.read_csv('./iris.csv', skiprows=1, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'type'])
print(df)
