#8.-x(t)=(1+sin(t))(cos(t));        Linea de color cyan (0,2pi) 100_puntos x=eje_X y=eje_Y que aparesca la expresion como titulo
#   y(t)=(1+2sin(t))(sin(t));       Linea de color magenta

import matplotlib.pyplot as plt
import numpy as np 

t = np.linspace(0, 2*np.pi, 100)
xt = (1 + np.sin(t)) * (np.cos(t))
yt = (1 + 2 * np.sin(t)) * (np.sin(t))
plt.plot(t, xt, 'o', linewidth=3, color='cyan', markersize=10, label = 'x(t) = (1+sin(t))(cos(t))')
plt.plot(t, yt, 'o', linewidth=3, color='magenta', markersize=10, label = 'y(t) = (1+2sin(t))(sin(t))')
plt.legend()
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
plt.title('Gráfico de: x(t) = (1+sin(t))(cos(t)) y y(t) = (1+2sin(t))(sin(t))')
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('Grafica_8.png')