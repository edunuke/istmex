FROM debian:stretch-slim
LABEL maintainer="eduardo.denadai@gmail.com"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y autoconf g++ wget bzip2 ca-certificates curl git nano iputils-ping nano procps supervisor && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc


COPY requirements.txt /home/requirements.txt

RUN pip install -r /home/requirements.txt

COPY supervisord.conf /home/supervisord.conf

COPY app /home/app

EXPOSE 8000 9001 18443 5000

ENTRYPOINT ["supervisord","-c","/home/supervisord.conf"]



