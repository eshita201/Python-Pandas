# Sorting Pandas Dataframe in Descending Order

# importing pandas library
import pandas as pd

# Initializing the nested list with Data set
age_list = [['Afghanistan', 1952, 8425333, 'Asia'],
			['Australia', 1957, 9712569, 'Oceania'],
            	['China', 1957, 637408000, 'Asia'],
			['France', 1957, 44310863, 'Europe'],
			['India', 1952, 3.72e+08, 'Asia'],
			['Brazil', 1962, 76039390, 'Americas'],
		
			['United States', 1957, 171984000, 'Americas']]

# creating a pandas dataframe
df = pd.DataFrame(age_list, columns=['Country', 'Year',
									'Population', 'Continent'])

# Sorting by column "Population"

#sf = df.sort_values(by=['Country'], ascending=False)

#sf = df.sort_values(by=['0'],inplace=True, ascending=False)
print(df)

cf =df.sort_index()

print(cf)
