import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-1, 1, 0.1)
y = np.arange(-1, 1, 0.1)

X, Y = np.meshgrid(x, y)

Z = np.cos(np.abs(X) + np.abs(Y)) * np.abs(X) + np.abs(Y)

fig = plt.figure()

ax1 = fig.add_subplot(121, projection='3d')
ax1.set_title('Trisurf')
ax1.plot_trisurf(X.flatten(), Y.flatten(), Z.flatten(), cmap='bone')

ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title('Wireframe')
ax2.plot_wireframe(X, Y, Z, cmap='bone')

for ax in [ax1, ax2]:
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

ax.set_title('Superficie de la funcion Z = sin(|X| + |Y|) * (|X| + |Y|)')

fig.tight_layout()

plt.savefig('Grafica_6-2.png')