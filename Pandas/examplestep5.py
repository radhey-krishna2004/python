

# 5 video
import pandas as pd

data = {
  "Name":['krishna', 'radhey', 'riyansh' , 'shyam', 'aman'],
  "Age":[10, 20, 30, 40, 50],
  "Salary":[50000, 40000, 550000, 56000, 54000],
  "performance score":[94, 34, 64, 45, 23]
    }

df= pd.DataFrame(data)

#display the data frame
print("Sample Dataframe")
print(df)
print("Names (Single column return series)")
name = df['Name']
print(df["name"])



#selecting the multiple colums

subset = df[["Name", "Salary"]]
print('\nSubset with Name and Salary')
print(subset)