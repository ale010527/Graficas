import matplotlib.pyplot as plt
import numpy as np

phi = np.linspace(0, 2*np.pi, 1500)
r = -250 * np.sin(5*phi) * np.cos(4*phi)
λ = phi + np.sin(r / 100)
X = 320 + r * np.cos(λ)
Y = -240 - r * np.sin(λ)

plt.plot(X, Y, linewidth=3, color='b', markersize=10, label='X = 320 + r cos(λ)')
plt.legend()
plt.xlabel('Eje X', fontsize=14)
plt.ylabel('Eje Y', fontsize=14)
plt.title('Gráfico de: X = 320 + r cos(λ) & Y = -240 - r sin(λ)')
plt.grid(True)
plt.axis('equal')
plt.axis('off')

plt.show()
