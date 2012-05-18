"""
pointServer.py

This module acts as a basic HTTP server that serves GPS coordinate data for
the specified point of interest (named GPS point).
Note that this module requires the gps.py module to manage the GPS point data.

Author: Garrett Heath Koller
"""

import sys

import SocketServer
import gps


def init():
    global gpsPoints
    gpsPoints = gps.GPS()
    port = 58974
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    return port


class GPSpointsRequestHandler(SocketServer.BaseRequestHandler):
    """
    This is a delegate class that must implement the handle() method.
    """

    def handle(self):
        GET  = "GET "
        POST = "POST "

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{0} wrote: ".format(self.client_address[0]) + self.data)

        if self.data.upper().startswith(GET):
            request = self.data[len(GET):]
            if request.upper() == "*ALL":
                sendStr = gpsPoints.getAllPoints()
                print("Sending data: " + sendStr)
                self.request.sendall(sendStr + '\n')
            else:
                self.request.sendall(gpsPoints.getPoint(request))
        elif self.data.upper().startswith(POST):
            request = self.data[len(POST):]
            parts = request.split(' ')
            if len(parts) >= 3:
                gpsName = ' '.join(parts[0:-2])
                gpsLat  = parts[-2]
                gpsLon  = parts[-1]
                gpsPoints.updatePoint(gpsName, gpsLat, gpsLon)
                self.request.sendall("UPDATED\n")
            else:
                self.request.sendall("ERROR\n")
        self.request.close()


def main():
    port = init()

    # Create the socket server, binding to localhost on port 9999
    server = SocketServer.TCPServer((str(), port), GPSpointsRequestHandler)

    # Activate the server; this will keep running until you interrupt
    # the program with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
