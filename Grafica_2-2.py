import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-2, 2.2, 0.2)
y = np.arange(-2, 2.2, 0.2)

X, Y = np.meshgrid(x, y)

Z = X * np.exp(-x**2 - y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap = 'viridis', linewidth = 0) 

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('Superficie de la funcion Z = Xe^-x^2-y^2')
ax.set_facecolor('white')

fig.colorbar(surf, ax = ax)

plt.savefig('Grafica2_2-2.png')