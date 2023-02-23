import time
from math import sin
import random

from sympy import symbols
import sympy as sy
import math

from sympy.plotting import plot3d
import matplotlib.cm as cm
st = time.time()

x, y, E, t = symbols('x y E t')
# expr = sy.exp(x)-sy.sin(x)
expr = -(sy.sin(x)) + x ** 2
# expr = ((x**4)+1)/((x**2)+1)
# expr = 500 - 20*x - 26*y - 4*x*y + 4*x**2 + 3*y**2


# expr = -(1+ sy.cos(12*sy.sqrt(x**2+y**2)))/(0.5*(x**2+y**2)+2)

c = 0.8

T = 0.000005

metropolis_expr = 1/(1+(sy.exp(E/t)))
# metropolis_expr = sy.exp(-E/T)

x_point = 150
y_point = 150
plot3d((expr,(x, -2, 2), (y, -2, 2)),((0,0,0)), use_cm=True)
# p._backend.ax.collections[0].set_cmap("magma")
# p._backend.ax[0].figure.show()
# while(T>0.00000005):
#     for i in range(100):
#         f_0 = expr.subs({x: x_point, y: y_point})
#         print('dfgdfvdfbv', f_0)
#         u1 = random.random()
#         u2 = random.random()
#         print("u: ", u1, u2)
#         tol = 6
#         x_range = []
#         y_range = []
#         x_range.append(x_point - tol)
#         x_range.append(x_point + tol)
#         y_range.append(y_point - tol)
#         y_range.append(y_point + tol)
#
#         x_temp = x_range[0] + u1 * (2*tol)
#         y_temp = y_range[0] + u2 * (2*tol)
#
#         f_1 = expr.subs({x: x_temp, y: y_temp})
#
#         e = f_1 - f_0
#         print('e: ',e)
#         p = metropolis_expr.subs({t: T, E: e})
#         print('p', p)
#         r = random.random()
#         print('r', r)
#         print('temp point: ', x_temp, y_temp)
#         if e<0:
#             x_point = x_temp
#             y_point = y_temp
#         elif r<p:
#             x_point = x_temp
#             y_point = y_temp
#         print('selected point: ', x_point,y_point)
#         print()
#     T = T * c
#     print('T: ', T) # adaptive simulated annealing local meta heuristics 4.3