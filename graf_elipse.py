import numpy as np
import matplotlib.pyplot as plt
import math

#valores de focos totales
# el valor de este dato debe ser el valor anterior a la raiz cuadrada
at=49
bt=4

# Valores de los ejes mayor y menor
a = math.sqrt(at)  # Semi-eje mayor en cm 
b = math.sqrt(bt)  # Semi-eje menor en cm 

# Cálculo de c (distancia focal desde el centro)
c = np.sqrt(a**2 - b**2)
foci_distance = 2 * c  # Distancia total entre los focos

# Coordenadas del centroide Nota: ajuste los valores del centroide en el eje correspondiente
centroid_x = 3
centroid_y = -2

# Coordenadas de los focos con el centroide desplazado
foco1 = (centroid_x - c, centroid_y)
foco2 = (centroid_x + c, centroid_y)

# Configuración de la elipse desplazada
theta = np.linspace(0, 2 * np.pi, 100)
x_ellipse = centroid_x + a * np.cos(theta)
y_ellipse = centroid_y + b * np.sin(theta)

# Graficar la elipse desplazada
plt.figure(figsize=(8, 6))
plt.plot(x_ellipse, y_ellipse, label="Elipse")
plt.scatter(*foco1, color="red", label=f"Foco 1 ({foco1[0]:.2f}, {foco1[1]})")
plt.scatter(*foco2, color="blue", label=f"Foco 2 ({foco2[0]:.2f}, {foco2[1]})")
plt.scatter(centroid_x, centroid_y, color="green", marker="x", label=f"Centroide C({centroid_x}, {centroid_y})")

# Vértices en el eje mayor y menor
vertice1 = (centroid_x - a, centroid_y)
vertice2 = (centroid_x + a, centroid_y)
vertice3 = (centroid_x, centroid_y - b)
vertice4 = (centroid_x, centroid_y + b)

# Dibujar los vértices
plt.scatter(*vertice1, color="purple", label="Vértice 1 (Eje Mayor)")
plt.scatter(*vertice2, color="purple", label="Vértice 2 (Eje Mayor)")
plt.scatter(*vertice3, color="orange", label="Vértice 3 (Eje Mayor)")
plt.scatter(*vertice4, color="orange", label="Vértice 4 (Eje Menor)")

# Ejes y límites de la gráfica
plt.plot([centroid_x - a, centroid_x + a], [centroid_y, centroid_y], 'k--', label=f"Eje Mayor ({a+a} cm)")
plt.plot([centroid_x, centroid_x], [centroid_y - b, centroid_y + b], 'k--', label=f"Eje Menor ({b+b} cm)")
plt.xlim(-10, 10) # ajustar escala de eje (x)
plt.ylim(-10, 10) # ajustar escala de eje (y)
plt.xlabel("X (cm)")
plt.ylabel("Y (cm)")
plt.title("Representación de la Elipse con Focos, Vértices y Ejes")
plt.axhline(y=0, color='red', linestyle='-', linewidth=1)
plt.axvline(x=0, color='red', linestyle='-', linewidth=1)
plt.legend(loc="upper right")
plt.grid(True)

# Agregar texto con la distancia entre los focos "Nota: ajustar valores de inpresion de texto en la imagen"
plt.text(-7.5, 2, f"Distancia entre focos: {foci_distance:.2f} cm", fontsize=10, color="purple")

# Guardar la gráfica como archivo en lugar de mostrarla
plt.savefig(f"/home/decker/Documentos/Carpeta.py/elipse_{centroid_x}_{centroid_y}.png")

# Si estás en un entorno interactivo, puedes descomentarlo para mostrarla:
# plt.show()




