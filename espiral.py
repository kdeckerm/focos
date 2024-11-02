import numpy as np
import matplotlib.pyplot as plt

# Configuración de las constantes a y b
a = 0
b = 1

# Generar valores de theta (ángulo)
theta = np.linspace(0, 10 * np.pi, 1000)

# Calcular las espirales
r1 = a + b * theta  # Primera espiral
r2 = -(a + b * theta)  # Segunda espiral para la doble representación

# Convertir a coordenadas cartesianas
x1 = r1 * np.cos(theta)
y1 = r1 * np.sin(theta)

x2 = r2 * np.cos(theta)
y2 = r2 * np.sin(theta)

# Graficar las espirales
plt.figure(figsize=(10, 10))
plt.plot(x1, y1, label='Espiral de Arquímedes positiva', color='blue')
plt.plot(x2, y2, label='Espiral de Arquímedes negativa', color='red')
plt.title('Doble representación de las Espirales de Arquímedes')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axhline(0, color='red', linewidth=0.5)
plt.axvline(0, color='red', linewidth=0.5)
plt.grid(True)
plt.legend()

# Guardar la figura
plt.savefig("/home/decker/Documentos/Carpeta.py/espirales_arquimedes.png")

