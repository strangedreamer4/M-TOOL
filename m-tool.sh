#!/bin/bash

# Check if the script is being run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root."
    exit 1
fi

# Update package information
sudo apt update -y
chmod +x .login.py
chmod +x .m-tool.sh

# Clear the terminal
clear
python3 .log_ip.py && clear
# Run the Python script (assuming .login.py is in the same directory as this script)
python3 .login.py
