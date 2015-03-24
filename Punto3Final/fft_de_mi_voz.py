
# coding: utf-8


from scipy.io import wavfile
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from pylab import *


 
sample, data = wavfile.read('nombre.wav')

#intervalo de tiempo
time = np.arange(0, len(data)/float(sample), 1/float(sample))
data=data/(2.**15)

#Intervalo de grabación del mismo tamaño que el tamaño de Data
n=len(data)
n2=len(time)


#Transformada de Fourier para sennal no periodica

from scipy.fftpack import fft, fftfreq, ifft

fftx = fft(data)/n # FFT Normalizado
freq = fftfreq(n, 1) # se recuperan las frecuencias

#Seleccionamos los valores positivos tanto de la trasformada como de la frecuencia
c=abs(fftx)
d=abs(freq)
#La maxima amplitud de los armónicos individuales
max_arm=max(c)
print max_arm

#Convertimos  a Series para acceder al índice de la amplitud y a su frecuencia correspondiente en ese indice
serie_fftx=pd.Series(c)
serie_freq=pd.Series(d)

indice=list(serie_fftx).index(max_arm)
frec_en_indice=serie_freq.values[indice]

print indice, frec_en_indice

plot(np.abs(freq),np.abs(fftx))
plt.ylabel('Amplitud')
plt.xlabel('frecuencia')
plt.title('Transformada de Fourier de LA VOZ y maxima amplitud del armonico', fontsize=20)
plot(frec_en_indice,max_arm, 'ro')
plt.savefig("mivoz_fft.png", transparent = True)
plt.show()

#http://hyperphysics.phy-astr.gsu.edu/hbase/audio/geowv.html#c1
print ("Asi como se muestra en el enlace, la maxima ampliud en una onda tipo 'sawtooth', esa contendrá todos los armónicos de la sennal \n por lo que la maxima amplitud, como lo indica el gráfico es la asociada al primer armónico, que está sennalado en el gráfico obtenido")




#Recursos Electronicos
##La transformada de Fourier demuestra la amplitud de todos los armonicos de la señal, en función de la frecuencia
#http://hyperphysics.phy-astr.gsu.edu/hbase/audio/Fourier.html#c1
#http://www.facstaff.bucknell.edu/mastascu/eLessonsHTML/Freq/Freq4Note8MatlabExample.htm