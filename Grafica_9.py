#9.- x(t) = cos^3(t) y(t) = sin^3(t)  (0, 2pi) 100 puntos x=eje_X y=eje_Y que aparesca la expresion como titulo
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 100)
xt = np.cos(t)**3
yt = np.sin(t)**3

plt.plot(t, xt, linewidth=3, color='r', markersize=10, label = 'x(t) = cos^3(t)')
plt.plot(t, yt, linewidth=3, color='k', markersize=10, label = 'y(t) = sin^3(t)')
plt.legend()
plt.xlabel('Eje X', fontsize = '14')
plt.ylabel('Eje Y', fontsize = '14')
plt.title('Grafica de: x(t) = cos^3(t) & y(t) = sin^3(t)')
a = plt.gca()
plt.grid(True)
plt.savefig('Grafica_9.png')