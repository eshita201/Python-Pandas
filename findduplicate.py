from tkinter import LAST
import pandas as pd,os
os.system('cls')
#data = pd.read_csv("Allfiles/employees.csv")
employees = [('Stuti', 28, 'Varanasi'),
            ('Saumya', 32, 'Delhi'),
            ('Aaditya', 25, 'Mumbai'),
            ('Saumya', 32, 'Delhi'),
            ('Saumya', 32, 'Delhi'),
            ('Saumya', 32, 'Mumbai'),
            ('Aaditya', 40, 'Dehradun'),
            ('Seema', 32, 'Delhi')
            ]
 
df = pd.DataFrame(employees,
                   columns = ['Name', 'Age', 'City'])
duplicate = df[df.duplicated(['Name', 'Age'])]
#print("Duplicate Rows based on Name and Age :")
#print(duplicate)


df.drop_duplicates(subset ="Name",keep = False, inplace = True)
print(df)




# sorting by first name
#df.sort_values("Name", inplace = True)
# 
## dropping ALL duplicate values
#df.drop_duplicates(subset ="Name",keep = LAST, inplace = True)
#print(df)


