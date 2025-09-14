"""  --------------5 vdo
1- how big is your dataset
2- what are the names of columns

shape => tells rows and coulumns
 and columns = > name of colums

"""

import pandas as pd
data = {
  "Name":['krishna', 'radhey', 'riyansh' , 'shyam', 'aman'],
  "Age":[10, 20, 30, 40, 50],
  "Salary":[50000, 40000, 550000, 56000, 54000],
  "performance score":[94, 34, 64, 45, 23]
    }

df= pd.DataFrame(data)
print(df)

print(f'shape: {df.shape}')
print(f'Column Names: {df.columns}')
