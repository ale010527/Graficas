# Sea x(t) = t + 2sin(2t) & y(t) = t + 2cos(5t) t = (-2pi, 2pi, 100) x=eje_X y=eje_Y que aparesca la expresion como titulo

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-2*np.pi, 2*np.pi, 100)
xt = t + 2*np.sin(2*t)
yt = t + 2*np.cos(5*t)

plt.plot(t, xt, linewidth = '4', color = 'r', markersize = '8', label = 'x(t) = t + 2sin(2t)')
plt.plot(t, yt, linewidth = '4', color = 'k', markersize = '8', label = 'y(t) = t + 2cos(5t)')
plt.legend()
plt.xlabel('Eje X', fontsize = '12')
plt.ylabel('Eje Y', fontsize = '12')
plt.title('Grafica de: x(t) = t + 2sin(2t) & y(t) = t + 2cos(5t)')
a = plt.gca()
plt.grid(True)
plt.savefig('Grafica_10.png')