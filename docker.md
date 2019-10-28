### Basic docker commands
```powershell
docker pull ubuntu

docker images #list all images

docker ps -a #-a: all 

docker image build -t imagename:1.0 . #Builds an image from a dockerfile

docker run -ti imagename:tag  #Builds and run the container 
  -t #tty 
  -i #interactive
  -p 8080:8080 #expose a port to the host fron the container

docker exec -ti [container-id] bash #Enter already running container with bash 
```

# Dockerfile
A textfile that contains the necessary commands to assemble an image

### Example of a dockerfile
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

### Commands
```Dockerfile
ADD Copy files from a source on the host to the container’s own filesystem at the set destination
CMD Execute a specific command within the container
ENTRYPOINT Set a default application to be used every time a container is created with the image.
ENV Set environment variables
EXPOSE Expose a specific port to enable networking between the container and the outside world.
FROM Define the base image used to start the build process.
MAINTAINER Define the full name and email address of the image creator
RUN Centra executing directive for Dockerfiles
USER Set the UID (the username) that will run the container
VOLUME Enable access from the container to a directory on the host machine.
WORKDIR Set the path where the command, defined with CMD, is to be executed.
```




