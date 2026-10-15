import pandas as pd
data={
      "product":["bag","book","pen","pencil"],
      "price":[10,20,30,23],
      "quantity":[1,3,4,9,10]
 }
df=pd.DataFrame(data)
df["total:"]=df["price"]*df["quantity"]
print(df)
print("sales:",df["total"].sum())
print("average:",df["total"].mean())
print("lowest:",df["total"].min())