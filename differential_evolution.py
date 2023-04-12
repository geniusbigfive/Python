from scipy.optimize import differential_evolution
from scipy.optimize import NonlinearConstraint, Bounds
import scipy
import numpy as np

# define design variable 
bounds = [(0., 5.), (0., 5.)]

# define object function define
def objectFunction(x):
    return  -1 * (x[0] + 5 * x[1])

# define subject function
def constraintsFunction(x):
    return  -1 * (x[0] + 5 * x[1])

nlc = NonlinearConstraint(constraintsFunction, -8, 0 ) #constrai

# Optimize
result = differential_evolution(objectFunction, bounds, args=( ),polish=True, constraints=(nlc),strategy = 'randtobest1bin', init = 'latinhypercube', maxiter = 2000, tol=1e-6, mutation=0.8, disp = True)

print(result.x, result.fun)
