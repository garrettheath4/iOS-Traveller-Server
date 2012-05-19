#!/bin/sh

screen -d -m -S pointServer python pointServer.py

sleep 2

screen -d -m -S bus1 python simulateBus1.py
screen -d -m -S bus2 python simulateBus2.py
screen -d -m -S bus3 python simulateBus3.py
screen -d -m -S bus4 python simulateBus4.py
