Create virtual env and setup AWS

```sh
python -m venv venv (venvvenvname)
python -m pip install --upgrade pip
pip install awscli
aws --version #Check the version and that it is installed 
```

Setup the credentials that will be located in home folder (~.aws)
```sh
aws configure
aws --profile #Run AWS commands with a specific user
aws s3 ls #See what buckets are available
```


Setup an ES service, setup the env variables ARN_ID & MY_IP
```sh
aws es create-elasticsearch-domain --domain-name "elastic" --elasticsearch-version "6.0" --elasticsearch-cluster-config InstanceType="t2.small.elasticsearch",InstanceCount=1,DedicatedMasterEnabled=false,ZoneAwarenessEnabled=false --ebs-options EBSEnabled=true,VolumeType="gp2",VolumeSize=10 --access-policies "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::"$AWS_ARN_ID":root\"},\"Action\":\"es:*\",\"Resource\":\"arn:aws:es:us-east-1:"$AWS_ARN_ID":domain/elastic/*\"},{\"Sid\":\"\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"*\"},\"Action\":\"es:*\",\"Resource\":\"arn:aws:es:us-east-1:"$AWS_ARN_ID":domain/elastic/*\",\"Condition\":{\"IpAddress\":{\"aws:SourceIp\":[\""$MY_IP_ADDRESS"\"]}}}]}"

```


## Chalice
```sh
chalice new project #Creates a new chalice project

chalice local #Run the app locally
chalice deploy #Deploy the app to a lambda function
```
