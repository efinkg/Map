from xml.etree import ElementTree
from pykml import parser
from os import path
import csv

kml_file = path.join( \
    '/Users/glassman/Documents/Engineering/Solidworks/Map/history-05-24-2013.kml')

with open(kml_file) as f:
     root = parser.parse(f).getroot()

writer = csv.writer(open("MapPlaces.csv", "wb"))

def coordUnique(seq, idfun=None):
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   coordList= []
   for coord in root.Document.Placemark.Track.coord:
       marker = idfun(coord)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen:
           continue
       seen[marker] = 1
       coord = str(coord)
       l = [float(x) for x in coord.split(' ')]
       coord = l
       coord = list(coord)
       del(coord[2])
       writer.writerow(list(coord))
       coordList.append(coord)
   return coordList

listCoords = coordUnique(root)
