import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datos del problema
t = np.array([0, 25, 50, 75, 100, 125])  # Tiempo en segundos
y = np.array([0, 32, 58, 78, 92, 100])   # Distancia en kilómetros

# Diferenciación numérica para la velocidad
def calculate_velocity(t, y):
    velocities = np.zeros_like(y, dtype=float)
    print("** Cálculo de Velocidades **")
    for i in range(len(t)):
        if i == 0:  # Diferencias hacia adelante
            velocities[i] = (y[i + 1] - y[i]) / (t[i + 1] - t[i])
            print(f"Velocidad en t={t[i]}s (diferencias hacia adelante): {velocities[i]:.4f} km/s")
        elif i == len(t) - 1:  # Diferencias hacia atrás
            velocities[i] = (y[i] - y[i - 1]) / (t[i] - t[i - 1])
            print(f"Velocidad en t={t[i]}s (diferencias hacia atrás): {velocities[i]:.4f} km/s")
        else:  # Diferencias centradas
            velocities[i] = (y[i + 1] - y[i - 1]) / (t[i + 1] - t[i - 1])
            print(f"Velocidad en t={t[i]}s (diferencias centradas): {velocities[i]:.4f} km/s")
    return velocities

# Diferenciación numérica para la aceleración
def calculate_acceleration(t, velocities):
    accelerations = np.zeros_like(velocities, dtype=float)
    print("\n** Cálculo de Aceleraciones **")
    for i in range(len(t)):
        if i == 0:  # Diferencias hacia adelante
            accelerations[i] = (velocities[i + 1] - velocities[i]) / (t[i + 1] - t[i])
            print(f"Aceleración en t={t[i]}s (diferencias hacia adelante): {accelerations[i]:.4f} km/s²")
        elif i == len(t) - 1:  # Diferencias hacia atrás
            accelerations[i] = (velocities[i] - velocities[i - 1]) / (t[i] - t[i - 1])
            print(f"Aceleración en t={t[i]}s (diferencias hacia atrás): {accelerations[i]:.4f} km/s²")
        else:  # Diferencias centradas
            accelerations[i] = (velocities[i + 1] - velocities[i - 1]) / (t[i + 1] - t[i - 1])
            print(f"Aceleración en t={t[i]}s (diferencias centradas): {accelerations[i]:.4f} km/s²")
    return accelerations

# Procedimiento detallado
print("** Procedimiento Detallado **")
print("\n1. Se calculan las velocidades utilizando diferenciación numérica.")
velocities = calculate_velocity(t, y)

print("\n2. Se calculan las aceleraciones utilizando diferenciación numérica sobre las velocidades.")
accelerations = calculate_acceleration(t, velocities)

# Resultados
results = pd.DataFrame({
    "Tiempo (s)": t,
    "Distancia (km)": y,
    "Velocidad (km/s)": velocities,
    "Aceleración (km/s²)": accelerations
})

print("\n** Resultados Finales **")
print(results)

# Graficar posición, velocidad y aceleración
plt.figure(figsize=(12, 8))

# Gráfico de posición
plt.subplot(3, 1, 1)
plt.plot(t, y, marker='o', color='b', label="Posición")
plt.title("Posición vs. Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (km)")
plt.grid()
plt.legend()

# Gráfico de velocidad
plt.subplot(3, 1, 2)
plt.plot(t, velocities, marker='o', color='g', label="Velocidad")
plt.title("Velocidad vs. Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (km/s)")
plt.grid()
plt.legend()

# Gráfico de aceleración
plt.subplot(3, 1, 3)
plt.plot(t, accelerations, marker='o', color='r', label="Aceleración")
plt.title("Aceleración vs. Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Aceleración (km/s²)")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
