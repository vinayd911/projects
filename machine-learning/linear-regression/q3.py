import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from scipy.optimize import fsolve

#load dataset
data = np.loadtxt('P2input2024.txt')

#take time and spots data
t = data[:, 0]
y = data[:, 1]

#Q3a
a0 = 100
a1_values = [0, 1]
a2_values = [0.2, 0.4]
a3_values = [0, 4]
b_values = [20, 40]

param_combinations = list(product(a1_values, a2_values, a3_values, b_values))

def calculate_mse(t, y, a0, a1, a2, a3, b):
    X = np.column_stack((np.ones_like(t), t, t**2, t**3, np.sin(np.pi / 8 * t)))
    theta = [a0, a1, a2, a3, b]
    y_pred = X @ theta
    mse = np.mean((y - y_pred)**2)
    return mse, y_pred

#store MSE in
results = []

#iterate over all parameter combinations
for a1, a2, a3, b in param_combinations:
    mse, _ = calculate_mse(t, y, a0, a1, a2, a3, b)
    results.append(((a1, a2, a3, b), mse))

#Q3b
sorted_results = sorted(results, key=lambda x: x[1])

#sort parameters set
print("Sorted parameter sets by MSE:")
for params, mse in sorted_results:
    print(f"Parameters (a1, a2, a3, b): {params}, MSE: {mse}")

#Q3c
best_params = sorted_results[:4]

plt.figure(figsize=(10, 6))
plt.scatter(t, y, label='Original data', color='blue')

for i, (params, mse) in enumerate(best_params):
    a1, a2, a3, b = params
    _, y_pred = calculate_mse(t, y, a0, a1, a2, a3, b)
    plt.plot(t, y_pred, label=f'Best Set {i+1}: a1={a1}, a2={a2}, a3={a3}, b={b} (MSE={mse:.2f})')

plt.xlabel('Time (hours)')
plt.ylabel('Available Parking Spots')
plt.legend()
plt.title('Best 4 Parameter Sets with Lowest MSE')
plt.savefig('q3_best_params_plot.png')

#Q3d
a0_200 = 200
best_a1, best_a2, best_a3, best_b = best_params[0][0]

def predict_full_utilization_200(a0, a1, a2, a3, b):
    def parking_lot_full(t):
        return a0 - (a1 * t + a2 * t**2 + a3 * t**3) - b * np.sin(np.pi / 8 * t)
    initial_guess = 12
    full_time = fsolve(parking_lot_full, initial_guess)
    return full_time[0]

full_utilization_time_200 = predict_full_utilization_200(a0_200, best_a1, best_a2, best_a3, best_b)
print(f"With a0=200, the parking lot will be fully utilized at t = {full_utilization_time_200:.2f} hours")

#Q3e
time_until_full = np.arange(0, full_utilization_time_200, 0.1) 

def calculate_y_pred_for_range(a0, a1, a2, a3, b, time_range):
    return a0 - (a1 * time_range + a2 * time_range**2 + a3 * time_range**3) - b * np.sin(np.pi / 8 * time_range)

y_pred_until_full = calculate_y_pred_for_range(a0_200, best_a1, best_a2, best_a3, best_b, time_until_full)

plt.figure(figsize=(10, 6))

plt.scatter(t, y, label='Original data', color='blue')

plt.plot(time_until_full, y_pred_until_full, color='red', label=f'Predicted availability (a0=200)')

#mark the point of full utilization
plt.axvline(x=full_utilization_time_200, color='green', linestyle='--', label=f'Full utilization at t={full_utilization_time_200:.2f} hours')

plt.xlabel('Time (hours)')
plt.ylabel('Available Parking Spots')
plt.legend()
plt.title('Prediction for a0=200 (Parking Lot Expansion until full utilization)')
plt.savefig('q3e_200_spots_full_utilization_plot.png')
