#3.-f(t)=t*exp^-2t;                 (-1,5) 300_puntos grafica=color K marcador=10 x=eje_X y=eje_Y que aparesca la expresion como titulo
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 24, 250)
ft = t * np.exp(-2*t)
plt.plot(t, ft, '*', linewidth=3, color='g', markersize=10)
plt.title('$F(t) = t * exp^(-2t)$')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
#a.set_facecolor('k')
plt.grid(True)
plt.savefig('Grafica_3.png')