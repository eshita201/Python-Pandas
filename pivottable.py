import pandas as pd,os

os.system('cls')

boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle']
        }

df = pd.DataFrame(boxes, columns= ['Color','Shape'])

dups_color_and_shape = df.pivot_table(columns=['Color'], aggfunc='size')
print (dups_color_and_shape)