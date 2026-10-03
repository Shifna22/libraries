import pandas as pd

data = {
"Name": ["Arun", "Rahul", "Anu", "Meera"],
"mark": [85, 72, 91, 65]
}
df = pd.DataFrame(data)

print("average:",df["mark"].mean())
print("heighest:",df["mark"].max())
print("lowest:",df["mark"].min())