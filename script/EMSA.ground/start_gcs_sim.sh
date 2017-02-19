#!bin/sh

mavproxy.py --baudrate 57600 --master=udp:127.0.0.1:14650 \
            --aircraft=EMSA.ground \
            --state-basedir=/home/george/EMSA/cuav/script \
            --console \
            --map \
            --cmd="script ${HOME}/EMSA/cuav/script/EMSA.ground/$1"