#Grafica X contra Y en donde X = r cos(Φ) & Y = r sin(Φ). El parametro r está definido, a su vez, como;
# r = 2 - 2 * sin(Φ) + sin(Φ) * (√|cos(Φ)| / sin(Φ) + 1.4)
#miesntras que Φ es un parametro independiente que se encuentra en el intervalo [0, 2pi].

import matplotlib.pyplot as plt
import numpy as np

phi = np.linspace(0, 2*np.pi, 100)
r = 2 - 2 * np.sin(phi) + np.sin(phi) * (np.sqrt(np.abs(np.cos(phi))) / np.sin(phi) + 1.4 )
X_phi = r * np.cos(phi)
Y_phi = r * np.sin(phi)

plt.plot(X_phi, Y_phi, linewidth=3, color='b', markersize=10, label='X = r cos(Φ)')
plt.plot(phi, Y_phi, linewidth=3, color='g', markersize=10, label='Y = r sin(Φ)')
plt.legend()
plt.xlabel('Eje X', fontsize=14)
plt.ylabel('Eje Y', fontsize=14)
plt.title('Gráfico de X = r cos(Φ) & Y = r sin(Φ)')
plt.fill_between(X_phi, Y_phi, color='red')
plt.grid(True)
plt.axis('equal')
plt.axis('off')

plt.show()
