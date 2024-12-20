import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#load dataset
data = np.loadtxt('P2input2024.txt')

#take time and spots data
t = data[:, 0]
y = data[:, 1]

#fit to given equation
X = np.column_stack((np.ones_like(t), t, t**2, t**3, np.sin(np.pi / 8 * t)))
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

#calculate MSE
mse = mean_squared_error(y, y_pred)
print("Fitted parameters (a0, a1, a2, a3, b):", model.coef_)
print("Mean Squared Error (MSE):", mse)

#plot data and predictions
plt.scatter(t, y, label='Original data')
plt.plot(t, y_pred, color='red', label='Fitted model')
plt.xlabel('Time (hours)')
plt.ylabel('Available Parking Spots')
plt.legend()
plt.savefig('parking_lot_plot.png')