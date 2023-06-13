#7.-f(t)=sin(3t)*cos(2t);           Linea de color cyan (0,4pi) 100_puntos x=eje_X y=eje_Y que aparesca la expresion como titulo
#   g(t)=1/2 cos(t) + 5/2cos(5t);   Linea de color magenta

import matplotlib.pyplot as plt
import numpy as np 

t = np.linspace(0, 4*np.pi, 100)
ft = np.sin(3*t) * np.cos(2*t)
gt = 1/2 * np.cos(t) + 5/2 * np.cos(5*t)
plt.plot(t, ft, linewidth=3, color='cyan', markersize=10, label = 'f(t)=sin(3t)*cos(2t)')
plt.plot(t, gt, linewidth=3, color='magenta', markersize=10, label = 'g(t)=1/2 cos(t) + 5/2cos(5t)')
plt.legend()
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
plt.title('Gráfico de: f(t) = sin(3t)*cos(2t) y g(t) = 1/2 cos(t) + 5/2cos(5t) ')
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('Grafica_7.png')