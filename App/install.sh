#!/bin/bash
echo "Installing Track"
sudo mkdir -v -p /var/log/track/water/
sudo touch /var/log/track/water/water.log
sudo chown -v pj:pj /var/log/track/water/water.log
sudo echo "" > /log/track/water/water.log
sudo mkdir -v -p /opt/track/water/
sudo cp -v track.py /opt/track/water/track.py
sudo mkdir -v -p /var/opt/track/water/
sudo ln -v /opt/track/water/track.py /var/opt/track/water/track
sudo touch /var/opt/track/water/target
sudo chown -v $USER:$USER /var/opt/track/water/target
sudo echo 0 > /var/opt/track/water/target
sudo touch /var/opt/track/water/count
sudo chown -v $USER:$USER /var/opt/track/water/count
sudo echo 0 > /var/opt/track/water/count
sudo ln -v -s /var/opt/track/water/track /usr/bin/track
sudo chown -v $USER:$USER /usr/bin/track
echo "Track installed"
