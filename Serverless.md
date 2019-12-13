# Installing the Serverless Framework 
First install Node.js
```sh
npm install -g serverless #Installs Serverless Framework
serverless --version #See if the framework is installed

sls plugin install -n serverless-python-requirements        #Enables installing libaries

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
Serverless .yml file 
```yml
provider:
  name: aws
  
  runtime: python2.7
  profile: serverless-admin #Or any other role that you want to specify
  region: eu-west-1
  memorySize: 256 #The standard for the lambda if not specified on specific functinos
  timeout: 6
  
  iamRoleStatements:
    - Effect: "Allow"
      Action:
        - "lambda:*"
      Resource:
        - "*"
        
   environment: #Put env variables for all functions, also possible to put in "functinos"
    variable1: value1
    FIRST_NAME: "ROBERT"
  
  
functions:
  hello-short-timeout:
    handler: handler.hello
    memorySize: 128
    timeout: 3
  hello-long-timeout:
    handler: handler.hello
    memorySize: 256
    timeout: 6
    environment: #Put env variables for all functions, also possible to put in "functinos"
      FIRST_NAME: "Not_ROBERT"
```

### Environmental Variable 
An S3 bucket 
```yml

custom:
  bucket: stephane-s3-thumbnail-generator
  pythonRequirements:
    dockersizePip: true

functions:
  s3-thumbnail-generator:
    handler: handler.s3_thumbnail-generator
    events:
      - s3:
        bucket: ${self:custom.bucket}         #Env variable pointing to slef (this document) and then custom.bucket name
        event: s3:ObjectCreated:*             #Triggered when an object is created
        rules:
          - suffix: .png                      #With the rule that the file must end with .png

```

### Plugins for python to install all dependencies in the requirements.txt
This will install all the dependencies that is placed in the file requirements.txt in the root folder of the service.
```yml
plugins:
  - serverless-python-requirements
```


### Structure of a .yml file
```yml
nested-value-pair:
  name : Robert
  family: Betto
  address-multi-line string: | 
    Hejvägen 1
    Stockholm

product-list:
  - price: 10
  - name: orange
  - description: fruit
comment: > 
  This is a long 
  comment, will be 
  represented as 
  one line
  
  
  

```
