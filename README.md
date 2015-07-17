Pyload Clipboard Monitor (for linux)

#requirements
xclip
```
apt-get install -y xclip git python-pip
```

#Install

```
git clone ...
cd pcm
pip install -r requirements.txt
pip install .
```

#RUN
```
python ~/pcm/pcm/pcm.py -a pyload_server_ip_address -P pyload_server_port -u pyload_username -p password
```

```
docker run -ti --rm --name pcm --cpuset 0 --memory 32mb -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix:0.0 francois/pcm:latest -a pyload_server_ip_address -P pyload_server_port -u pyload_username -p password
```
