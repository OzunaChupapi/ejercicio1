import math

# Definir la función original
def f(x):
    return 25 * x**3 - 6 * x**2 + 7 * x - 88

# Derivada de primer orden
def f_prime(x):
    return 75 * x**2 - 12 * x + 7

# Derivada de segundo orden
def f_double_prime(x):
    return 150 * x - 12

# Derivada de tercer orden
def f_triple_prime(x):
    return 150

# Punto base x = 1
x_base = 1

# Valor donde queremos predecir f(3)
x_predict = 3

# Evaluar las derivadas en x = 1
f_base = f(x_base)
f_prime_base = f_prime(x_base)
f_double_prime_base = f_double_prime(x_base)
f_triple_prime_base = f_triple_prime(x_base)

# Expansión de Taylor hasta el tercer orden
taylor_approximation = (f_base +
                        f_prime_base * (x_predict - x_base) +
                        (f_double_prime_base / math.factorial(2)) * (x_predict - x_base)**2 +
                        (f_triple_prime_base / math.factorial(3)) * (x_predict - x_base)**3)

# Valor real de f(3)
f_real = f(x_predict)

# Calcular el error relativo porcentual
error_relativo_porcentual = abs((f_real - taylor_approximation) / f_real) * 100

# Mostrar los resultados
print(f"Valor de f(3) real: {f_real}")
print(f"Valor aproximado de f(3) con la serie de Taylor: {taylor_approximation}")
print(f"Error relativo porcentual: {error_relativo_porcentual:.6f}%")
