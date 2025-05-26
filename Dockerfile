FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
    python3 build-essential clisp fpc gawk gccgo ghc git golang lua5.2 mono-mcs ocaml openjdk-11-jdk perl python2.7 racket rake valac \
    python3-pip \
    socat \
    libseccomp2 \
    unzip \
    make \
    wget

# copy all files into container and retain file structure
COPY ./ / 

RUN chmod 555 /src/server.py
RUN chmod 555 /run.sh
RUN wget https://github.com/quark-zju/lrun/archive/refs/tags/v1.2.1.zip
RUN unzip v1.2.1.zip
RUN cd v1.2.1
RUN make install
RUN gpasswd -a $USER lrun 
RUN cd ..
RUN make install 
RUN ljudge --check

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/run.sh,stderr