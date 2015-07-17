# Base docker image
FROM debian:jessie
MAINTAINER François Billant <fbillant@gmail.com>

RUN sed -i.bak 's/jessie main/jessie main contrib non-free/g' /etc/apt/sources.list && \

apt-get update && \
apt-get install -y \
xclip python-pip git

RUN cd /root && \
git clone https://github.com/francois-learnings/pcm.git

RUN cd /root/pcm && \
pip install -r requirements.txt && \
pip install .

ENTRYPOINT ["python /root/pcm/pcm/pcm.py"]
