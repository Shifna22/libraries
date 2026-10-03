import pandas as pd

data = {
    "Name": ["Anu", "Amal", "Sara", "Rahul"],
    "Age": [21, 22, 20, 23],
    "Mark": [85, 78, 92, 67]
}

df = pd.DataFrame(data)

print(df)
print(df["Name"])
