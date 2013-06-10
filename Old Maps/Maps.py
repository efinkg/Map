from xml.etree import ElementTree
from pykml import parser
from os import path

kml_file = path.join( \
    '/Users/glassman/Documents/Engineering/Solidworks/Map/history-05-24-2013.kml')

with open(kml_file) as f:
     root = parser.parse(f).getroot()

def coords(seq):
    coordList = []
    for coord in root.Document.Placemark.Track.coord:
        if coord not in coordList:
            coordList.append(coord)
    return coordList
