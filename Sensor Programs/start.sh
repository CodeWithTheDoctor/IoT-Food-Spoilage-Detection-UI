#!/bin/bash

# Path to the virtual environment
VENV_PATH="env"

# Path to your Python script
SCRIPT_PATH="main.py"

# Path to log file
LOG_PATH="main.log"

# Check if the virtual environment exists
if [ ! -d "$VENV_PATH" ]; then
    echo "Virtual environment not found at $VENV_PATH."
    exit 1
fi

# Activate the virtual environment
source $VENV_PATH/bin/activate

# Check if main.py is already running
if pgrep -f $SCRIPT_PATH > /dev/null
then
    echo "$SCRIPT_PATH is already running."
else
    # Start main.py with nohup and log output to main.log
    nohup python3 $SCRIPT_PATH > $LOG_PATH 2>&1 &
    echo "Started $SCRIPT_PATH using virtual environment $VENV_PATH and logging to $LOG_PATH."
fi

# Deactivate the virtual environment
deactivate


