
# coding: utf-8

# In[7]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#NOTA= Lee los archivo de temperaturas creados en R con el codigo "temperaturas.r", guardados en  el /Home. Para ejecutar este codigo, pegar los archivos en la misma carpeta

# In[9]:

#**BOGOTA**
#Crea un Data Frame (df) con la librería Pandas 
#con fechas y temperaturas para cada ciudad
df= pd.read_table("bogota2.txt")
df = df[['temperature','date']]

#Not available data
df=df.replace(r'NA', np.nan, regex=True)

#Cambia indices por tipo DatetimeIndex con las fechas en la columna Date, requerimiento para interpolar con Pandas
df=df.set_index(pd.DatetimeIndex(df['date']))
print type(df.index)
#Scatter plot de datos originales
df.plot( style='.', x= 'date', y='temperature', title="Scatter plot de datos originales Bogota", legend=None)
plt.show()

#Interpolación lineal de los datos de temp de Bogotá
inp_lineal=df.interpolate(method='linear')
inp_lineal.to_csv('inp_linealBog.csv')

#Interpolacion polinómica de los datos de temp de Bogotá
inp_polBog=df.interpolate(method='polynomial', order=1)
inp_polBog.to_csv('inp_polBog.csv')

#interpolacion por splines de los datos de temp de Bogotá
inp_splBog=df.interpolate(method='spline', order=3)
inp_splBog.to_csv('inp_splBog.csv')

plt.plot(df.index, df.temperature,'o', inp_lineal.index, inp_lineal.temperature,'-', inp_polBog.index, inp_polBog.temperature, '-',inp_splBog.index, inp_splBog.temperature, '-')
plt.ylabel('tiempo')
plt.xlabel('temperatura')
plt.title("Interpolaciones lineales, polinomicas(grado1) y por splin- Bogota")
plt.savefig("Bogota_interpolaciones.png", transparent = True)

plt.show()


# In[10]:


#**CALI**
#Lee el archivo de temperaturas de Cali creado en R con el codigo "temperaturas.r" .Crea un Data Frame (df) con la librería Pandas 
#con datos y temperatura
df= pd.read_table("cali2.txt")
df = df[['temperature','date']]

#Not available data
df=df.replace(r'NA', np.nan, regex=True)

#Cambia indices por tipo DatetimeIndex con las fechas en la columna Date, requerimiento para interpolar con Pandas
df=df.set_index(pd.DatetimeIndex(df['date']))

#Scatter plot de datos originales
df.plot( style='.', x= 'date', y='temperature', title="Scatter plot de datos originales Cali", legend=None)
plt.show()

#Interpolación lineal de los datos de temp de Cali
inp_lineal2=df.interpolate(method='linear')
inp_lineal2.to_csv('inp_linealCali.csv')

#Interpolacion polinómica de los datos de temp de Cali
inp_polCal=df.interpolate(method='polynomial', order=1)
inp_polCal.to_csv('inp_polCal.csv')

#interpolacion por splines de los datos de temp de Cali
inp_splCal=df.interpolate(method='spline', order=3)
inp_splCal.to_csv('inp_splCal.csv')

plt.plot(df.index, df.temperature,'o', inp_lineal2.index, inp_lineal2.temperature,'-', inp_polCal.index, inp_polCal.temperature, '-',inp_splCal.index, inp_splCal.temperature, '-')
plt.ylabel('tiempo')
plt.xlabel('temperatura')
plt.title("Interpolaciones lineales, polinomicas(grado1) y por splin- Cali")
plt.savefig("Cali_interpolaciones.png", transparent = True)
plt.show()



# In[11]:


#**Bucaramanga**
#Lee el archivo de temperaturas de Bucaramanga creado en R con el codigo "temperaturas.r" .Crea un Data Frame (df) con la librería Pandas 
#con datos y temperatura
df= pd.read_table("Bmanga2.txt")
df = df[['temperature','date']]

#Not available data
df=df.replace(r'NA', np.nan, regex=True)

#Cambia indices por tipo DatetimeIndex con las fechas en la columna Date, requerimiento para interpolar con Pandas
df=df.set_index(pd.DatetimeIndex(df['date']))

#Scatter plot de datos originales
df.plot( style='.', x= 'date', y='temperature', title="Scatter plot de datos originales Bucaramanga", legend=None)
plt.show()

#Interpolación lineal de los datos de temp de Bga
inp_lineal4=df.interpolate(method='linear')
inp_lineal4.to_csv('inp_linealBga.csv')

#Interpolacion polinómica de los datos de temp de Bga
inp_polBga=df.interpolate(method='polynomial', order=1)
inp_polBga.to_csv('inp_polBga.csv')

#interpolacion por splines de los datos de temp de Bga
inp_splBga=df.interpolate(method='spline', order=3)
inp_splBga.to_csv('inp_splBga.csv')

