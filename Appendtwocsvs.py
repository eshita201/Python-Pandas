import pandas as pd,os

os.system('cls')

path1 = pd.read_csv("Allfiles/demofile1.csv")
path2 = pd.read_csv("Allfiles/demofile2.csv")

merge = pd.concat([path1,path2])
print(merge)