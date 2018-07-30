FROM python:3.7

RUN apt-get update --fix-missing && \
    apt-get install -y autoconf g++ wget bzip2 ca-certificates curl git nano iputils-ping nano procps supervisor nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /home/requirements.txt

RUN pip install -r /home/requirements.txt


COPY supervisord.conf /home/supervisord.conf

COPY app /home/app



ENTRYPOINT ["supervisord","-c","/home/supervisord.conf"]
