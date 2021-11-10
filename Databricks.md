# Setup Azure Datalake connection using key
```py
storageurl = "fs.azure.account.key.<SCOPE>.dfs.core.windows.net"
spark.conf.set(storageurl, dbutils.secrets.get(scope="scopename",key="keyname"))

storage_account = "storageaccountname"

```


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
