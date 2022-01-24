# Setup Azure Datalake connection using access key and secrets
Setup Variables
```py
scope_name = ""
storage_account_access_key_name = ""
storage_account_name = ""
source_container_name = ""
```

Direct connection 
```py
storatge_url = f"fs.azure.account.key.{storage_account_name}.dfs.core.windows.net"
spark.conf.set(storatge_url, dbutils.secrets.get(scope="scope_name",key="storage_account_access_key_name"))
spark.conf.set(storage_account_name,storage_account_access_key_name)
datalake_url = f"abfss://{source_container_name}@{storage_account_name}.dfs.core.windows.net"
```


Mounting storage to Databricks 
```py
storageAccountName = "storageaccountname"
source_container_name = "container-name"
storage_account_access_key_name = "access-key"
scope_name = "key_vault_name"
storageAccountAccessKey = dbutils.secrets.get(scope=scope_name,key=storage_account_access_key_name)
 
try:
  dbutils.fs.mount(
    source = f"wasbs://{source_container_name}@{storageAccountName}.blob.core.windows.net", #Blob
    source = f"abfss://{source_container_name}@{storageAccountName}.dfs.core.windows.net/", #Datalake
    mount_point = f"/mnt/filestore/{source_container_name}/",
    extra_configs = {'fs.azure.account.key.' + storageAccountName + '.blob.core.windows.net': storageAccountAccessKey}
  )
except Exception as e:
  print(e)

```
Note access keys are not an option on ADLS whereas they can be used for normal blob containers without HNS enabled.

Unmounting storage to Databricks
```py
dbutils.fs.unmount("/mnt/path/to/folder")
```


# Create Delta Table using the Delta Table Builder Class
```py
from delta.tables import *
deltatabletest = DeltaTable.createOrReplace(spark).tableName(<table_name>) #Creates an object of the  DeltaTableBuilder class
deltatabletest.addColumn(<column name>, <column type>, comment=<>) # Add columns to the deltatablebuilder object 
deltatabletest.location(<path>).execute() # Execute the deltatablebuilder object and stores the table in path
```

# Merge Delta Table using the Delta Merge Builder Class


# Read and Writestream
Readstream using autoloader 
```py
loadloc = f"abfss://{container}@{storage_account}.dfs.core.windows.net/{endpoint}"

df_schema = spark.read.parquet(loadloc).schema #When reading parquet files

df = (spark.readStream.format("cloudFiles")
  .option("cloudFiles.format", "parquet")
  .option("mergeSchema", "true")
  .schema(df_schema)
  .load(loadloc))
```

Writestream
```py

loadloc = f"abfss://{container}@{storage_account}.dfs.core.windows.net/{endpoint}"

df_schema = spark.read.parquet(loadloc).schema

df = (spark.readStream.format("cloudFiles")
  .option("cloudFiles.format", "parquet")
  .option("mergeSchema", "true")
  .schema(df_schema)
  .load(loadloc))

```

Foreachbatch function
```py

def mergetoDF(microdf, batchId):
  microdf.createOrReplaceTempView('microbatch') #Creates a temporary view of the dataframe microbatch
  
  df_microbatch = sqlContext.sql(
  """ SELECT * FROM microbatch """
  
  #And then a merge function or similar to have a return from the function
  
```

# Create, Delete a table + metadata
Create a database
```sql
CREATE DATABASE IF NOT EXISTS database_name;
USE database_name;
```

Remove the files from blob
```py
dbutils.fs.rm(f"abfss://{container}@{storage_account}.dfs.core.windows.net/{endpoint}", True) #Deleteing recursive 
```
Delete the metadata, the table reference from databricks
```sql
DROP TABLE IF EXISTS database.table_name
```


# Databricks + Datafactory
Use this in the notebook to return a value to the datafactory
```py
dbutils.notebook.exit(myReturnValueGoesHere)
dbutils.notebook.exit('{"hello": {"some": {"object": "value"}}}')
```
And this inside the datafactory to read the output
```py
@activity('RunNotebookActivityName').output.runOutput
@activity('RunNotebookActivityName').output.runOutput.hello.some.object
```
