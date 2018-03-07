# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 14:44:36 2018

@author: Matias Garavaglia
"""
import numpy as np
import matplotlib.pylab as plt

"""Seteo de variables principales:
    x= cantidad de valores dentro del arreglo
    y= cantidad de valores de la ventana"""

y = 100000
x = 10
"""Esta variable es solo para usar de eje x en el gráfico"""
valores_de_x = np.arange(y)

"""Creación del array de ceros de dimensión "y"."""
S_total = np.zeros((y,), dtype=np.int)
R_total = np.zeros((y,), dtype=np.int)
Out_signal = np.zeros((y,), dtype=np.int)

"""Creación de un array que vaya de 10 en 10 para luego cambiar el array
principal"""
ventana = np.arange(0, y-x+1, x)

"""Loop central donde se toman los valores del array principal S_total y R_total
y según como sale el flip coin se cambian simultaneamente sus valores, al mismo
tiempo se crea el dataset Ouput, teniendo en cuenta los valores de S y R"""

for i in ventana:
    moneda = np.random.random_integers(1, high=3, size=1)
    if moneda == 1:
        S_total[i:i+x] = 1
        R_total[i:i+x] = 0
        Out_signal[i:i+x] = 1
    elif moneda == 2:
        S_total[i:i+x] = 0
        R_total[i:i+x] = 1
        Out_signal[i:i+x] = 0
    elif np.size(Out_signal[i-x:i])> 0:
        Out_signal[i:i+x] = Out_signal[i-x:i]
    else:
        S_total[i:i+x] = 0
        R_total[i:i+x] = 0
        Out_signal[i:i+x] = 0

print S_total         
print R_total
print Out_signal
        
plt.scatter(valores_de_x, S_total)
plt.xlabel('cadena de datos')
plt.ylabel('valores de S')
plt.axis('tight')
plt.show()
    
plt.scatter(valores_de_x, R_total)
plt.xlabel('cadena de datos')
plt.ylabel('valores de R')
plt.axis('tight')
plt.show()

plt.scatter(valores_de_x, Out_signal)
plt.xlabel('cadena de datos')
plt.ylabel('valores de O')
plt.axis('tight')
plt.show()


np.savetxt("Valores_de_s.csv", S_total, delimiter=",")
np.savetxt("Valores_de_r.csv", R_total, delimiter=",")
