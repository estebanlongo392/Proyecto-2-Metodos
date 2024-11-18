//Problema_3 Proyecto_2 Métodos
import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x) y el punto x donde se calcularán las derivadas
def f(x):
    return np.sin(x)  # Puedes cambiar esta función por tu favorita

x = 1.0  # Cambiar este valor si deseas evaluar en otro punto

# Cálculo de las aproximaciones de f'_n(x)
n_values = np.arange(1, 21, dtype=float)  # Valores de n desde 1 hasta 20
h_values = 10.0 ** (-n_values)  # Valores de h = 10^(-n)
approximations = [(f(x + h) - f(x)) / h for h in h_values]

# Derivada exacta para comparar
exact_derivative = np.cos(x)  # Derivada exacta de sin(x) es cos(x)
errors = np.abs(approximations - exact_derivative)

# Mostrar la tabla de resultados
print("{:<5} {:<15} {:<25} {:<20}".format("n", "h (10^-n)", "Aproximación f'_n(x)", "Error absoluto"))
print("=" * 65)
for n, h, approx, error in zip(n_values, h_values, approximations, errors):
    print("{:<5} {:<15.8e} {:<25.8f} {:<20.8e}".format(int(n), h, approx, error))

# Graficar las aproximaciones y los errores
plt.figure(figsize=(12, 6))

# Aproximaciones
plt.subplot(1, 2, 1)
plt.plot(n_values, approximations, 'o-', label="Aproximaciones $f'_n(x)$")
plt.axhline(y=exact_derivative, color='r', linestyle='--', label="Derivada exacta")
plt.xlabel('n')
plt.ylabel("$f'_n(x)$")
plt.title("Aproximaciones de la derivada")
plt.legend()
plt.grid(True)

# Errores
plt.subplot(1, 2, 2)
plt.plot(n_values, errors, 's-', label="Error absoluto")
plt.xlabel('n')
plt.ylabel("Error absoluto")
plt.title("Error en las aproximaciones")
plt.yscale('log')  # Escala logarítmica para el error
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
