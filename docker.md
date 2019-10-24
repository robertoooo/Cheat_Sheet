### Basic docker commands
```sh
docker pull ubuntu

docker images %list all images

docker ps -a #-a: all 

docker image build -t imagename:1.0 . #Builds an image from a dockerfile

docker run -ti imagename:tag  //Builds and run the container


docker exec -it 72ca2488b353 bash #Enter already running container with bash 
```
