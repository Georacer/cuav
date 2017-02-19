#!/bin/bash

export FAKE_CAMERA=1

while [ $(date +%s) -lt 1469439272 ]; do
    sleep 2
done

mavproxy.py --mav20 --baudrate 115200 --master=udp:192.168.1.100:14550 --aircraft=EMSA.plane --state-basedir=${HOME}/EMSA/cuav/script
