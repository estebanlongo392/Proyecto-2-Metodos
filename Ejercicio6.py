import numpy as np
import pandas as pd

# Datos
x = np.array([1, 2, 3, 4, 5])               # Valores de x
f_x = np.array([2.71828, 7.3896, 20.08554, 54.59815, 148.41316])  # Valores de f(x)
h = x[1] - x[0]  # Paso (asumimos que es uniforme)

# Función exacta
def exact_f_prime(x_val):
    return np.exp(x_val)

def exact_f_double_prime(x_val):
    return np.exp(x_val)

# --- Inciso 6.1: Aproximación de f'(x) usando O(h) ---
print("6.1 Aproximación de f'(x) usando O(h):")
print("Procedimiento:")
print(f"Paso h = {h}")
f_prime_2 = (f_x[2] - f_x[1]) / h
print(f"Para f'(2): (f(3) - f(2)) / h = ({f_x[2]} - {f_x[1]}) / {h} = {f_prime_2}")

f_prime_3 = (f_x[3] - f_x[1]) / (2 * h)
print(f"Para f'(3): (f(4) - f(2)) / (2 * h) = ({f_x[3]} - {f_x[1]}) / (2 * {h}) = {f_prime_3}")

f_prime_4 = (f_x[4] - f_x[3]) / h
print(f"Para f'(4): (f(5) - f(4)) / h = ({f_x[4]} - {f_x[3]}) / {h} = {f_prime_4}")
print()

# --- Inciso 6.2: Aproximación de f''(x) usando O(h^2) ---
print("6.2 Aproximación de f''(x) usando O(h^2):")
print("Procedimiento:")
f_double_prime_2 = (f_x[2] - 2 * f_x[1] + f_x[0]) / (h ** 2)
print(f"Para f''(2): (f(3) - 2*f(2) + f(1)) / h^2 = ({f_x[2]} - 2*{f_x[1]} + {f_x[0]}) / {h**2} = {f_double_prime_2}")

f_double_prime_3 = (f_x[4] - 2 * f_x[3] + f_x[2]) / (h ** 2)
print(f"Para f''(3): (f(5) - 2*f(4) + f(3)) / h^2 = ({f_x[4]} - 2*{f_x[3]} + {f_x[2]}) / {h**2} = {f_double_prime_3}")

f_double_prime_4 = (f_x[4] - 2 * f_x[3] + f_x[2]) / (h ** 2)
print(f"Para f''(4): (f(5) - 2*f(4) + f(3)) / h^2 = ({f_x[4]} - 2*{f_x[3]} + {f_x[2]}) / {h**2} = {f_double_prime_4}")
print()

# --- Inciso 6.3: Errores ---
print("6.3 Errores de aproximación:")
print("Procedimiento:")
exact_f_prime_vals = [exact_f_prime(2), exact_f_prime(3), exact_f_prime(4)]
exact_f_double_prime_vals = [exact_f_double_prime(2), exact_f_double_prime(3), exact_f_double_prime(4)]

error_f_prime_2 = abs(f_prime_2 - exact_f_prime_vals[0])
print(f"Error en f'(2): |{f_prime_2} - {exact_f_prime_vals[0]}| = {error_f_prime_2}")

error_f_prime_3 = abs(f_prime_3 - exact_f_prime_vals[1])
print(f"Error en f'(3): |{f_prime_3} - {exact_f_prime_vals[1]}| = {error_f_prime_3}")

error_f_prime_4 = abs(f_prime_4 - exact_f_prime_vals[2])
print(f"Error en f'(4): |{f_prime_4} - {exact_f_prime_vals[2]}| = {error_f_prime_4}")

error_f_double_prime_2 = abs(f_double_prime_2 - exact_f_double_prime_vals[0])
print(f"Error en f''(2): |{f_double_prime_2} - {exact_f_double_prime_vals[0]}| = {error_f_double_prime_2}")

error_f_double_prime_3 = abs(f_double_prime_3 - exact_f_double_prime_vals[1])
print(f"Error en f''(3): |{f_double_prime_3} - {exact_f_double_prime_vals[1]}| = {error_f_double_prime_3}")

error_f_double_prime_4 = abs(f_double_prime_4 - exact_f_double_prime_vals[2])
print(f"Error en f''(4): |{f_double_prime_4} - {exact_f_double_prime_vals[2]}| = {error_f_double_prime_4}")
print()

# --- Resumen en tabla ---
results = pd.DataFrame({
    "x": [2, 3, 4],
    "f'(x) (Aproximado)": [f_prime_2, f_prime_3, f_prime_4],
    "f'(x) (Exacto)": exact_f_prime_vals,
    "Error f'(x)": [error_f_prime_2, error_f_prime_3, error_f_prime_4],
    "f''(x) (Aproximado)": [f_double_prime_2, f_double_prime_3, f_double_prime_4],
    "f''(x) (Exacto)": exact_f_double_prime_vals,
    "Error f''(x)": [error_f_double_prime_2, error_f_double_prime_3, error_f_double_prime_4]
})

print("Resumen en tabla:")
print(results)
