import sympy as sy

a, b = sy.symbols('a b')
x = sy.symbols('x')
y = sy.symbols('y')
I = sy.Integral(sy.sin(x)+x,(x,a,b))
print(sy.pretty(I))
