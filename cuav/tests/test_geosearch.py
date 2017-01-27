#!/bin/sh

geosearch.py --directory /media/Data/cuav_test_dataset_2016/OBC2016/CanberraUAV/camera/raw \
            --mission /media/Data/cuav_test_dataset_2016/OBC2016/CanberraUAV/way.txt \
            --mavlog /media/Data/cuav_test_dataset_2016/OBC2016/CanberraUAV/flight.tlog \
            --target=-27.358630,151.239908,0 \
            --flag=-27.358630,151.239908,barrell --flag=-27.358100,151.240624,barrell \
            --service=MicrosoftSat \
            --view \
            --lens=4 \
            --sensorwidth=5