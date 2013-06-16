import pylab as p
import numpy as nx

import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.collections import LineCollection
import csv

# requires pyshapelib from Thuban (http://thuban.intevation.org/). 
# cd to libraries/pyshapelib in Thuban source distribution, run 
# 'python setup.py install'. 

# Lambert Conformal map of lower 48 states. 
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49, 
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95) 
fig=p.figure(figsize=(10,m.aspect*8))

canvas = FigureCanvas(fig)

# draw state boundaries. 
shp_info = m.readshapefile('statesp020','states',drawbounds=True) 

#generate empty lats and longs lists
latsList=[]
lonsList=[]

#Import previously generated CSV File, Write to a new list of lats and longs
with open('MapPlaces.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        list(row)
        lons = float(row[0])
        lonsList.append(lons)
        lats = float(row[1])
        latsList.append(lats)

x, y = m(lonsList, latsList)

#plot lists onto map
m.plot(x, y,'b-')

canvas.print_figure('map2.ps', dpi=200)
