FROM python:3.8-buster

RUN apt-get update -y
RUN apt-get install python3-pip -y

WORKDIR /project 
COPY requirements.txt requirements.txt
COPY flaskapp flaskapp

RUN pip3 install -r requirements.txt
WORKDIR /project/flaskapp

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app", "--workers=3"]