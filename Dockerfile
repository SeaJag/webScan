FROM vulnerables/web-dvwa

ADD . /webscan/

WORKDIR /webscan

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip

RUN pip3 install -r requirements.txt