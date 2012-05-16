"""
gps.py

This module converts a Python list containing GPS point of interest information
to a .KML formatted XML document.

Author: Garrett Heath Koller
"""

from lxml import etree as ET


class GPS:
    def __init__(self):
        self.GPSpoints = {}

    def updatePoint(self, gpsName, gpsLat, gpsLon):
        self.GPSpoints[gpsName] = (gpsName, gpsLat, gpsLon)

    def getPoint(self, gpsName):
        if gpsName in self.GPSpoints:
            requestedPoint = [self.GPSpoints[gpsName]]
        else:
            requestedPoint = []
        return self._toXML(requestedPoint)

    def getAllPoints(self):
        return self._toXML(list(self.GPSpoints.values()))

    def _toXML(self, points):
        """
        Receives a list of tuples of GPS data, where each tuple is in the form
           ( name(str), description(str), latitude(str), longitude(str) )
        , and returns a string in the .KML format (an XML document).
        """
        
        root = ET.Element('kml', {'xmlns':"http://www.opengis.net/kml/2.2"})
        document = ET.SubElement(root, 'Document')

        for data in points:
            (gpsName, gpsLat, gpsLon) = data
            placemark   = ET.SubElement(document,  'Placemark')
            name        = ET.SubElement(placemark, 'name')
            name.text   = gpsName
            description      = ET.SubElement(placemark, 'description')
            description.text = gpsName
            point = ET.SubElement(placemark, 'Point')
            coordinates      = ET.SubElement(point, 'coordinates')
            coordinates.text = '' + gpsLat + ',' + gpsLon + ',0'

        return ET.tostring(root, encoding='UTF-8', pretty_print=True,
                           xml_declaration=True)
        # write to file:
        # tree = ET.ElementTree(root)
        # tree.write('output.xml', pretty_print=True, xml_declaration=True)



def main():
    gps = GPS()
    gps.updatePoint('New York City', '-74.006393', '40.714172')
    print(gps.getAllPoints())

if __name__ == '__main__':
    main()










