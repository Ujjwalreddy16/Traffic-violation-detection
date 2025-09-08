import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('Iris')
print("Iris dataset loaded successfully.")
data.head()
correlation = data[['sepal_length','petal_length']].corr(method='pearson')
print("pearson correlation coefficient:\n")
print("correlation")
covariance = data[['sepal_length','petal_length']].cov()
print("covariance matrix:\n")
print("covariance")
x_col = 'sepal_lenght'
y_col = 'petal_length'
plt.figure(figsize=(8,5))
plt.scatter(data[x_col], data[y_col], color = purple, alpha = 0.6)
plt.xlabel(x_col.capitalize())
plt.ylabel(y_col.capitalize())
plt.title(f"scatter plot of {x_col} and {y_col}")
plt.grid(True)
plt.show()