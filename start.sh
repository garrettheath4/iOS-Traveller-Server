#!/bin/sh

python pointServer.py &

sleep 2

python simulateBus1.py &
python simulateBus2.py &
python simulateBus3.py &
python simulateBus4.py &
