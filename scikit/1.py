from sklearn.datasets import load_iris
iris = load_iris()
print("Feature names:")
print(iris.feature_names)
print("\nFirst 5 rows:")
print(iris.data[:5])
print("\nFlower types:")
print(iris.target_names)



