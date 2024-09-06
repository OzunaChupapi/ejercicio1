import numpy as np
import pandas as pd
import os

# Definir las variables conocidas
B = 20  # Ancho del canal en metros
H = 0.3  # Profundidad del canal en metros
n = 0.03  # Coeficiente de rugosidad
S = 0.0003  # Pendiente

# Definir los rangos de incertidumbre para n y S
n_range = (0.027, 0.033)
S_range = (0.00027, 0.00033)

# Incrementos para diferencias finitas
delta_n = 0.001  # Incremento pequeño para n
delta_S = 0.00001  # Incremento pequeño para S

# Definir la fórmula de Manning para el flujo en un canal rectangular
def manning_flow(B, H, n, S):
    return (1 / n) * ((B * H)**(5/3)) / ((B + 2 * H)**(2/3)) * np.sqrt(S)

# Calcular el flujo nominal
Q_nominal = manning_flow(B, H, n, S)

# Análisis de sensibilidad de primer orden (diferencias finitas)
# Sensibilidad con respecto a n (coeficiente de rugosidad)
Q_n_plus = manning_flow(B, H, n + delta_n, S)  # Flujo con n + delta_n
Q_n_minus = manning_flow(B, H, n - delta_n, S)  # Flujo con n - delta_n
dQ_dn = (Q_n_plus - Q_n_minus) / (2 * delta_n)  # Derivada numérica central
uncertainty_n = (n_range[1] - n_range[0]) / 2  # Incertidumbre en n
sensitivity_n = abs(dQ_dn * uncertainty_n)

# Sensibilidad con respecto a S (pendiente)
Q_S_plus = manning_flow(B, H, n, S + delta_S)  # Flujo con S + delta_S
Q_S_minus = manning_flow(B, H, n, S - delta_S)  # Flujo con S - delta_S
dQ_dS = (Q_S_plus - Q_S_minus) / (2 * delta_S)  # Derivada numérica central
uncertainty_S = (S_range[1] - S_range[0]) / 2  # Incertidumbre en S
sensitivity_S = abs(dQ_dS * uncertainty_S)

# Crear un DataFrame para los resultados
data = {
    'Variable': ['n (rugosidad)', 'S (pendiente)'],
    'Flujo Nominal (Q) [m^3/s]': [Q_nominal, Q_nominal],
    'Derivada Numérica (dQ/dVariable)': [dQ_dn, dQ_dS],
    'Incertidumbre': [uncertainty_n, uncertainty_S],
    'Sensibilidad (dQ/dVariable * Incertidumbre) [m^3/s]': [sensitivity_n, sensitivity_S]
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
file_name = 'Sensibilidad_Manning.xlsx'
file_path = os.path.join(os.getcwd(), file_name)  # Ruta en el directorio actual

try:
    df.to_excel(file_path, index=False)
    print(f"Archivo de resultados guardado en: {file_path}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")

# Mostrar los resultados en consola
print(df)