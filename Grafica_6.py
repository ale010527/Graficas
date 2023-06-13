#6.-f(x)=x*e^-3x;                   Linea de color cyan (0,2) 100_puntos x=eje_X y=eje_Y que aparesca la expresion como titulo
#   g(x)=1-3x*e^-3x;                Linea color magenta

import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 2, 100)
fx = x * np.exp(-3*x)
gx = (1 - 3 * x) * np.exp(-3*x)
plt.plot(x, fx, 'o', linewidth=3, color='cyan', markersize=10, label = 'f(x) = x*e^-3x')
plt.plot(x, gx, 'o', linewidth=3, color='magenta', markersize=10, label = 'g(x) = 1-3x*e^-3x')
plt.legend()
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
plt.title('Gráfico de: f(x) = x*e^-3x & g(x) = 1-3x*e^-3x ')
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('Grafica_6.png')