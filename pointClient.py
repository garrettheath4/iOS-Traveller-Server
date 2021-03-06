"""
pointClient.py

This module acts as a basic HTTP client that requests the GPS coordinate on
the running pointServer.

Author: Garrett Heath Koller
"""

import sys

import socket

HOST, PORT = "localhost", 58974

def request(data):
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(data + "\n")

        # Receive data from the server and shut down
        received = sock.recv(1024)
    finally:
        sock.close()

    print "Sent:     {0}".format(data)
    print "Received: {0}".format(received)


def init():
    global HOST
    global PORT
    if len(sys.argv) >= 2:
        HOST = str(sys.argv[1])
    if len(sys.argv) >= 3:
        PORT = int(sys.argv[2])

def testNYC():
    request("GET *ALL")
    request("GET New York City")
    request("GET No such city")

    request("POST New York City 40.714172 -74.006393")

    request("GET *ALL")
    request("GET New York City")
    request("GET No such city")

def placeBuses():
    request("POST Traveller Bus #1 -79.450362 37.792104")
    request("POST Traveller Bus #2 -79.449998 37.791757")
    request("POST Traveller Bus #3 -79.448922 37.791583")
    request("POST Traveller Bus #4 -79.450014 37.792037")

def main():
    init()
    print("Connecting to %s on port %d." % (HOST, PORT))
    #testNYC()

    request("GET *ALL")

    placeBuses()

    request("GET *ALL")

if __name__ == "__main__":
    main()

