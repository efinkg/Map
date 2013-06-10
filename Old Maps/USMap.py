import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

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

lats = [41.38, 43.18, 48.87, 43.60, 46.52, 43.28, 46.20]
lons = [ 2.18,  3.00,  2.32,  1.43,  6.63,  5.37,  6.15]
name = ['Barcelona', 'Narbonne', 'Paris', 'Toulouse', 'Lausanne', 'Marseille', 'Geneva']

m.drawcoastlines(color='black')
m.drawcountries(color='black')
m.drawstates(color='gray')
x, y = m(lons, lats)
m.plot(x, y, 'bo')
canvas.print_figure('map.png', dpi=100)
