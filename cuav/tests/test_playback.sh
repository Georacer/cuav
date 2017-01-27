#!/bin/sh

[ $# -ge 1 ] || {
    echo "Usage: test_playback.sh <LOGDIR>"
    exit 1
}
logdir="$1"
FDIR="$1"
IDIR="$1/camera/raw"
shift

[ -r "$logdir"/flight.log ] || {
    echo "Invalid log directory - $logdir/flight.tlog not found"
    exit 1
}
[ -d "$logdir"/camera/raw ] || {
    echo "Invalid log directory - $logdir/camera/raw not found"
    exit 1
}

export FAKE_CHAMELEON=1
/home/george/EMSA/cuav/cuav/tests/playback.py $FDIR/flight.tlog --imagedir=$IDIR --speedup=1 & rm -rf OBC2016/logs
mavproxy.py --aircraft OBC2016 --master 127.0.0.1:14550
