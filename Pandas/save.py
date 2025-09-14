# videio 1

import pandas as pd

data = {
    "Nmae":['ram', 'krishna', 'ghanshyam'],
    "Age":[1, 2, 3],
     "city":['nagpur', 'mumbai', 'delhi']
}

df = pd.DataFrame(data)     #
print(df)


# ----------------how to save data------------


# df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
# df.to_json("output.json", index=False)