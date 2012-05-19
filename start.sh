#!/bin/sh

screen -S pointServer python pointServer.py

sleep 2

screen -S bus1 python simulateBus1.py
screen -S bus2 python simulateBus2.py
screen -S bus3 python simulateBus3.py
screen -S bus4 python simulateBus4.py
