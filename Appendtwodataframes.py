import pandas as pd,os
os.system('cls')

data = {'Name' :['Eshita','John'],
        'Age'  :[26,30]}
data1 = {'Name' : ['Ram','Lakshman'],
         'Age'  : [23,24]}
df=pd.DataFrame(data)
df.index+=1
df1=pd.DataFrame(data1)
df1.index+=1
df1=pd.concat([df,df1])
    
print(df1)