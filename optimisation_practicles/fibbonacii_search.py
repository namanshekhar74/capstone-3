import time
from sympy import symbols
import sympy as sy
import math

st = time.perf_counter()

x = symbols('x')

# expr = sy.exp(x)-sy.sin(x)
# expr = -(sy.sin(x)) + x ** 2
expr = ((x**4)+1)/((x**2)+1)

iter = 0

tol = 0.1
b = 3
a = 0
fn = (b - a) / tol
fn = math.ceil(fn)




def fibonacci_nums(fn):
    sequence = [0, 1]
    while sequence[-1] <= fn:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)
    return sequence


fib_list = fibonacci_nums(fn)

itr = len(fib_list)
print("no. of iterations: ", itr)

def fibbonacii_search(expr, upper_range, lower_range, x1, x2, iter, itr):
    a = fib_list[itr-2] / fib_list[itr-1]

    if (x1 == 0):
        x1 = upper_range - (a * (upper_range - lower_range))

    if (x2 == 0):
        x2 = lower_range + (a * (upper_range - lower_range))


    x1_val = expr.subs(x, x1)
    x2_val = expr.subs(x, x2)

    if itr == 2:
        print("x: ", (upper_range + lower_range) / 2)
        print("y: ", expr.subs(x, (upper_range + lower_range) / 2))
        return upper_range, lower_range

    else:
        if x1_val < x2_val:
            itr -= 1
            print(lower_range, upper_range)
            fibbonacii_search(expr, x2, lower_range, 0, x1, iter, itr)


        else:
            itr -= 1
            print(lower_range, upper_range)
            fibbonacii_search(expr, upper_range, x1, x2, 0, iter, itr)


final_answer = fibbonacii_search(expr, 3, 0, 0, 0, iter, itr)
et = time.perf_counter()
print("time: ", et - st)
