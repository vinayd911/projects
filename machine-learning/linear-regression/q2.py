import numpy as np
import matplotlib.pyplot as plt
import math

#load dataset
data = np.loadtxt('P2input2024.txt')

#take time and spots data
t = data[:, 0]
y = data[:, 1]

#fit to given equation using normal equation
X = np.column_stack((np.ones_like(t), t, t**2, t**3, np.sin(np.pi / 8 * t)))
theta = np.linalg.inv(X.T @ X) @ (X.T @ y)
y_pred = X @ theta

#calculate MSE
mse = np.mean((y - y_pred)**2)
print("Learned parameters (a0, a1, a2, a3, b):", theta)
print("Mean Squared Error (MSE):", mse)

#prediction
def predict_full_utilization(theta):
    #solve equation using fsolve
    from scipy.optimize import fsolve
    def parking_lot_full(t):
        a0, a1, a2, a3, b = theta  # Extract parameters
        return a0 - (a1 * t + a2 * t**2 + a3 * t**3) - b * np.sin(np.pi / 8 * t)
    initial_guess = 12
    full_time = fsolve(parking_lot_full, initial_guess)
    return full_time[0]

full_utilization_time = predict_full_utilization(theta)
print(f"The parking lot will be fully utilized at t = {full_utilization_time:.2f} hours")

#plot data and prediction
plt.scatter(t, y, label='Original data')
plt.plot(t, y_pred, color='red', label='Fitted model')
plt.axvline(x=full_utilization_time, color='green', linestyle='--', label=f'Full utilization at t={full_utilization_time:.2f}')
plt.xlabel('Time (hours)')
plt.ylabel('Available Parking Spots')
plt.legend()
plt.savefig('parking_lot_plot.png')
