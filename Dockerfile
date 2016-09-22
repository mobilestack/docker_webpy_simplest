############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Tony 


# Update the sources list
RUN apt-get update && apt-get install -y \
    tar git curl nano wget dialog net-tools build-essential \
    python python-dev python-distribute python-pip

# Copy the application folder inside the container
ADD /webpy_server /webpy_server

# Get pip to download and install requirements:
RUN pip install -r /webpy_server/requirements.txt

# Expose ports
EXPOSE 80

# Set the default directory where CMD will execute
#WORKDIR /webpy_server

# Set the default command to execute    
# when creating a new container
#CMD python index.py

