# Installing the Serverless Framework 
First install Node.js
```sh
npm install -g serverless #Installs Serverless Framework
serverless --version #See if the framework is installed

```

#### Setup the AWS Credentials
Create a new role called serverless-admiin and get the access key ID and secret access key
```sh
serverless config credentials --provider aws --key XXX --secret YYY --profile serverless-admin
```

## Create and deploy a serverless service
```sh
sls create --template aws-python --path hellow-world-python
sls deploy -v #Deploys a serverless service with the whole stack

sls deploy function -f hello #Deploys a single function from the service

sls remove #Removes the whole stack 
```

#### Invoke function from CLI
```sh
sls invoke -f hello -l #-f:function -l:output logging data

```

#### Monitor the logs
```sh
sls logs -f hello -t #Logs the function hello and tails it
```


# .yml File
```yml
provider:
  name: aws
  runtime: python2.7
  profile: serverless-admin #Or any other role that you want to specify
  region: eu-west-1
  
```
