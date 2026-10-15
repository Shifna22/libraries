import numpy as np

salary = np.array([25000, 32000, 45000, 28000, 50000, 38000])

print("Average salary:", np.mean(salary))
print("Highest salary:", np.max(salary))
print("Lowest salary:", np.min(salary))
print("Employees above 30000:", salary[salary > 30000])