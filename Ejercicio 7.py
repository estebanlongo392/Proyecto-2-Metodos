import numpy as np

# Definimos constantes globales
m = 100000  # población total
y_0 = 1000  # infectados iniciales
k = 2e-6  # constante de proporcionalidad
t_final = 30  # tiempo en días
h = 1  # tamaño de paso

# Inciso 7.1: Modelo de la ecuación diferencial ya resuelta
def model():
    print("7.1. Modelo de la ecuación diferencial:")
    print("La forma inicial de la ecuación diferencial es:")
    print("dy/dt = k * (m - y) * y")
    print("\nResolviendo la ecuación diferencial:")
    print("y(t) = m / (1 + ((m - y_0) / y_0) * exp(-m * k * t))")
    print("\nSustituyendo valores para obtener la solución particular:")
    C2 = y_0 / (m - y_0)  # constante de integración
    print(f"y(t) = {m} / (1 + ({C2:.5f}) * exp(-{m * k:.5f} * t))")
    print()

# Función derivada (modelo de la ecuación diferencial)
def f(t, y):
    return k * (m - y) * y

# Inciso 7.2: Métodos numéricos
def euler_method(y_0, t_final, h):
    t_values = np.arange(0, t_final + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y_0
    for i in range(1, len(t_values)):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])
    return y_values[-1]

def heun_method(y_0, t_final, h):
    t_values = np.arange(0, t_final + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y_0
    for i in range(1, len(t_values)):
        y_pred = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])  # predicción
        y_values[i] = y_values[i-1] + (h / 2) * (f(t_values[i-1], y_values[i-1]) + f(t_values[i], y_pred))
    return y_values[-1]

def runge_kutta_4th_order(y_0, t_final, h):
    t_values = np.arange(0, t_final + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y_0
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        y = y_values[i-1]
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        k3 = f(t + h / 2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)
        y_values[i] = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y_values[-1]

# Inciso 7.3: Solución exacta
def exact_solution(t, m, k, y_0):
    C2 = y_0 / (m - y_0)  # constante C2
    exponent = m * k * t
    return (m * C2 * np.exp(exponent)) / (1 + C2 * np.exp(exponent))

# Inciso 7.4: Límite cuando t -> ∞
def limit_solution(m):
    return m  # La solución se aproxima a m cuando t -> ∞

# Función principal para resolver cada inciso
def main():
    # Inciso 7.1: Modelo
    model()
    
    # Inciso 7.2: Métodos numéricos
    y_euler = euler_method(y_0, t_final, h)
    y_heun = heun_method(y_0, t_final, h)
    y_runge_kutta = runge_kutta_4th_order(y_0, t_final, h)
    print("7.2. Aproximaciones numéricas para y(30):")
    print(f"   Método de Euler: {y_euler:.2f} infectados")
    print(f"   Método de Heun: {y_heun:.2f} infectados")
    print(f"   Método de Runge-Kutta: {y_runge_kutta:.2f} infectados")

    # Inciso 7.3: Solución exacta y diferencias explícitas
    y_exact = 80295.72  # Dado por el problema
    print(f"\n7.3. Solución exacta para y(30): {y_exact:.2f}")
    print(f"Diferencias explícitas:")
    print(f" Método de Euler:       80295.72 - {y_euler:.2f} = {y_exact - y_euler:.2f}")
    print(f" Método de Heun:        80295.72 - {y_heun:.2f} = {y_exact - y_heun:.2f}")
    print(f" Método de Runge-Kutta: 80295.72 - {y_runge_kutta:.2f} = {y_exact - y_runge_kutta:.2f}")

    # Inciso 7.4: Límite cuando t -> ∞
    y_limit = limit_solution(m)
    print(f"\n7.4. Límite cuando t -> ∞: {y_limit}")

# Ejecutar la función principal
main()
