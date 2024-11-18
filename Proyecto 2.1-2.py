import numpy as np

# Ejercicio 1

def five_point_derivative_step_by_step(f, x0, h):
    """
    Aproxima la derivada f'(x0) usando la fórmula de cinco puntos,
    mostrando el cálculo iterativo paso a paso.

    Parámetros:
    - f: función a derivar.
    - x0: punto donde se evalúa la derivada.
    - h: paso.

    Retorna:
    - Aproximación de la derivada f'(x0).
    """
    
    print("Ejercicio 1\n")
    
    # Valores individuales en cada punto
    term1 = -1 / (4 * h) * f(x0 - h)
    print(f"Paso 1: Termino (-1/4h)f(x0 - h) = {term1:.10f}")
    
    term2 = -5 / (6 * h) * f(x0)
    print(f"Paso 2: Termino (-5/6h)f(x0) = {term2:.10f}")
    
    term3 = 3 / (2 * h) * f(x0 + h)
    print(f"Paso 3: Termino (3/2h)f(x0 + h) = {term3:.10f}")
    
    term4 = -1 / (2 * h) * f(x0 + 2 * h)
    print(f"Paso 4: Termino (-1/2h)f(x0 + 2h) = {term4:.10f}")
    
    term5 = 1 / (12 * h) * f(x0 + 3 * h)
    print(f"Paso 5: Termino (1/12h)f(x0 + 3h) = {term5:.10f}")
    
    # Suma total
    result = term1 + term2 + term3 + term4 + term5
    print(f"Suma total: f'(x0) ≈ {result:.10f}")
    
    return result

# Función de prueba y su derivada exacta
f = np.sin  # Función f(x) = sin(x)
df_exacto = np.cos  # Derivada exacta f'(x) = cos(x)

# Parámetros
x0 = np.pi / 4  # Punto donde queremos evaluar (45 grados)
h = 0.01  # Paso pequeño

# Calcular derivada aproximada
aproximacion = five_point_derivative_step_by_step(f, x0, h)

# Derivada exacta
derivada_exacta = df_exacto(x0)
print(f"Derivada exacta: f'(x0) = {derivada_exacta:.10f}")


# Ejercicio 2

def five_point_derivative_given_values(x_values, f_values, x0):
    """
    Aproxima la derivada f'(x0) usando la fórmula de cinco puntos
    con datos tabulados para casos simétricos.

    Parámetros:
    - x_values: lista con los valores de x.
    - f_values: lista con los valores de f(x).
    - x0: punto donde se evalúa la derivada.

    Retorna:
    - Aproximación de la derivada f'(x0).
    """
    # Tamaño del paso (asumiendo paso uniforme)
    h = x_values[1] - x_values[0]

    # Índice de x0 en la tabla
    idx = x_values.index(x0)

    # Fórmula de cinco puntos (simétrica)
    term1 = -1 / (4 * h) * f_values[idx - 1]  # f(x0 - h)
    term2 = -5 / (6 * h) * f_values[idx]      # f(x0)
    term3 = 3 / (2 * h) * f_values[idx + 1]   # f(x0 + h)
    term4 = -1 / (2 * h) * f_values[idx + 2]  # f(x0 + 2h)
    term5 = 1 / (12 * h) * f_values[idx + 3]  # f(x0 + 3h)

    # Suma total
    result = term1 + term2 + term3 + term4 + term5
    return result


def five_point_derivative_asymmetric_backward(x_values, f_values, x0):
    """
    Aproxima la derivada f'(x0) usando una fórmula de cinco puntos asimétrica hacia atrás,
    adecuada para puntos cercanos al final de los datos.

    Parámetros:
    - x_values: lista con los valores de x.
    - f_values: lista con los valores de f(x).
    - x0: punto donde se evalúa la derivada.

    Retorna:
    - Aproximación de la derivada f'(x0).
    """
    # Tamaño del paso (asumiendo paso uniforme)
    h = x_values[1] - x_values[0]

    # Índice de x0 en la tabla
    idx = x_values.index(x0)

    # Fórmula de cinco puntos asimétrica hacia atrás
    term1 = -25 / (12 * h) * f_values[idx]         # f(x0)
    term2 = 48 / (12 * h) * f_values[idx - 1]      # f(x0 - h)
    term3 = -36 / (12 * h) * f_values[idx - 2]     # f(x0 - 2h)
    term4 = 16 / (12 * h) * f_values[idx - 3]      # f(x0 - 3h)
    term5 = -3 / (12 * h) * f_values[idx - 4]      # f(x0 - 4h)

    # Suma total
    result = term1 + term2 + term3 + term4 + term5
    return result


# Datos del problema
x_values = [0.2, 0.4, 0.6, 0.8, 1.0]
f_values = [0.9798652, 0.9177710, 0.8080348, 0.6386093, 0.3843735]

print("\nEjercicio 2\n")

# Aproximar la derivada en 0.4 usando la fórmula simétrica
f_prime_0_4 = five_point_derivative_given_values(x_values, f_values, 0.4)
print(f"f'(0.4) ≈ {f_prime_0_4:.10f}")

# Aproximar la derivada en 0.8 usando la fórmula asimétrica hacia atrás
f_prime_0_8 = five_point_derivative_asymmetric_backward(x_values, f_values, 0.8)
print(f"f'(0.8) ≈ {f_prime_0_8:.10f}")
