#!/bin/bash

# Print installing track
echo "Installing Track"

# Make required directories for track
sudo mkdir -v -p /opt/track/water/
sudo mkdir -v -p /var/opt/track/water/
sudo mkdir -v -p /var/log/track/water/

# Give privilleges to local user for required directories
sudo chown -vR $USER:$USER /opt/track/
sudo chown -vR $USER:$USER /var/opt/track/
sudo chown -vR $USER:$USER /var/log/track/
sudo chown -v $USER:$USER /usr/local/bin/track

# Copy source file to system
sudo cp -v track.py /opt/track/water/track.py

# Make required log file
sudo touch -v /var/log/track/water/water.log

# Make required variables
sudo touch -v /var/opt/track/water/target
sudo touch -v /var/opt/track/water/count

# Initialise variables
sudo echo 0 > /var/opt/track/water/target
sudo echo 0 > /var/opt/track/water/count

# Initialise log
sudo echo -v "" > /log/track/water/water.log

# Make command for track
sudo ln -v -s /var/opt/track/water/track /usr/local/bin/track

#  Print installation done
echo "Installation done"
