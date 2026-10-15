from sklearn.model_selection import train_test_split
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print("Training data:",X_train)
print("Testing data:",X_test)
print("Training labels:",y_train)
print("Testing labels:",y_test)