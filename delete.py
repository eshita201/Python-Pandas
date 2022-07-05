import pandas as pd,os
import csv

os.system('cls')
data = pd.read_csv("Allfiles/nba.csv", index_col ="Name" )  
# dropping passed values
#data.drop(["Avery Bradley", "John Holland", "R.J. Hunter",
#                            "R.J. Hunter"], inplace = True)
data.drop(["Team", "Weight"], axis = 1, inplace = True)   
# display
data.to_csv("Allfiles/newfile.csv")

count=0

with open('Allfiles/newfile.csv','r') as csv_file:

   csv_reader = csv.reader(csv_file)

   for line in csv_reader:
      count = count+1
      #print(line)

print("count" ,count)
#print(data)