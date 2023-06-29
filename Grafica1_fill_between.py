#Grafica X contra Y en donde X = r cos(Φ) & Y = r sin(Φ). El parametro r está definido, a su vez, como;
# r = 2 - 2 * sin(Φ) + sin(Φ) * (√|cos(Φ)| / sin(Φ) + 1.4)
#miesntras que Φ es un parametro independiente que se encuentra en el intervalo [0, 2pi].


import matplotlib.pyplot as plt
import numpy as np

phi = np.linspace(0, 2*np.pi, 1000)
r = 2 - 2 * np.sin(phi) + np.sin(phi) * (np.sqrt(np.abs(np.cos(phi)))) / (np.sin(phi) + 1.4)
x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y, linewidth=3, color='b', markersize=10)
plt.fill_between(x, y, color='red')
plt.title('Gráfico de X = r cos(Φ) & Y = r sin(Φ)')
plt.axis('equal')
plt.axis('off')

plt.show()
