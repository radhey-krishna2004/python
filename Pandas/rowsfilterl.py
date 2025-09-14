# 6 vdo

import pandas as pd

data = {
  "Name":['krishna', 'radhey', 'riyansh' , 'shyam', 'aman'],
  "Age":[10, 20, 30, 40, 50],
  "Salary":[50000, 40000, 550000, 56000, 54000],
  "performance_score":[94, 34, 64, 45, 23]
    }

df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 50000]
print('Employees with salary > 50000')
print(high_salary)

#filtering rows salary > 50k & age > 30

filtered= df[(df['Age'] > 30) & (df['Salary'] > 50000)]
print(f'Employee list Age > 30 + Salary > 50000')
print(filtered)

#using or condition


filtered_or= df[(df['Age'] > 30) | (df["performance_score"] > 50)]
print('Employee older than 35 or performance score>50')
print(filtered_or)