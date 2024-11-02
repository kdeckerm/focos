import matplotlib.pyplot as plt
import numpy as np

# Datos del problema
diameter = 14  # diámetro de la antena en metros
depth = 2.7  # profundidad de la antena en metros

# Calcular el parámetro a
a = depth / (diameter / 2) ** 2

# Calcular la distancia focal f
focal_distance = 1 / (4 * a)

# Crear la parábola
x = np.linspace(-diameter / 2, diameter / 2, 400)
y = a * x**2

# Graficar la parábola y la posición del foco
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Parábola de la antena")
plt.scatter(0, focal_distance, color="red", label=f"Foco a {focal_distance:.2f} m", zorder=5)
plt.axhline(0, color="black", linewidth=0.5)  # Eje x
plt.axvline(0, color="black", linewidth=0.5)  # Eje y

# Trazar los puntos de diámetro y profundidad
plt.scatter([diameter / 2, -diameter / 2], [depth, depth], color="blue", label=f"Diametro de la antena ({diameter}m")

# Punto para marcar la profundidad en la parábola con su etiqueta
plt.scatter([0], [depth], color="purple", label=f"Profundidad máxima ({depth} m)", zorder=5)

# Ejes en color rojo
plt.axhline(0, color="red", linewidth=0.5)  # Eje x en rojo
plt.axvline(0, color="red", linewidth=0.5)  # Eje y en rojo

# Etiquetas y título
plt.title("Sección cónica de la antena parabólica con posición del foco")
plt.xlabel("Ancho de la antena (m)")
plt.ylabel("Profundidad (m)")
plt.legend()
plt.grid(True)

# Guardar la gráfica como archivo
plt.savefig("/home/decker/Documentos/Carpeta.py/antena_parabolica.png")

# Imprimir la distancia focal
print(f"La distancia focal es de aproximadamente {focal_distance:.2f} metros.")
