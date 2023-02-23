from sympy import symbols, diff, solve, Eq, N, re
from sympy.core.evalf import evalf

x_init = 1
y_init = 1.5
x, y = symbols('x y')
expr = 100*(y-x**2)**2 + (1-x)**2

# expr = (x ** 2 - 10) ** 2 + (y - 5) ** 2
# expr = x**2+y**2+x+y+1
iter = 15


def gradient_des(expr, x_init, y_init, iter):
    delta1 = diff(expr, x)
    delta2 = diff(expr, y)

    delta1 = delta1.subs({x: x_init, y: y_init})
    delta2 = delta2.subs({x: x_init, y: y_init})
    a = symbols('a')

    x_subs = x_init - a * delta1
    y_subs = y_init - a * delta2

    expr_a = expr.subs({x: x_subs, y: y_subs})
    min_a = diff(expr_a, a)

    min_a = solve(Eq(min_a, 0))
    minimum_a = []
    for i in min_a:
        minimum_a.append(re(i.evalf()))

    if minimum_a:
        minimum_a = min(minimum_a)
        x_subs = x_subs.subs(a, minimum_a)
        y_subs = y_subs.subs(a, minimum_a)
        print(x_subs, y_subs)
    else:
        return

    if iter:
        iter -= 1
        gradient_des(expr, x_subs, y_subs, iter)

    return x_subs, y_subs


gradient_des(expr, x_init, y_init, iter)
