# Setup
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

run models based on tags inside the dbt_project.yml file
```sh
dbt run -m tag:hub
```

Produce the documentation including the data lineage graph and host it locally
```sh
dbt docs generate
dbt docs serve
```
