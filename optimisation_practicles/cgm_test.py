from numpy import gradient
from sympy import symbols, diff, solve, Eq, N, re, hessian
from sympy.core.evalf import evalf
from numdifftools import Gradient
import numpy as np

# x_init = 5
# y_init = 5
# point_init = [x_init, y_init]
# point_init = np.array(point_init)
# x, y = symbols('x y')


x = [-5,0]
y= [[1,1],[1,2]]
x = np.array(x)
y = np.array(y)
print(np.matmul(x,y))
