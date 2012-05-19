#!/bin/sh

kill `ps aux | fgrep 'python pointServer.py' | grep -v fgrep | awk '{ print $2 }'`

kill `ps aux | fgrep 'python simulateBus1.py' | grep -v fgrep | awk '{ print $2 }'`
kill `ps aux | fgrep 'python simulateBus2.py' | grep -v fgrep | awk '{ print $2 }'`
kill `ps aux | fgrep 'python simulateBus3.py' | grep -v fgrep | awk '{ print $2 }'`
kill `ps aux | fgrep 'python simulateBus4.py' | grep -v fgrep | awk '{ print $2 }'`
