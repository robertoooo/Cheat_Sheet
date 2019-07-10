## Setup the chalice env
```py
python -m venv venvchalice
python -m pip install --upgrade pip
pip install awscli boto chalice httpie jsonschema #httpie (REST) & jsonschema is optional
```


Deploy lambda function with chalice 
```py
chalice deploy --no-autogen-policy #Using a custom policy is optional

```

