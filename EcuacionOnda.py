import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros
L = 20.0   	# Longitud del dominio
T = 40.0   	# Tiempo total de simulación
nx = 100  	# Número de puntos en el espacio
nt = 200 	# Número de pasos en el tiempo
c = 1.0   	# Velocidad de la onda

# Discretización
dx = L / (nx - 1)
dt = T / (nt - 1)
r = c * dt / dx

# Condición inicial
x = np.linspace(0, L, nx)
u0 = np.sin(np.pi * x / L)

# Inicializar las matrices de solución
u = np.zeros((nx, nt))
u[:, 0] = u0
u[:, 1] = u0  

# Iteración temporal
for j in range(1, nt-1):
	for i in range(1, nx-1):
    	u[i, j+1] = 2*(1 - r**2)*u[i, j] + r**2*(u[i+1, j] + u[i-1, j]) - u[i, j-1]

# Crear figura y ejes en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Preparar datos para la gráfica
X, Y = np.meshgrid(np.linspace(0, T, nt), x)
Z = u

# Graficar superficie
ax.plot_surface(X, Y, Z, cmap='viridis')

# Etiquetas y título
ax.set_xlabel('Tiempo')
ax.set_ylabel('Posición')
ax.set_zlabel('u')
ax.set_title('Evolución de la Onda en 3D')
plt.show()