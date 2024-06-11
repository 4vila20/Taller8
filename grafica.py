import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('recursos.csv')

# Convertir la columna 'Hora' a formato de tiempo
df['Hora'] = pd.to_datetime(df['Hora'])

# Calcular el porcentaje de uso de CPU
df['%CPU'] = 100 - (df['Memoria libre (kB)'] / df['Memoria total (kB)'] * 100)

# Graficar el consumo de memoria
plt.figure(figsize=(10, 6))
plt.plot(df['Hora'], df['Memoria usada (kB)'], label='Memoria usada (kB)', color='blue')
plt.plot(df['Hora'], df['Caché (kB)'], label='Caché (kB)', color='green')
plt.xlabel('Hora')
plt.ylabel('Consumo de memoria (kB)')
plt.title('Consumo de memoria')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graficar el uso de CPU
plt.figure(figsize=(10, 6))
plt.plot(df['Hora'], df['%CPU'], label='%CPU', color='red')
plt.xlabel('Hora')
plt.ylabel('Porcentaje de uso de CPU')
plt.title('Uso de CPU')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
