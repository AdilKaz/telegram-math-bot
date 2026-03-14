from sympy import symbols, solve, diff, integrate, latex
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

# Symbol
x = symbols('x')

# SymPy parser with implicit multiplication
transformations = standard_transformations + (implicit_multiplication_application,)

def parse_math(expr: str):
    """Parse user input like '2x^2 + 3x' into SymPy expression."""
    expr = expr.replace("^", "**")
    return parse_expr(expr, transformations=transformations)

def solve_expression(expr: str):
    e = parse_math(expr)
    return e.evalf()

def solve_equation(expr: str):
    if "=" in expr:
        left, right = expr.split("=")
        e = parse_math(left) - parse_math(right)
    else:
        e = parse_math(expr)
    return solve(e, x)

def derivative(expr: str):
    e = parse_math(expr)
    return diff(e, x)

def integral(expr: str):
    e = parse_math(expr)
    return integrate(e, x)