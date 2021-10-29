from typing import Callable
from formulas import approximant, approximant_summed, least_squares_custom
from scipy.optimize import least_squares, minimize, differential_evolution, dual_annealing

def levenberg_marquadt(start: [float], precision: float) -> (float, (float, float), int, int):
    ans = least_squares(approximant_summed, start, method='lm', ftol=precision, xtol=precision)
    val = least_squares_custom(ans.x)
    return (val, ans.x, ans.nfev, ans.njev)

def nelder_mead(start: [float], precision: float) -> (float, (float, float), int, int):
    ans = minimize(least_squares_custom, start, method='Nelder-Mead', tol=precision)
    val = least_squares_custom(ans.x)
    return (val, ans.x, ans.nfev ,ans.nit)

def diff_evolution(start: [float], bond: [(float ,float)], precision: float, iters: int) -> (float, (float, float), int, int):
    ans = differential_evolution(least_squares_custom, bond, x0=start, tol=precision, maxiter=iters)
    val = least_squares_custom(ans.x)
    return (val, ans.x, ans.nfev ,ans.nit)

def dual_ann(start: [float], bond: [(float ,float)], iters: int) -> (float, (float, float), int, int):
    ans = dual_annealing(least_squares_custom, bond, x0=start, maxiter=iters, no_local_search=True)
    val = least_squares_custom(ans.x)
    return (val, ans.x, ans.nfev ,ans.nit)