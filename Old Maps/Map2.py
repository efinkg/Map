from pykml import parser

kml_file = "/Users/glassman/Documents/Engineering/Solidworks/Map/history-05-23-2013.kml"

with open(kml_file) as f:

    doc = parser.parse(f)

coordinate = doc.Point("coordinates")
print coordinate
