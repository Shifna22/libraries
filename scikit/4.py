import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X=np.array([[1],[2],[1],[4],[5],[6],[7],[8],[9],[10]])
y=np.array([1,0,0,0,0,1,0,1,1,1 ])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

model=LogisticRegression()
model.fit(X_train,y_train)
hours=np.array([[3]])
marks=model.predict(hours)
if marks[0]==1:
    print("pass")
else:
    print("fail")