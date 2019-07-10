## Setup the chalice env
```sh
python -m venv venvchalice
python -m pip install --upgrade pip
pip install awscli boto chalice httpie jsonschema #httpie (REST) & jsonschema is optional
```

Create new project
```sh
chalice new-project projectname #Creates new project

```


Deploy lambda function with chalice 
```sh
chalice deploy --no-autogen-policy #Using a custom policy is optional

```

