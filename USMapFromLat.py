import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import csv

m = Basemap(llcrnrlon= -126, \
            llcrnrlat=23, \
            urcrnrlon= -65, \
            urcrnrlat = 50, \
            resolution = 'l', \
            projection = 'tmerc', \
            lon_0 = -100, \
            lat_0 = 37)

fig = Figure()
canvas = FigureCanvas(fig)
m.ax = fig.add_axes([0, 0, 1, 1])
fig.set_size_inches((8/m.aspect, 8.))

latsList=[]
lonsList=[]

with open('MapPlaces.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        list(row)
        lons = float(row[0])
        lonsList.append(lons)
        lats = float(row[1])
        latsList.append(lats)

x, y = m(lonsList, latsList)
m.plot(x, y,'b-')

m.drawcoastlines(color='black')
m.drawcountries(color='black')
m.drawstates(color='gray')
canvas.print_figure('mapUS.png', dpi=100)