plt.plot(df.index, df.temperature,'o', inp_lineal4.index, inp_lineal4.temperature,'-', inp_polBga.index, inp_polBga.temperature, '-',inp_splBga.index, inp_splBga.temperature, '-')
plt.ylabel('tiempo')
plt.xlabel('temperatura')
plt.title("Interpolaciones lineales, polinomicas(grado1) y por splin- Bucaramanga")
plt.savefig("Bucaramanga_interpolaciones.png", transparent = True)
plt.show()


# In[17]:


#**Barranquilla**
#Lee el archivo de temperaturas de BQUILLA creado en R con el codigo "temperaturas.r" .Crea un Data Frame (df) con la librería Pandas 
#con datos y temperatura
df= pd.read_table("Bquilla2.txt")
df = df[['temperature','date']]

#Not available data
df=df.replace(r'NA', np.nan, regex=True)

#Cambia indices por tipo DatetimeIndex con las fechas en la columna Date, requerimiento para interpolar con Pandas
df=df.set_index(pd.DatetimeIndex(df['date']))

#Scatter plot de datos originales
df.plot( style='.', x= 'date', y='temperature', title="Scatter plot de datos originales Barranquilla", legend=None)
plt.show()

#Interpolación lineal de los datos de temp de Cali
inp_lineal3=df.interpolate(method='linear')
inp_lineal3.to_csv('inp_linealBquilla.csv')

#Interpolacion polinómica de los datos de temp de Cali
inp_polBq=df.interpolate(method='polynomial', order=1)
inp_polBq.to_csv('inp_polBq.csv')

#interpolacion por splines de los datos de temp de Cali
inp_splBq=df.interpolate(method='spline', order=3)
inp_splBq.to_csv('inp_splBq.csv')

plt.plot(df.index, df.temperature,'o', inp_lineal3.index, inp_lineal3.temperature,'-', inp_polBq.index, inp_polBq.temperature, '-',inp_splBq.index, inp_splBq.temperature, '-')
plt.ylabel('tiempo')
plt.xlabel('temperatura')
plt.title("Interpolaciones lineales, polinomicas(grado1) y por splin- Barranquilla")
plt.savefig("Bquilla_interpolaciones.png", transparent = True)
plt.show()


# In[15]:


#**Ipiales**
#Lee el archivo de temperaturas de BQUILLA creado en R con el codigo "temperaturas.r" .Crea un Data Frame (df) con la librería Pandas 
#con datos y temperatura
df= pd.read_table("Ipiales2.txt")
df = df[['temperature','date']]

#Not available data
df=df.replace(r'NA', np.nan, regex=True)

#Cambia indices por tipo DatetimeIndex con las fechas en la columna Date, requerimiento para interpolar con Pandas
df=df.set_index(pd.DatetimeIndex(df['date']))

#Scatter plot de datos originales
df.plot( style='.', x= 'date', y='temperature', title="Scatter plot de datos originales Ipiales", legend=None)
plt.show()

#Interpolación lineal de los datos de temp de Cali
inp_lineal5=df.interpolate(method='linear')
inp_lineal5.to_csv('inp_linealIpiales.csv')

#Interpolacion polinómica de los datos de temp de Cali
inp_polIp=df.interpolate(method='polynomial', order=1)
inp_polIp.to_csv('inp_polIp.csv')

#interpol                                                                                                                                                                   acion por splines de los datos de temp de Cali
inp_splIp=df.interpolate(method='spline', order=3)
inp_splIp.to_csv('inp_splIp.csv')

plt.plot(df.index, df.temperature,'o', inp_lineal5.index, inp_lineal5.temperature,'-', inp_polIp.index, inp_polIp.temperature, '-',inp_splIp.index, inp_splIp.temperature, '-')
plt.ylabel('tiempo')
plt.xlabel('temperatura')
plt.title("Interpolaciones lineales, polinomicas(grado1) y por splin- Ipiales")
plt.savefig("Ipiales_interpolaciones.png", transparent = True)
plt.show()


# In[ ]:

print ("Al analizar los gráficos y archivos .csv, generados desde las interpolaciones para cada ciudad, se puede concluir que \n Pese a que las 3 interpolaciones coinciden su mayoría a generar las mismas lineas, la diferencia de estas está marcada en los intervalos en donde \n# se tienen valores 'NA'. Así como se puede ver, la interpolación por splin en grado 3 demuestra definir varios polinomios que se ajustaran al espacio \n # carente de datos. Así como se explica en este recurso web: http://www.uv.es/~diaz/mn/node40.html, este tipo de interpolacion proporciona un excelente ajuste \n # para los datos, garantizando continuidad , existiendo un polinomio distinto para cada intervalo entre dos datos.\n #Gráficamente se puede observar que especialmente en donde hay baches de datos, la interpolacipon por splin (azul claro), hace un salto menos directo al siguiente dato diponible.")