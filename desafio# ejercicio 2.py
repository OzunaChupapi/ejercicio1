import math

# Definimos la función original f(x)
def f(x):
    return math.log(x)

# Definimos las derivadas de la función f(x) = ln(x)
def f_prime(x):
    return 1/x

def f_double_prime(x):
    return -1/(x**2)

def f_triple_prime(x):
    return 2/(x**3)

def f_quadruple_prime(x):
    return -6/(x**4)

# Expansión de Taylor hasta cuarto orden alrededor de x = 1
def taylor_series_approx_ln(x_base, x_value, order):
    approximation = f(x_base)
    if order >= 1:
        approximation += f_prime(x_base) * (x_value - x_base)
    if order >= 2:
        approximation += (f_double_prime(x_base) * (x_value - x_base)**2) / math.factorial(2)
    if order >= 3:
        approximation += (f_triple_prime(x_base) * (x_value - x_base)**3) / math.factorial(3)
    if order >= 4:
        approximation += (f_quadruple_prime(x_base) * (x_value - x_base)**4) / math.factorial(4)
    return approximation

# Cálculo del error relativo porcentual verdadero
def true_relative_error(true_value, approx_value):
    return abs((true_value - approx_value) / true_value) * 100

# Parámetros
x_base = 1    # Punto base
x_value = 2.5 # Valor donde queremos aproximar
true_value = f(x_value)  # Valor verdadero de ln(2.5)

# Calcular aproximaciones y errores
for order in range(5):
    approx_value = taylor_series_approx_ln(x_base, x_value, order)
    error = true_relative_error(true_value, approx_value)
    print(f"Aproximación de orden {order}: {approx_value}")
    print(f"Error relativo porcentual: {error:.5f}%\n")