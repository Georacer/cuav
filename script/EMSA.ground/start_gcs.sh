#!bin/sh

mavproxy.py --baudrate 57600 \
            --aircraft=EMSA.ground \
            --state-basedir=/home/george/EMSA/cuav/script \
            --console \
            --map \
            --cmd="script /home/george/EMSA/cuav/script/EMSA.ground/$1"