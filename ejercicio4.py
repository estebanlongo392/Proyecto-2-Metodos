//Problema_4 Proyecto_2 Métodos
import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la función f(x) = sin(x)
f = sp.sin(x)

# Calcular las derivadas necesarias para la expansión de Taylor
f_prime = sp.diff(f, x, 1)
f_double_prime = sp.diff(f, x, 2)
f_triple_prime = sp.diff(f, x, 3)
f_fourth_prime = sp.diff(f, x, 4)

# Expansión de Taylor de la función f(x) alrededor de x0
x0 = sp.symbols('x0')
expansion_taylor = f.subs(x, x0) + f_prime.subs(x, x0)*(x - x0) + (f_double_prime.subs(x, x0) / 2)*(x - x0)**2 \
                   + (f_triple_prime.subs(x, x0) / 6)*(x - x0)**3 + (f_fourth_prime.subs(x, x0) / 24)*(x - x0)**4

# Aproximación de la tercera derivada usando el polinomio de Taylor
tercera_derivada_approx = (expansion_taylor.diff(x, 3)).subs(x, x0)

# Mostrar la tercera derivada aproximada
print(f"La tercera derivada aproximada usando expansión de Taylor es: {tercera_derivada_approx}")

# Evaluar la tercera derivada en puntos específicos
evaluacion_1 = tercera_derivada_approx.subs(x0, 1.0)
evaluacion_1_5 = tercera_derivada_approx.subs(x0, 1.5)
evaluacion_2 = tercera_derivada_approx.subs(x0, 2.0)

print(f"Evaluación en x0 = 1.0: {evaluacion_1}")
print(f"Evaluación en x0 = 1.5: {evaluacion_1_5}")
print(f"Evaluación en x0 = 2.0: {evaluacion_2}")

