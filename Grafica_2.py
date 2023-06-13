#2.-f(x)=2x^2-8x-11;                (-1,5) 100_puntos grafica roja marcador=10 x=eje_X y=eje_Y que aparesca la expresion como titulo
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 5, 100)
fx = 2*x**2 - 8*x -11
plt.plot(x, fx, 'o', linewidth=3, color='r', markersize=10)
plt.title('$F(x) = 2x^2 - 8x - 11')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
a.set_facecolor('k')
plt.grid(True)
plt.savefig('Grafica_2.png')