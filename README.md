#Pyload Clipboard Monitor (for linux)

##requirements
xclip
```
apt-get install -y xclip git python-pip
```

##Install

```
git clone ...
cd pcm
pip install -r requirements.txt
pip install .
```

##RUN
```
python ~/pcm/pcm/pcm.py -a pyload_server_ip_address -P pyload_server_port -u pyload_username -p password
```

```
docker run -ti --rm --name pcm --cpuset 0 --memory 32mb -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix:0.0 francois/pcm:latest -a pyload_server_ip_address -P pyload_server_port -u pyload_username -p password
```

#TODO:
- Tests for pretty much everthing
- Add a method to set a proper package name
- Find a way to packages in the collector rather than directly in queue
- Add a pop-up handler that would :
	* inform a link has been capture
	* inform if the link has been added or is offline...
