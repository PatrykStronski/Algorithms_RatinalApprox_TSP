import pandas as pd
import math
import random

alpha = 0.8
ITERATIONS_PER_TEMP = 5
MAX_ITERS = 1000000
INITIAL_TEMPERATURE = 1000
CRITICAL_TEMPERATURE = 0.01

def calculate_whole_way(cities: pd.DataFrame, distances: pd.DataFrame, steps: [int]) -> float:
    distance_sum = 0.0
    city1 = cities.iloc[int(steps[0])].city
    for s in range(1,len(steps)):
        city2 = cities.iloc[int(steps[s])].city
        distance_sum += distances.loc[(distances.city1 == city1) & (distances.city2 == city2)].iloc[0].distance
        city1 = city2
    return distance_sum

def temperature_reduction(current_temp: float) -> float:
    return current_temp * alpha

def generate_neighbouring_solution(sol: [int]):
    to_exchange1 = 100
    to_exchange2 = 100
    while to_exchange1 == to_exchange2:
        to_exchange1 = random.randint(1, 19)
        to_exchange2 = random.randint(1, 19)
    tmp = sol[to_exchange1]
    sol[to_exchange1] = sol[to_exchange2]
    sol[to_exchange2] = tmp
    return sol

def accept_new(cost_change: float, temperature: float) -> bool:
    if cost_change > 0:
        return True

    prob_remain = math.exp(cost_change/temperature)
    ran = random.random()
    return prob_remain >= ran


def anneal(cities: pd.DataFrame, distances: pd.DataFrame, initial_guess: [int]) -> (float, [int], int, int):
    primary_guess = initial_guess.copy()
    temperature = INITIAL_TEMPERATURE
    i = 0
    while i < MAX_ITERS and temperature > CRITICAL_TEMPERATURE:
        for x in range(0, ITERATIONS_PER_TEMP):
            i += 1
            neighbor = generate_neighbouring_solution(primary_guess.copy())
            road_primary = calculate_whole_way(cities, distances, primary_guess)
            road_neighbor = calculate_whole_way(cities, distances, neighbor)
            cost_diff = road_primary - road_neighbor

            an = accept_new(cost_diff, temperature)
            if an:
                primary_guess = neighbor
                road_primary = road_neighbor
        temperature = temperature_reduction(temperature)
    return (road_primary, primary_guess, 2 * i, i)