
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


# In[2]:

#Descarga del archivo
url='http://www.cgd.ucar.edu/cas/catalog/surface/dai-runoff/coastal-stns-byVol-updated-oct2007.txt'
urllib.urlretrieve(url, "top300.txt")


# In[3]:

os.system("sed 's/,/ /g' top300.txt >sincoma.txt")
os.system("sed '621d' sincoma.txt >rios.txt")
os.system("rm sincoma.txt")
os.system("rm top300.txt")


# In[6]:

#Se genera un Data Frame para obtener los datos
a=np.genfromtxt('rios.txt', dtype=None, skiprows=1, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14))
ddf = pd.DataFrame(a)


# In[7]:

#Se sortea el DataFrame de acuerdo a la tasa de flujo m2s_ratio
result = ddf.sort(['f1'], ascending=False)
top300=result.head(300)
top300.columns = ['No', 'm2s_ratio', 'lonm', 'latm', 'area(km2)', 'Vol(km3/yr)','nyr', 'yrb', 'yre', 'elev(m)', 'CT', 'CN', 'River_Name', 'OCN', 'Station_Name']
top300.to_csv('top_300_rios.csv')
print top300


# In[7]:






# In[ ]:



