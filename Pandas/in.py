----------3 vdo---------------

import pandas as pd

#df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})

data = {
    "Nmae":['ram', 'krishna', 'ghanshyam'],
    "Age":[1, 2, 3],
     "city":['nagpur', 'mumbai', 'delhi']
}

df = pd.DataFrame(data)
print('displaying the info of data set')
print(df.info())
