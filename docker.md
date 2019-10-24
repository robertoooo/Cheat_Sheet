### Basic docker commands
```sh
docker pull ubuntu

docker images #list all images

docker ps -a #-a: all 

docker image build -t imagename:1.0 . #Builds an image from a dockerfile

docker run -ti imagename:tag  #Builds and run the container


docker exec -it 72ca2488b353 bash #Enter already running container with bash 
```


#### Example of a dockerfile
```Dockerfile
FROM ubuntu:16.04
MAINTAINER Robert robert.yousif@scania.com
COPY . /app
WORKDIR /app
RUN apt-get update 
RUN apt-get -y install python
RUN apt-get -y install python-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
```


