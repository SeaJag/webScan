FROM vulnerables/web-dvwa

ADD . /webscan/

WORKDIR /webscan

RUN apt update && \
    apt upgrade -y && \
    apt install -y python3 python3-pip doxygen doxygen-gui doxygen-doc

RUN pip3 install -r requirements.txt