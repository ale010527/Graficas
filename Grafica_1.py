#1.-f(x)=5-4x-x^2;        (-6,2) 200_puntos grafica verde x=eje_X y=eje_Y que aparesca la expresion como titulo

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 2, 200)
fx = 5 - 4*x - x**2
plt.plot(x, fx, '*', linewidth=3, color='g', markersize=10)
plt.title('$F(x) = 5 - 4x - x^2$')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('Grafica_1.png')