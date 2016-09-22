# docker_webpy_simplest

## Usage:

clone the whole directory into your server


`git clone git@github.com:mobilestack/docker_webpy_simplest.git webpy_server`


build your docker image, from d docker file and give it a tag name, and specify the location

`docker build -f ./webpy_server/Dockerfile -t webpy_server_image .`

run your docker container from one of these methods:

 a) with name to the container

`docker run --name simplest_webpy -p 80:80 -i -t webpy_server_image`

 b) or run it in background

`docker run -d -p 80:80 -i -t webpy_server_image`

 c) or if you do not sepecify CMD in Dockerfile, you can do it later when you run your docker container

`docker run -p 8080:8080 -it no_CMD_in_Dockerfile_image python /webpy_server/index.py`

 d) or run it from another port, as long as you have changed it and committed the image

`docker commit --change='CMD []' -c "EXPOSE 80" f319 no_run_image_80:v0`


`docker run -d -p 80:80 -it webpy_server_image:v2 python /webpy_server/index.py 80`

