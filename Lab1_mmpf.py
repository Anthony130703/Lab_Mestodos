import sympy as sp

# Definiendo la varible simbolica
x = sp.symbols('x')

# Defininiendo la funcion para el item (a)
f1 = sp.exp(2*x)
f1_deriv = sp.diff(f1, x, 2) + sp.diff(f1, x)

# Definiendo la funcion para el item (b)
f2 = sp.sin(x)
f2_deriv = 3*sp.diff(f2, x, 2) + 2*sp.diff(f2, x) + 2*f2

# Definiendo la funcion para el item (c)
f3 = 2*sp.exp(x) * sp.cos(x)
f3_deriv_parte1 = sp.diff(f3, x) - x*f3
resultado_final = sp.diff(f3_deriv_parte1, x) + f3_deriv_parte1

# Mostrando los resultados
print("(D^2 + D)e^(2x) =", f1_deriv)
print("(3D^2 + 2D + 2)sin(x) =", f2_deriv)
print("(D+1)(D-x)(2e^x + cos(x)) =", resultado_final)


# Imprimiendo algunos resultados numericos
print("\nresultados numericos con x = 0:")
print(f1_deriv.subs(x, 0))
print(f2_deriv.subs(x, 0))
print(resultado_final.subs(x, 0))