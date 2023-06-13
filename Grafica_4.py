#4.-h(t)=e^-0.1t * sin(2t);         (0,24) 250_puntos x=eje_X y=eje_Y que aparesca la expresion como titulo 
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 24, 250)
ht = np.exp(-0.1*t) *np.sin(2*t)
plt.plot(t, ht, 'o', linewidth=3, color='g', markersize=10)
plt.title('$h(t) = e^-0.1 * tsin(2t)$')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('Grafica_4.png')