import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import csv

#request section of Basemap in latitude longitude box
m = Basemap(llcrnrlon= -122, \
            llcrnrlat=22, \
            urcrnrlon= -64, \
            urcrnrlat = 49, \
            resolution = 'l', \
            projection = 'tmerc', \
            lon_0 = -100, \
            lat_0 = 37)

fig = Figure()
canvas = FigureCanvas(fig)
m.ax = fig.add_axes([0, 0, 1, 1])
fig.set_size_inches((8/m.aspect, 8.))

#generate map with coasts, countries, state boarders
m.drawcoastlines(color='black')
m.drawcountries(color='black')
m.drawstates(color='gray')

#generate empty lats and longs lists
latsList=[]
lonsList=[]

#generate empty stops lats and longs lists
stopsLatsList=[]
stopsLonsList=[]

#Import previously generated Tracks CSV File, Write to a new list of lats and longs
with open('MapPlaces.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        list(row)
        lons = float(row[0])
        lonsList.append(lons)
        lats = float(row[1])
        latsList.append(lats)

#Import previously generated Stops CSV File, Write to a new list of lats and longs
with open('Stops.csv', 'U') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        list(row)
        stopslons = float(row[0])
        stopsLonsList.append(stopslons)
        stopslats = float(row[1])
        stopsLatsList.append(stopslats)

#plot tracking lists onto map
x, y = m(lonsList, latsList)
m.plot(x, y,'b-')

#plot stops lists onto map
x, y = m(stopsLonsList, stopsLatsList)
m.plot(x, y,'ro')

canvas.print_figure('mapUS.png', dpi=300)
