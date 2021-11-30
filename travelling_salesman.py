import matplotlib.pyplot as plt
import pandas as pd
from simulated_annealing import anneal, calculate_whole_way

INITIAL_STEP = [x for x in range(0,20)] + [0]
cities = pd.read_csv('./cities.csv', sep=';')
distances = pd.read_csv('./distances.csv', sep=';')

plt.scatter(cities.longitude, cities.latitude, label='Russian cities', c='red', s=10)
plt.scatter(cities.iloc[0].longitude, cities.iloc[0].latitude, label='Moscow (starting point)', c='green', s=25)
print(f"Whole Way in the initial step {INITIAL_STEP} is {calculate_whole_way(cities, distances, INITIAL_STEP)}")
answ = anneal(cities, distances, INITIAL_STEP)
print(f"Simulated Annaeling: result={answ[0]} steps={answ[1]};function_calculation={answ[2]}; iterations={answ[3]}")
calculated_longitude = []
calculated_latitude = []

initial_longitude = []
initial_latitude = []

for step in answ[1]:
    calculated_longitude.append(cities.iloc[int(step)].longitude)
    calculated_latitude.append(cities.iloc[int(step)].latitude)

for step in INITIAL_STEP:
    initial_longitude.append(cities.iloc[int(step)].longitude)
    initial_latitude.append(cities.iloc[int(step)].latitude)

plt.plot(initial_longitude, initial_latitude, label='Initial step', linewidth=1)
plt.plot(calculated_longitude, calculated_latitude, label='dual annaeling', linewidth=2)

plt.xlabel('X-value')
plt.ylabel('Y-value')
plt.legend()
plt.grid(True)
plt.title(f"Travelling Salesman Problem (From Moscow to other cities)")
plt.show()