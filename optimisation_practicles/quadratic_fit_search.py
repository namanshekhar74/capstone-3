from sympy import symbols, Eq, solve, plot_implicit
from sympy.plotting import plot
import time
import sympy as sy
import sys


x = symbols('x')
expr = -(sy.sin(x)) + x ** 2
# expr = (x+3) ** 2
upper_range = 2
lower_range = -4
minima_list = [sys.maxsize-1, sys.maxsize]
iter = 1
tol = 0.00000001

st = time.time()

p1 = plot(expr, show=False)
def quadratic_fit_search(expr, upper_range, lower_range, iter):
    if tol >= minima_list[iter - 1] - minima_list[iter] > 0 or minima_list[iter - 1] == minima_list[iter]:
        print("number of iter: ", iter)

    else:
        mid = (upper_range + lower_range) / 2
        q0 = expr.subs(x, upper_range)
        q1 = expr.subs(x, lower_range)
        q2 = expr.subs(x, mid)

        y = symbols('y')
        c0 = symbols('c0')
        c1 = symbols('c1')
        c2 = symbols('c2')

        expr0 = (c0 + c1 * y + c2 * y ** 2).subs(y, upper_range)
        expr1 = (c0 + c1 * y + c2 * y ** 2).subs(y, lower_range)
        expr2 = (c0 + c1 * y + c2 * y ** 2).subs(y, mid)

        sol = solve([Eq(expr0, q0),
                     Eq(expr1, q1),
                     Eq(expr2, q2)

                     ])

        xq = -sol.get(c1) / (2 * sol.get(c2))
        minima_list.append(xq)
        xq_sol = expr.subs(x, xq)

        expr_final = c0 + c1 * y + c2 * y ** 2
        expr_final = expr_final.subs(c0,sol.get(c0) )
        expr_final = expr_final.subs(c1, sol.get(c1))
        expr_final = expr_final.subs(c2, sol.get(c2))
        p2 = plot(expr_final, show=False)
        p1.append(p2[0])

        if xq < mid:
            if xq_sol < q2:
                iter += 1
                print(lower_range, upper_range)
                quadratic_fit_search(expr, mid, lower_range, iter)

            else:
                iter += 1
                print(lower_range, upper_range)
                quadratic_fit_search(expr, upper_range, xq, iter)
        else:
            if xq_sol < q2:
                iter += 1
                print(lower_range, upper_range)
                quadratic_fit_search(expr, upper_range, mid, iter)

            else:
                iter += 1
                print(lower_range, upper_range)
                quadratic_fit_search(expr, lower_range, xq, iter)



final_answer = quadratic_fit_search(expr, upper_range, lower_range, iter)

print("final_answer:", expr.subs(x, minima_list[-1]))

print(minima_list[2:])
et =   time.time()
print("time: ", et-st)




p1.show()