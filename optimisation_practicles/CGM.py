import math

from numpy import gradient
from sympy import symbols, diff, solve, Eq, N, re, hessian
from sympy.core.evalf import evalf
from numdifftools import Gradient
import numpy as np

x_init = 5
y_init = 5
point_init = [x_init, y_init]
point_init = np.array(point_init)

x, y = symbols('x y')
expr = 100 * (y - x ** 2) ** 2 + (1 - x) ** 2

# expr = (x ** 2 - 10) ** 2 + (y - 5) ** 2
# expr = x**2+y**2+x+y+1
# expr = (x ** 2) / 2 + x * y + y ** 2


def gradient(expr, x_init, y_init):
    delta1 = diff(expr, x)
    delta2 = diff(expr, y)
    delta = []
    delta1 = delta1.subs({x: x_init, y: y_init})
    delta2 = delta2.subs({x: x_init, y: y_init})
    delta.append(delta1)
    delta.append(delta2)
    return delta


a = hessian(expr, [x, y]).subs({x: x_init, y: y_init})
a = np.array(a)
u0 = gradient(expr, x_init, y_init)

u0 = np.array(u0)
u0 = -1 * u0


def cgm(expr, u0, a, point):
    alpha_num = -np.matmul(u0, np.matmul(a, point))
    alpha_den = np.matmul(u0, np.matmul(a, u0))
    alpha = alpha_num / alpha_den
    bool = math.isnan(alpha)
    if not bool:
        next_point = point + np.dot(alpha, u0)
        print('point:', next_point)
        delta_new = gradient(expr, next_point[0], next_point[1])
        delta_new = np.array(delta_new)

        beta_num = np.matmul(delta_new, np.matmul(a, u0))
        beta_den = np.matmul(u0, np.matmul(a, u0))
        beta = beta_num / beta_den
        u_new = -delta_new + np.dot(beta, u0)
        cgm(expr, u_new, a, next_point)


cgm(expr, u0, a, point_init)
