#!/bin/bash

export FAKE_CAMERA=1

while [ $(date +%s) -lt 1469439272 ]; do
    sleep 2
done

mavproxy.py --mav20 --baudrate 115200 --master=udp:127.0.0.1:14750 \
			--aircraft=EMSA.plane \
			--state-basedir=${HOME}/EMSA/cuav/script \
            --cmd="script ${HOME}/EMSA/cuav/script/EMSA.plane/$1"
