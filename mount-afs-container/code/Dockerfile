FROM python:3.8-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 \
        python3-pip \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /project
COPY service service
RUN pip3 install -r service/requirements.txt
WORKDIR /project/service
RUN python3 setup.py develop

# WORKDIR /project/service

CMD ["python3", "-m", "afs_app"]
