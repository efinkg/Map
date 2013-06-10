import pylab as p
import numpy as nx

from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
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

canvas = FigureCanvas(fig)
# draw state boundaries. 
shp_info = m.readshapefile('statesp020','states',drawbounds=True) 
# choose a color for each climate division (randomly). 
canvas.print_figure('map2.png', dpi=100)
