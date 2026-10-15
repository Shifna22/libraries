
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
X = np.array([[500], [700],[900], [1000], [1200],
              [1500], [1800], [2000], [2200], [2500]])

y = np.array([10, 14, 18, 20, 24, 30, 36, 40, 44, 50])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

area=np.area([[1600]])
predicted_price=model.predict(area)
print("predicted price:",predicted_price=[0],"lak")
