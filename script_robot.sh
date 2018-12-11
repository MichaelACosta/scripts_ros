#!/bin/bash

gnome-terminal -e 'roslaunch ydlidar lidar.launch'

sleep 3

gnome-terminal -e 'roslaunch odometry arduino.launch'

#sleep 3

gnome-terminal -e 'rosrun odometry node_test.py'
