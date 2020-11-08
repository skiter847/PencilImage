FROM python:3
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update
RUN apt-get -y upgrade
RUN apt install -y python-opencv
RUN pip install -r requirements.txt
COPY . /code/
