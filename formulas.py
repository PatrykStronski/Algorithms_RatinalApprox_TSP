import math
import numpy as np
from random import random

DELTA_NOISE =  np.random.randn(1000)
SUPERSMALL_NUMBER = 0.000000000000001
alpha = random()
beta = random()

def fx(x: float) -> float:
    return 1 / (x**2 - 3* x + 2)

"""noise generator from 2nd task"""
def gen_noisy_data(k: int) -> float:
    x = 3 * k / 1000
    f = fx(x)
    delta = DELTA_NOISE[k]
    if f < -100:
        return -100 + delta
    if f <= 100:
        return f + delta
    return 100 + delta

NOISY_DATA = [] 
X_ES = []

for k in range(0,1000):
    x = 3 * k / 1000
    NOISY_DATA.append(gen_noisy_data(k))
    X_ES.append(x)

def approximant(x: float, a:float, b:float, c:float, d:float) -> float:
    return (a * x + b) / (x**2 + c * x + d + SUPERSMALL_NUMBER)

def approximant_summed(point: (float, float, float, float)) -> float:
    return [approximant(X_ES[k], point[0], point[1], point[2], point[3]) - NOISY_DATA[k] for k in range(0,1000)] 

"""Least squares method that for function func calculates lest square sum"""
def least_squares_custom(point: (float, float, float, float)) -> float:
    sum = 0
    for k in range(0,1000):
        y = NOISY_DATA[k]
        x = X_ES[k]
        sum += (approximant(x, point[0], point[1], point[2], point[3]) - y) **2
    return sum