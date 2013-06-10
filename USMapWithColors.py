import pylab as p
import numpy as nx

from mpl_toolkits.basemap import Basemap
from matplotlib.collections import LineCollection 
from matplotlib.colors import rgb2hex 
import random 

# requires pyshapelib from Thuban (http://thuban.intevation.org/). 
# cd to libraries/pyshapelib in Thuban source distribution, run 
# 'python setup.py install'. 

# Lambert Conformal map of lower 48 states. 
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49, 
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95) 
fig=p.figure(figsize=(8,m.aspect*8)) 
fig.add_axes([0.1,0.1,0.8,0.8]) 
# draw state boundaries. 
shp_info = m.readshapefile('statesp020','states',drawbounds=True) 
# choose a color for each climate division (randomly). 
colors={} 
statenames=[] 
for shapedict in m.states_info: 
    statename = shapedict['STATE'] 
    colors[statename] = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)) 
    statenames.append(statename) 
# cycle through climate divnames, color each one. 
for nshape,seg in enumerate(m.states): 
    xx,yy = zip(*seg) 
    color = rgb2hex(colors[statenames[nshape]]) 
    p.fill(xx,yy,color,edgecolor=color) 
# draw meridians and parallels. 
m.drawparallels(nx.arange(25,65,20),labels=[1,0,0,0]) 
m.drawmeridians(nx.arange(-120,-40,20),labels=[0,0,0,1]) 
p.title('Filling State Polygons') 
p.show() 
