import pandas as pd
data = {
    "Name": ["Anu", "Riya", "Amal", "Fathima", "Rahul"],
    "Age": [22, 25, 30, 28, 35],
    "City": ["Calicut", "Kochi", "Calicut", "Kochi", "Bangalore"],
    "Purchase": [4500, 6500, 3000, 8000, 5500]
}

df=pd.DataFrame(data)
print(df)
average_age=df["Age"].mean()
print("average_age:",average_age)

total=df["Purchase"].sum()
print("total:",total)

highest=df["Purchase"].max()
print("hiegt:",highest)

greater_5000=df[df["Purchase"]>5000]
print("5000 above:")
print(greater_5000)
