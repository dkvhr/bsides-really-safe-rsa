from sympy.solvers import solve
from sympy import Symbol
import sys

sys.set_int_max_str_digits(0)

# Lendo o valor de n
n_value = open("n_value.py", "r")
n = int(n_value.read()[4:])

# Resolvendo a equação
x = Symbol('x')
x_roots = solve(2*x**2 + x - n, x)
e = 65537

# Escolhendo a raiz positiva:
p = int(x_roots[1])

# Calculos finais
q = 2*p + 1
phi = (p-1) * (q-1)
d = pow(e, -1, phi)
print(str(d)[-15:])
