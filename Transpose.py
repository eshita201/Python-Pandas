import numpy as np
import pandas as pd,os

os.system('cls')

d1 = {'c1': [2, 3], 'c2': [4, 5]}
df1 = pd.DataFrame(data=d1)
print(df1)

df1_transposed = df1.T

print(df1_transposed)