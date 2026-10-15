import pandas as pd
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12000, 15000, 11000, 18000, 20000, 17000]
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print("Total sales:", df["Sales"].sum())

highest = df.loc[df["Sales"].idxmax()]
print("Highest sales:")
print(highest)


