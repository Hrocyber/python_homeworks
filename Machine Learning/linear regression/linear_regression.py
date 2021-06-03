from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

first_np = np.array([22, 23, 22, 25, 24, 26, 28, 24, 25, 29])
second_np = np.array([24, 27, 32, 35, 34, 36, 38, 34, 35, 39])
first_np = first_np.reshape(-1, 1)  # miachapic erkchap

plt.scatter(first_np, second_np, color='pink', marker="*")
plt.plot(first_np, second_np )  # ketagcer
plt.xlabel("first")
plt.ylabel("second")
model = LinearRegression()
model.fit(first_np, second_np)
y_pred = model.predict([[input("input number ")]])
print(y_pred)
plt.show()
