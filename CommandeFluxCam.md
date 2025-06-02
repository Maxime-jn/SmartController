rpicam-vid --list-cameras


docker run --name rtsp3 -it --network=host --privileged --tmpfs /dev/shm:exec -v $PWD/mediamtx.yml:/mediamtx.yml -v /run/udev:/run/udev:ro  bluenviron/mediamtx:latest-rpi


ln -snf /sbin/ldconfig /usr/sbin/ldconfig


docker exec -it rtsp-orig bash


docker exec -it rtsp3 bash


docker ps



dans vlc ou lecteur :

rtsp://10.5.57.116:8554/mycam
