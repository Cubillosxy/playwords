FROM python:2.7

MAINTAINER Edwin C
WORKDIR /tmp/

RUN apt-get update
RUN apt-get -y install apt-utils
RUN apt-get update && apt-get install -y \
    vim \
    nano
RUN apt-get install x11-xserver-utils -y
RUN apt-get install python-tk -y
RUN pip install ipython
RUN pip install ipdb
RUN pip install pyinstaller
RUN mkdir /code
WORKDIR /code
ADD . .

CMD ["python", "playenglish.py"]
