from sympy import sympify, solve, symbols, diff, integrate

x = symbols('x')

def solve_expression(expr: str):
    expr = expr.replace("^", "**")
    return sympify(expr).evalf()

def solve_equation(expr: str):
    expr = expr.replace("^", "**")

    if "=" in expr:
        left, right = expr.split("=")
        expr = sympify(left) - sympify(right)
    else:
        expr = sympify(expr)

    return solve(expr, x)

def derivative(expr: str):
    expr = expr.replace("^", "**")
    return diff(sympify(expr), x)

def integral(expr: str):
    expr = expr.replace("^", "**")
    return integrate(sympify(expr), x)