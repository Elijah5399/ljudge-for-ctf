FROM kyungw00k/lrun:1.1.4

LABEL maintainer Kyungwook Park <parksama@gmail.com>

ENV LJUDGE_VERSION=0.6.1

# INSTALL LJUDGE BINARY
# THIS DOESNT WORK
RUN wget "https://github.com/quark-zju/ljudge/releases/download/v0.6.1/ljudge_0.6.1_amd64.deb" && \
    dpkg -i "ljudge_0.6.1_amd64.deb" && \
    rm -f "ljudge_0.6.1_amd64.deb"

CMD ["/usr/bin/ljudge"]