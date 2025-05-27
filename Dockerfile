FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
    python3 build-essential python3 openjdk-11-jdk \
    python3-pip \
    socat \
    libseccomp2 \
    unzip \
    make \
    wget \
    rake

# copy all files into container and retain file structure
COPY ./ / 

RUN chmod 555 /src/server.py
RUN chmod 555 /run.sh
# RUN wget https://github.com/quark-zju/lrun/archive/refs/tags/v1.2.1.zip
# RUN unzip v1.2.1.zip
WORKDIR /lrun-1.2.1

RUN sed -i 's|#include "utils/|#include "../../src/utils/|g' tools/mirrorfs/mirrorfs.cc
RUN sed -i 's|utils/fs.o|../../src/utils/fs.o|g' tools/mirrorfs/Makefile

RUN make install

RUN sysctl -w debug.exception-trace=0
RUN echo 'debug.exception-trace=0' | tee /etc/sysctl.d/99-disable-trace.conf
RUN useradd ctfuser
RUN mkdir -p /home/ctfuser/.cache/ljudge && chown -R ctfuser:ctfuser /home/ctfuser/.cache

RUN gpasswd -a ctfuser lrun 
WORKDIR /
RUN make install 

USER ctfuser

# ljudge cannot be run if you are not root 
# RUN ljudge --check 

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:"python3 /src/server.py",stderr