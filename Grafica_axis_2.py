import matplotlib.pyplot as plt
import numpy as np

phi = np.linspace(0, 4*np.pi, 4000)
r = 105 + 100 * np.sin(4.5*phi) * np.cos(4*phi)
λ = phi - np.cos(10 * phi) / 10
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
