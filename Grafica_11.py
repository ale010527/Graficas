#Sea x(t) = sin(3t) & y(t) = sin(4t) ;t=(0, 2pi, 100)

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 100)
xt = np.sin(3*t)
yt = np.sin(4*t)

plt.plot(t, xt, linewidth = '4', color = 'g', markersize = '8', label = 'x(t) = sin(3t)')
plt.plot(t, yt, linewidth = '4', color = 'b', markersize = '8', label = 'y(t) = sin(4t)')
plt.legend()
plt.xlabel('Eje X', fontsize = '12')
plt.ylabel('Eje Y', fontsize = '12')
plt.title('Grafica de: x(t) = sin(3t) & y(t) = sin(4t)')
a = plt.gca()
plt.grid(True)
plt.savefig('Grafica_11.png')