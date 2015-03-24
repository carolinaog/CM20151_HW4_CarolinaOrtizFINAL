
# coding: utf-8

# In[1]:

import urllib
import os
import StringIO
import pandas as pd
from pandas import read_csv
import numpy as np
from numpy import * 
from pandas import DataFrame

import matplotlib.pyplot as plt
import mpl_toolkits
import string
import matplotlib.cm as cm

from mpl_toolkits.basemap import Basemap


# In[2]:

#Descarga del archivo
url='http://www.cgd.ucar.edu/cas/catalog/surface/dai-runoff/coastal-stns-byVol-updated-oct2007.txt'
urllib.urlretrieve(url, "top300.txt")
os.system("sed 's/,/ /g' top300.txt >sincoma.txt")
os.system("sed '621d' sincoma.txt >rios.txt")
os.system("rm sincoma.txt")
os.system("rm top300.txt")


# In[16]:

#Se genera un Data Frame para obtener los datos
a=np.genfromtxt('rios.txt', dtype=None, skiprows=1, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14))
ddf = pd.DataFrame(a)
#Se sortea el DataFrame de acuerdo a la tasa de flujo vol(km3/yr) para los principales 150 rios y se genera el archivo top_150_rios.csv
result = ddf.sort(['f1'], ascending=False)
top150=result.head(150)
top150.columns = ['No', 'm2s_ratio', 'lonm', 'latm', 'area(km2)', 'Vol(km3/yr)','nyr', 'yrb', 'yre', 'elev(m)', 'CT', 'CN', 'River_Name', 'OCN', 'Station_Name']
top150.to_csv('top_150_rios.csv')
print top150


# In[6]:

#Se lee el archivo .csv y se hacen arreglos con lat, lon, y flujo, a partir de las columnas del data frame
lista=pd.read_csv('top_150_rios.csv')

ddf = pd.DataFrame(lista)

lats = ddf['latm'][:]
lons = ddf['lonm'][:]
labels= ddf['River_Name'][:]
rate=ddf['m2s_ratio']

lon = pd.np.array(lons)
lat = pd.np.array(lats)
labs= pd.np.array(labels)
descargo= pd.np.array(rate)


# In[15]:

m = Basemap(projection='hammer',lat_0=0,lon_0=-70)
x, y = m(lon,lat)

m.scatter(x,y,marker='o',s=descargo*0.05,c=descargo, alpha=0.5,zorder=4)
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='white')
c = plt.colorbar(orientation='horizontal')
c.set_label("Tasa de descargo")


plt.title('Ubicacion de los 150 rios con mayor tasa de descargue',fontsize=15)
plt.savefig("tasa_flujo_150.jpg", transparent = True)
plt.show()





# In[ ]:



