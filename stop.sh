#!/bin/sh

kill `ps aux | fgrep 'python pointServer.py' | grep -v fgrep | awk '{ print $2 }'`
