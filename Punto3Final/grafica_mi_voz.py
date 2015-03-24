
# coding: utf-8

# In[1]:

from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np
from pylab import *


 
sample, data = wavfile.read('nombre.wav')

#intervalo de tiempo
time = np.arange(0, len(data)/float(sample), 1/float(sample))
data=data/(2.**15)

#Intervalo de grabación del mismo tamaño que el tamaño de Data
n=len(data)
n2=len(time)


print data
print n
print n2
print sample


#plot

plt.figure(1)
plt.plot(time,data)
plt.title('Grafica de LA VOZ')
plt.ylabel('sennal')
plt.xlabel('tiempo(s)')
plt.savefig('mi_voz.png')
plt.show()



#Recursos electronicos
#http://hyperphysics.phy-astr.gsu.edu/hbase/audio/Fourier.html#c1
#http://www.facstaff.bucknell.edu/mastascu/eLessonsHTML/Freq/Freq4Note8MatlabExample.htm
