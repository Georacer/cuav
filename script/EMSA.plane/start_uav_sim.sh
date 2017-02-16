#!/bin/bash

# RUN on the GCS to simulate vehicle movement

# cd /home/odroid/ardupilot/ArduCopter
cd ${HOME}/ardupilot/ArduCopter

# sim_vehicle.py -C --mav20 --baudrate 115200 --aircraft=EMSA.plane --state-basedir=/home/odroid/cuav/script --console
sim_vehicle.py -C --mav20 --baudrate 115200 --console --out=udp:192.168.1.100:14550
