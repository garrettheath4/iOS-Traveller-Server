"""
gps.py

This module converts a Python list containing GPS point of interest information
to a .KML formatted XML document.

Author: Garrett Heath Koller
"""

import os

import pickle
from lxml import etree as ET


class GPS:
    def __init__(self):
        self.GPSpoints = {}
        self.fileName = "gps_data.dat"

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

        root = ET.Element('kml')
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
            # Note that KML stores coordinates as longitude,latitude,
            # not as latitude,longitude like you would think
            coordinates.text = '' + gpsLon + ',' + gpsLat + ',0'

        tree = ET.ElementTree(root)

        return ET.tostring(tree, encoding='UTF-8', pretty_print=True,
                           xml_declaration=True).replace("'", '"')
        # write to file:
        # tree.write('output.xml', pretty_print=True, xml_declaration=True)

    def save(self, fileName = None):
        """Saves pickled accounts to a file.  The parameter
        allows the user to change file names."""
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            raise ValueError("No filename given to save GPS data as")
        fileObj = open(self.fileName, 'wb')
        pickle.dump(self.GPSpoints, fileObj)
        fileObj.close()

    def load(self, fileName = None):
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            raise ValueError("No filename given to load GPS data from")
        fileObj = open(self.fileName, 'rb')
        self.GPSpoints = pickle.load(fileObj)
        fileObj.close()


def testSave():
    gps = GPS()
    gps.updatePoint('New York City', '-74.006393', '40.714172')
    gps.save()

def testLoad():
    gps2 = GPS()
    gps2.load()
    print(gps2.getAllPoints())

def testLoadIfExists():
    gps3 = GPS()
    if os.path.exists("./" + gps3.fileName):
        testLoad()
    else:
        print(gps3.fileName + " does not exist\n")

def main():
    testLoadIfExists()
    testSave()
    testLoad()

if __name__ == '__main__':
    main()







