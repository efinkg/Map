import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
# draw state boundaries.
# data from U.S Census Bureau
# http://www.census.gov/geo/www/cob/st1990.html
shp_info = m.readshapefile('statesp020','states',drawbounds=True)

fig=Figure()
canvas = FigureCanvas(fig)
m.ax = fig.add_axes([0, 0, 1, 1])
fig.set_size_inches((8/m.aspect, 8.))

lats = [41.38, 43.18, 48.87, 43.60, 46.52, 43.28, 46.20]
lons = [ 2.18,  3.00,  2.32,  1.43,  6.63,  5.37,  6.15]
name = ['Barcelona', 'Narbonne', 'Paris', 'Toulouse', 'Lausanne', 'Marseille', 'Geneva']

x, y = m(lons, lats)
m.plot(x, y, 'bo')
canvas.print_figure('map.png', dpi=100)
