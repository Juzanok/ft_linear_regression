import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(theta0_now, theta1_now, points, L):
    theta0tmp = theta0_now
    theta1tmp = theta1_now

    m = len(points)
    
    sum_theta0 = 0
    sum_theta1 = 0

    for i in range(m):
        x = points.iloc[i].normalized_km
        y = points.iloc[i].normalized_price

        sum_theta0 += ((theta0tmp + (theta1tmp * x)) - y)
        sum_theta1 += ((theta0tmp + (theta1tmp * x)) - y) * x

    theta0tmp -= (L / m) * sum_theta0
    theta1tmp -= (L / m) * sum_theta1

    return theta0tmp, theta1tmp

data = pd.read_csv('data.csv')

mean_km = np.mean(data['km'])
std_km = np.std(data['km'])

mean_price = np.mean(data['price'])
std_price = np.std(data['price'])

data['normalized_km'] = (data['km'] - mean_km) / std_km
data['normalized_price'] = (data['price'] - mean_price) / std_price

theta0 = 0
theta1 = 0
epochs = 10000
L = 0.000001

for i in range(epochs):
    if (i % 50 == 0) :
        print(f"Generation: {i}")
    theta0, theta1 = gradient_descent(theta0, theta1, data, L)

with open('theta.csv', 'w') as output:
    output.write(f"{theta0},{theta1}")

plt.title("Real values")
plt.xlabel("km")
plt.ylabel("price")

plt.scatter(data['normalized_km'], data['normalized_price'], color="blue")

x_range = np.linspace(min(data['normalized_km']), max(data['normalized_km']), 100)
y_range = [theta0 + theta1 * ((x - mean_km) / std_km) for x in x_range]

plt.plot(x_range, y_range, color="red")

plt.show()

