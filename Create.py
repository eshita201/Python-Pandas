from csv import reader
from operator import index
import pandas as pd,os
from pandas.io.formats.style import Styler
import xlsxwriter
os.system('cls')
data = {'Name':['Ashika', 'Tanu', 'Ashwin', 'Mohit', 'Sourabh'],
        'Age': [24, 23, 22, 19, 10]}
#df = pd.DataFrame(data)
#df.index+=1
#print(df[['Age']])
#df.to_excel("outputfile.xlsx") 
##df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])
df = pd.DataFrame(data)
df.index.names =['SNo']
df.index+=1  
df.to_csv('path_to_csv_file.csv',index=False)
df.to_csv('Allfiles/demofile1.csv',index=False)
df.to_csv('Allfiles/demofile2.csv',index=False)
with pd.ExcelWriter("path_to_excel_file.xlsx") as writer:
 df.to_excel(writer) 
with pd.ExcelWriter("Allfiles/demoxlfile1.xlsx") as writer:
 df.to_excel(writer) 
with pd.ExcelWriter("Allfiles/demoxlfile2.xlsx") as writer:
 df.to_excel(writer) 
df=pd.read_excel("path_to_excel_file.xlsx")
#df = pd.read_csv('path_to_csv_file.csv', index_col=0) 
blankIndex=[''] * len(df)
df.index=blankIndex
print(df[['Name','Age','SNo']])
#df.index.names = ['S.no']


