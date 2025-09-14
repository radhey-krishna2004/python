-------------7--------
#adding columns here

import pandas as pd

data = {
  "Name":['krishna', 'radhey', 'riyansh' , 'shyam', 'aman'],
  "Age":[10, 20, 30, 40, 50],
  "Salary":[50000, 40000, 550000, 56000, 54000],
  "performance_score":[94, 34, 64, 45, 23]
    }

df = pd.DataFrame(data)
print(df)

#square brackets df("column name") = some Data

df["Bonus"] = df['Salary'] * 0.1
print(df)