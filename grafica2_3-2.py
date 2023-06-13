import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(x, y)

Z = np.abs(np.cos(X) + np.cos(Y))**1/2

fig = plt.figure()

ax1 = fig.add_subplot(121, projection='3d')
ax1.set_title('Trisurf')
ax1.plot_trisurf(X.flatten(), Y.flatten(), Z.flatten(), cmap='magma')

ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title('Wireframe')
ax2.plot_wireframe(X, Y, Z, cmap='magma')

for ax in [ax1, ax2]:
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

ax.set_title('Superficie de la funcion Z = |cos(X)+cos(Y)|^1/2')

fig.tight_layout()

plt.savefig('grafica2_3-2.png')