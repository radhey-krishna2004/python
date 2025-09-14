#step 1 sample data frame ----------------- 4vdo-----------

import pandas as pd
data = {
  "Name":['krishna', 'radhey', 'riyansh' , 'shyam', 'aman'],
  "Age":[10, 20, 30, 40, 50],
  "Salary":[50000, 40000, 550000, 56000, 54000],
  "performance score":[94, 34, 64, 45, 23]
    }

df= pd.DataFrame(data)
print("Sample Dataframe")
print(df)
print('Descrtptive Statistics')
print(df.describe())