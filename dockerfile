# Use the existing image as base
FROM pintia/ljudge-docker:7469cbb AS app

# FROM pwn.red/jail

# COPY --from=app /usr /usr
# COPY --from=app / /srv 

# setup the binary to run
# COPY ./server.py /srv/app/run

# COPY ./testcases /srv/app/testcases
# RUN chmod +x /srv/app/run

# Optional: switch to root to ensure permission
USER root

RUN apt-get update && apt-get install -y socat

COPY ./ /

RUN chmod 555 /server.py

# Set working directory
WORKDIR /workspace

# Optional: run setup scripts or install packages
# RUN apt-get update && apt-get install -y <your-tools>

# (Optional) Set environment variables
# ENV LANGUAGE=en_US.UTF-8
# ENV TIMEZONE=Asia/Shanghai

# Stay as root for socat, but run the Python script as judger

USER judger 
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:"python3 /server.py",stderr