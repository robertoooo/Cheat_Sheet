## Setup
Setup a virtual env, install dbt using pip.

Configure profiles
```sh
dbt debug --config-dir      
``` 

Setup dbt project
```sh
dbt init dbtprojectname
```

debug the connection 
```sh
dbt debug
```
## Run models

run models based on tags inside the dbt_project.yml file
```sh
dbt run -m tag:hub
```

## Sources
Create a schema.yml file and add the following
```sh
version: 2

sources:
  - name: nameofsource
    database: nameofdatabase
    schema: nameofschema
    tables:
      - name: tablename1
      - name: tablename2
```
Reference the source tables inside a model
```sh
SELECT * FROM {{ source('nameofsource', 'tablename1') }}
```


## Docs

Produce the documentation including the data lineage graph and host it locally
```sh
dbt docs generate
dbt docs serve
```
