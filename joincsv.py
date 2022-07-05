import pandas as pd
df_product=pd.read_csv("Allfiles/product.csv")
df_customer=pd.read_csv("Allfiles/customer.csv")

merge_data=pd.merge(df_product,df_customer,on='Product_ID',how='inner')
print(merge_data['Product_ID'])