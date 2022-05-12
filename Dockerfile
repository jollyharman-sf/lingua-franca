FROM python:3.6.6

WORKDIR /workdir
ADD ./requirements.txt /workdir/requirements.txt

RUN apt update
RUN apt install openssl ca-certificates wget python3-pip git apt-transport-https ca-certificates -y
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

ADD . /workdir
ENTRYPOINT ["/bin/sh"]
CMD ["./python3 main.py"]