import matplotlib.pyplot as plt
from algorithms import nelder_mead, levenberg_marquadt, diff_evolution, dual_ann
from formulas import NOISY_DATA, X_ES, approximant

PRECISION = 0.001
START = [0.1, 0.1, 0.1, 0.1]
BOND = [(0,1), (0,1), (0,1), (0,1)]
MAX_ITERS = 1000

plt.scatter(X_ES, NOISY_DATA, label='Y noisy data', c='pink', s=1)

answ = nelder_mead(START, PRECISION)
print(f"Nelder-Mead Search: result={answ[0]} a={answ[1][0]}; b={answ[1][1]};function_calculation={answ[2]}; iterations={answ[3]}")
plt.plot(X_ES, [approximant(x, answ[1][0], answ[1][1], answ[1][2], answ[1][3]) for x in X_ES], label='Nelder-Mead method')

answ = levenberg_marquadt(START, PRECISION)
print(f"Levenberg-Marquadt: a={answ[1][0]}; b={answ[1][1]}; c={answ[1][2]} ; d={answ[1][3]};function_calculation={answ[2]}; jacobian_calculations={answ[3]}")
plt.plot(X_ES, [approximant(x, answ[1][0], answ[1][1], answ[1][2], answ[1][3]) for x in X_ES], label='Levenberg-Marquadt', linewidth=1)

answ = diff_evolution(START, BOND, PRECISION, MAX_ITERS)
print(f"Differential evolution: result={answ[0]} a={answ[1][0]}; b={answ[1][1]}; c={answ[1][2]} ; d={answ[1][3]};function_calculation={answ[2]}; iterations={answ[3]}")
plt.plot(X_ES, [approximant(x, answ[1][0], answ[1][1], answ[1][2], answ[1][3]) for x in X_ES], label='differential evolution', linewidth=1)

answ = dual_ann(START, BOND, MAX_ITERS)
print(f"Dual Annaeling: result={answ[0]} a={answ[1][0]}; b={answ[1][1]}; c={answ[1][2]} ; d={answ[1][3]};function_calculation={answ[2]}; iterations={answ[3]}")
plt.plot(X_ES, [approximant(x, answ[1][0], answ[1][1], answ[1][2], answ[1][3]) for x in X_ES], label='dual annaeling', linewidth=1)

plt.xlabel('X-value')
plt.ylabel('Y-value')
plt.legend()
plt.grid(True)
plt.title(f"Data and its rational approximation with precision {PRECISION}")
plt.show()