FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN python3 -m pip install pip --upgrade
RUN python3 --version
RUN nodejs -v
# RUN mkdir /base
ENV FLASK_APP data/server/server.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV FLASK_DEBUG 1
WORKDIR /
#COPY . /base
RUN pip3 --version
RUN pip3 install flask
VOLUME [ "/data" ]
CMD ["flask", "run"]
