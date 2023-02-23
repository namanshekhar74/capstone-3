import time
from math import sin
import random

from sympy import symbols
import sympy as sy
import math

st = time.time()

x, y, E, t = symbols('x y E t')
# expr = sy.exp(x)-sy.sin(x)
# expr = -(sy.sin(x)) + x ** 2
# expr = ((x**4)+1)/((x**2)+1)
expr = 500 - 20*x - 26*y - 4*x*y + 4*x**2 + 3*y**2
expr = -(1+ sy.cos(12*sy.sqrt(x**2+y**2)))/(0.5*(x**2+y**2)+2)

a = expr.subs({x: 1500, y: 1500})

print(a)

print(expr.subs({x: 150, y: 150}))