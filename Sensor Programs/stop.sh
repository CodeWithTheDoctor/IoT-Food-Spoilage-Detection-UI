#!/bin/bash

# Find the process ID (PID) of the running main.py
if pgrep -f main.py > /dev/null
then
    pkill -f main.py
    echo "Stopped main.py."
else
    echo "main.py is not running."
fi
