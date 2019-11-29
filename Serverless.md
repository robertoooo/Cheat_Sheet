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

#### Create and deploy a serverless service
```sh
sls create --template aws-python --path hellow-world-python
sls deploy -v #v:verbose
```
