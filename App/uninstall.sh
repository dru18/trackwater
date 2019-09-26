#!/bin/bash
echo "Uninstalling Track"
sudo rm -v /usr/bin/track
sudo rm -vr /var/opt/track/
sudo rm -vr /opt/track/
sudo rm -vr /var/log/track/
echo "Track uninstalled"
