#!/bin/bash

# export FAKE_CHAMELEON=1 # I think this one is only for testing
while [ $(date +%s) -lt 1469439272 ]; do
    sleep 2
done
mavproxy.py --mav20 --baudrate 115200 --master udp:127.0.0.1:14550 --aircraft=EMSA.plane --state-basedir=/home/odroid/cuav/script
