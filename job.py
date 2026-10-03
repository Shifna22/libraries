import pandas as pd

data = {
    "Job": ["Data Analyst", "Data Scientist", "Data Analyst",
            "ML Engineer", "Data Analyst", "BI Analyst"],
    "Skill": ["Python", "Python", "SQL", "Machine Learning",
              "Power BI", "Power BI"],
    "Location": ["Kochi", "Bangalore", "Calicut",
                 "Bangalore", "Kochi", "Calicut"]
}

df =pd.DataFrame(data)

print(df)

count=df["Job"].value_counts()
print(count)
print(df.isnull())
