import sympy as sp

# Definiendo la varible simbolica
x = sp.symbols('x')

# Defininiendo la funcion para el item (a)
f1 = sp.exp(2*x)
f1_deriv = sp.diff(f1, x, 2) + sp.diff(f1, x)

# Definiendo la funcion para el item (b)
f2 = sp.sin(x)
f2_deriv = 3*sp.diff(f2, x, 2) + 2*sp.diff(f2, x) + 2*f2

# Mostrando los resultados
print("(D^2 + D)e^(2x) =", f1_deriv)
print("(3D^2 + 2D + 2)sin(x) =", f2_deriv)

# Imprimiendo algunos resultados numericos
print(f1_deriv.subs(x, 0))
print(f2_deriv.subs(x, 0))