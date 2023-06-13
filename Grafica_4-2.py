import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)

X, Y = np.meshgrid(x, y)

Z = np.sin(np.abs(X) - np.abs(Y))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap = 'cividis', linewidth = 0) 

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('Superficie de la funcion Z = sin(|X| - |Y|)')
ax.set_facecolor('white')

fig.colorbar(surf, ax = ax)

plt.savefig('Grafica_4-2.png')