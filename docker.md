## Basic docker commands
```powershell
docker pull ubuntu

docker images #list all images

docker ps #View all active containers 
  -a #all 
  -q #quiet, only displys numeric IDs.

docker image build -t imagename:1.0 . #Builds an image from a dockerfile

docker run -ti imagename:tag  #Builds and run the container interactive
  -t #tty 
  -i #interactive
  -p 8080:8080 #expose a port to the host fron the container
  
docker run -d -p 5000:5000 flask-tutorial #Builds and run the container in the bakground 

docker exec -ti [container-id] bash #Enter already running container with bash 
```

### Docker Build
```powershell
docker build . #Builds a dockerimage based on the dockerfile

### Docker Monitoring
```Dockerfile
docker logs [container-ID] #Fetch stdout/stderr of the docker container
docker service logs #Fetch stdout/stderr about all the containers related to the service
docker inspect <containerNameOrId> #Return low-level information on Docker objects

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




# Push an Image into Amazon ECR with Docker
```powershell
aws ecr get-login --region eu-west-1 > text.txt #Get the ecr credentials
docker login -u AWS https://aws_account_id.dkr.ecr.eu-west-1.amazonaws.com #Login to ECR with docker
aws ecr create-repository --repository-name nameofrep #Create new repository
docker tag centos:6.6 aws_account_id.dkr.ecr.eu-west-1.amazonaws.com/centos:6.6 #Rename the image to the ECR repository
docker push aws_account_id.dkr.ecr.eu-west-1.amazonaws.com/centos:6.6 #Push the image to ECR

```

### Delete image or repository 
```powershell
aws ecr batch-delete-image --repository-name centos --image-ids imageTag=6.6 #Delete Image
aws ecr delete-repository --repository-name centos #Delete Repository
```
Source: https://blog.dbi-services.com/how-to-push-an-image-into-amazon-ecr-with-docker/


# Create ECS Cluster
```powershell
aws ecs create-cluster --cluster-name name-of-cluster #Create a cluster in ECS

#Cloudwatch log group, important to monitor fargate containers
aws logs create-log-group --log-group-name mythicalmysfits-logs #Create new log group in cloudwatch



```
