import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # Usaremos pandas para crear una tabla más clara

# Parámetros del problema
k1, k2, k3, k4 = 3, 0.002, 0.0006, 0.5  # Constantes de proporcionalidad
x1_0, x2_0 = 1000, 500  # Condiciones iniciales
h = 0.1  # Tamaño del paso (para cálculo interno)
t_max = 4  # Tiempo máximo

# INCISO 8.1: Definición del modelo de ecuaciones diferenciales
print("8.1 Modelo de ecuaciones diferenciales:")
print("Sistema que describe el cambio de las poblaciones de presas y depredadores:")
print("dx1/dt = k1 * x1(t) - k2 * x1(t) * x2(t)")
print("dx2/dt = k3 * x1(t) * x2(t) - k4 * x2(t)")
print(f"Con k1={k1}, k2={k2}, k3={k3}, k4={k4}\n")

# INCISO 8.2: Aproximación numérica usando el método de Euler
# Inicialización de las variables
print("8.2 Tabla de comportamiento")

print("Sistema que describe el cambio de las poblaciones de presas y depredadores:")
print(f"dx1/dt = {k1} * 1000(t) - {k2} * 1000(t) * 500(t)")
print(f"dx2/dt = {k3} * 1000(t) * 500(t) - {k4} * 500(t)\n")


t = np.arange(0, t_max + h, h)  # Vector de tiempos
x1 = np.zeros(len(t))  # Población de presas
x2 = np.zeros(len(t))  # Población de depredadores
x1[0], x2[0] = x1_0, x2_0  # Asignar condiciones iniciales

# Método de Euler para resolver el sistema
for i in range(len(t) - 1):
    # Calcular las derivadas en el tiempo actual
    x1_prime = k1 * x1[i] - k2 * x1[i] * x2[i]  # x1'(t)
    x2_prime = k3 * x1[i] * x2[i] - k4 * x2[i]  # x2'(t)

    # Actualizar las poblaciones usando el método de Euler
    x1[i+1] = x1[i] + h * x1_prime
    x2[i+1] = x2[i] + h * x2_prime

# Crear tabla para los tiempos con intervalos de 0.5
t_table = np.arange(0, t_max + 0.25, 0.25)
x1_table = np.interp(t_table, t, x1)  # Interpolar para obtener valores en t_table
x2_table = np.interp(t_table, t, x2)  # Interpolar para obtener valores en t_table

# Crear un DataFrame para mostrar la tabla (redondeando a 2 decimales)
tabla = pd.DataFrame({
    "Tiempo (t)": np.round(t_table, 2),
    "Población de presas (x1)": np.round(x1_table, 2),
    "Población de depredadores (x2)": np.round(x2_table, 2)
})

# Mostrar los resultados en consola
print("Tabla de valores de poblaciones (con intervalos de 0.25):")
print(tabla.to_string(index=False))


# INCISO 8.3: Gráfica de las soluciones
print("\n8.3 Gráfica de las soluciones:")
plt.plot(t, x1, label="Población de presas ($x_1(t)$)")
plt.plot(t, x2, label="Población de depredadores ($x_2(t)$)")
plt.xlabel("Tiempo (t)")
plt.ylabel("Población")
plt.title("Modelo presa-depredador (Método de Euler)")
plt.legend()
plt.grid(True)
plt.show()

# Explicación del fenómeno
print("\nFenómeno físico representado:")
print("El modelo describe la interacción entre una población de presas y depredadores.")
print("La población de presas crece proporcionalmente pero disminuye por depredación.")
print("La población de depredadores depende de la disponibilidad de presas.")
