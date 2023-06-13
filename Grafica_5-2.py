import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-1, 1, 0.1)
y = np.arange(-1, 1, 0.1)

X, Y = np.meshgrid(x, y)

Z = np.cos(np.abs(X) + np.abs(Y))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap = 'jet', linewidth = 0) 

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('Superficie de la funcion Z = sin(|X| + |Y|)')
ax.set_facecolor('white')

fig.colorbar(surf, ax = ax)

plt.savefig('Grafica_5-2.png')