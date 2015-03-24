
# coding: utf-8

# In[62]:

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



data = Dataset('air.mon.ltm.nc', 'r', format='NETCDF4')
print data


# In[63]:

print data.dimensions


# In[64]:

from pylab import *
                         
time = data.variables['time'][:]
lats = data.variables['lat'][:]
lons = data.variables['lon'][:]
nn = data.variables['climatology_bounds'][:]
aire = data.variables['air'][:]
data.close()



# In[60]:

m = Basemap(projection='hammer',lat_0=0,lon_0=-70)
x, y = m(lon, lat)
plt.figure(figsize=(10,7))
m.drawcoastlines()
m.drawmeridians(np.arange(0,360,30))
m.drawparallels(np.arange(-90,90,30))
m.drawmapboundary(fill_color='white')
m.contour(x,y,aire,linewidths=1)
c = plt.colorbar(orientation='horizontal')
c.set_label("Temp Aire")


# In[35]:




# In[ ]:



