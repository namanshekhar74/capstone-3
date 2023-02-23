import time
from sympy import symbols
import sympy as sy
import math

st = time.time()
x = symbols('x')

#expr = sy.exp(x)-sy.sin(x)
expr = -(sy.sin(x))+x**2

iter = 0

tol = 0.0000000001
b = 1
a = 0
itr =(math.log(tol/(b-a))/math.log(0.5))
itr = math.ceil(itr)

print("no. of iterations: ", itr)

def halfing_method(expr, upper_range, lower_range, iter,itr):
    mid = (upper_range + lower_range) / 2
    m1 = (mid + lower_range) / 2
    m2 = (upper_range + mid) / 2
    upper_val = expr.subs(x, upper_range)
    mid_val = expr.subs(x, mid)
    m1_val = expr.subs(x, m1)
    m2_val = expr.subs(x, m2)
    lower_val = expr.subs(x, lower_range)
    if iter == itr:
        print("x: ", (upper_range+lower_range)/2)
        print("y: ",expr.subs(x, (upper_range+lower_range)/2))
        return upper_range, lower_range
    else:
        if m1_val < mid_val:
            iter += 1
            print(lower_range, upper_range)
            halfing_method(expr, mid, lower_range, iter,itr)

        elif m2_val < mid_val:
            iter += 1
            print(lower_range, upper_range)
            halfing_method(expr, upper_range, mid, iter,itr)
        else:
            iter += 1
            print(lower_range, upper_range)
            halfing_method(expr, m2, m1, iter,itr)


final_answer = halfing_method(expr, 1, 0, 0,itr)
et =   time.time()
print("time: ", et-st)
arwgfwrf = input()