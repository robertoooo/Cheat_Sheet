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

