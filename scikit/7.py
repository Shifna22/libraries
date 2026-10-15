
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
iris = load_iris( )
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42, stratify=y)
dt = DecisionTreeClassifier(random_state=42)
lr = LogisticRegression(max_iter=200)
dt.fit(X_train, y_train)
lr.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
lr_pred = lr.predict(X_test)
dt_acc = accuracy_score(y_test, dt_pred)
lr_acc = accuracy_score(y_test, lr_pred)
print("Decision Tree Accuracy:", dt_acc)
print("Logistic Regression Accuracy:", lr_acc)
if dt_acc > lr_acc:
    print("Decision Tree performs better.")
elif lr_acc > dt_acc:
    print("Logistic Regression performs better.")
else:
    print("Both models have equal accuracy.")
