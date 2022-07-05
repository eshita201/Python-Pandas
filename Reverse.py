import pandas as pd
 
# Define a dictionary containing employee data
data = {'Income': [150000, 13000, 11000, 11000],
        'Expenses': [10000, 11000, 7000, 50000],
        'Profit': [5000, 2000, 4000, 6000]
        }
 
 
# Convert the dictionary into DataFrame
dataframe = pd.DataFrame(data)
Data_reverse_row_1 = dataframe.iloc[::-1]
# Observe the result
print(Data_reverse_row_1)