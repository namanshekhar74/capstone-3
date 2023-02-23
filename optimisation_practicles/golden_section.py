import time
from math import sin
from sympy import symbols
import sympy as sy
import math

st = time.time()

x = symbols('x')

# expr = sy.exp(x)-sy.sin(x)
# expr = -(sy.sin(x)) + x ** 2
expr = ((x**4)+1)/((x**2)+1)
iter = 0

tol = 0.1
b = 3
a = 0
itr = (math.log(tol / (b - a)) / math.log(0.618))
itr = math.ceil(itr)

print("no. of iterations: ", itr)


def golden_section(expr, upper_range, lower_range, x1, x2, iter, itr, x1_val, x2_val):
    a = 0.618

    if (x1 == 0):
        x1 = upper_range - (a * (upper_range - lower_range))

    if (x2 == 0):
        x2 = lower_range + (a * (upper_range - lower_range))

    mid = (upper_range + lower_range) / 2

    if x1_val == 0:
        x1_val = expr.subs(x, x1)

    if (x2_val == 0):
        x2_val = expr.subs(x, x2)

    if itr == iter:
        print("x: ", (upper_range + lower_range) / 2)
        print("y: ", expr.subs(x, (upper_range + lower_range) / 2))
        return upper_range, lower_range

    else:
        if x1_val < x2_val:
            iter += 1
            print(lower_range, upper_range)
            golden_section(expr, x2, lower_range, 0, x1, iter, itr, 0, x1_val)


        else:
            iter += 1
            print(lower_range, upper_range)
            golden_section(expr, upper_range, x1, x2, 0, iter, itr, x2_val, 0)


final_answer = golden_section(expr, 3, 0, 0, 0, iter, itr, 0, 0)
et = time.time()
print("time: ", et - st)
