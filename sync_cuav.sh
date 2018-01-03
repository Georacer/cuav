#!/bin/sh

# synch changes for workstation to odroid and re-build it

rsync -avzh --delete --progress ${HOME}/EMSA/MAVProxy/ ucandrone@192.168.1.100:/home/ucandrone/EMSA/MAVProxy
rsync -avzh --delete --progress ${HOME}/EMSA/cuav/ ucandrone@192.168.1.100:/home/ucandrone/EMSA/cuav
rsync -avzh --delete --exclude ${HOME}/catkin_ws/src/emsa-ros/machine_camera/flycapture --progress /home/george/catkin_ws/src/emsa-ros/ ucandrone@192.168.1.100:/home/ucandrone/catkin_ws/src

ssh ucandrone@192.168.1.100 'cd ~/EMSA/MAVProxy; ./update_installation.sh'
ssh ucandrone@192.168.1.100 'cd ~/EMSA/cuav; ./update_installation.sh'
echo 'Done upating'