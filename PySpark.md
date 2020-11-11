# Apache Spark Notebook Basics
Magical Commands: allows us to execute code in languages other then the notebook's default.
```sh
%sh ps | grep 'java'
```

Markdown in a cell:
```sh
%md
# Label 1
Text
```

Run a notebook from another notebook using %run
```sh
%run "./Includes/Another-notebook"
```

## Databricks File System - DBFS
Returns a collection of `MountInfo` objects, one for each mount.
```py
mounts = dbutils.fs.mounts()

for mount in mounts:
  print(mount.mountPoint + " >> " + mount.source)

print("-"*80)
```
### View the contents of a specific mount
#### Using a for loop
```py
files = dbutils.fs.ls("/mnt/training/")

for fileInfo in files:
  print(fileInfo.path)

print("-"*80)
```
#### Using the display command
```py
files = dbutils.fs.ls("/mnt/training/")

display(files)
```

Another magic command that can be used equivalent to the display command
```sh
%fs ls /mnt/training
```
## Set number of partitions
To make sure wide operations don't repartition to 200
```py
partitions = 8
spark.conf.set("spark.sql.shuffle.partitions", str(partitions))
```
Repartition
```py
# Create our initial DataFrame. We can let it infer the 
# schema because the cost for parquet files is really low.
initialDF = (spark.read
  .option("inferSchema", "true") # The default, but not costly w/Parquet
  .parquet(parquetFile)          # Read the data in
  .repartition(partitions)       # From 7 >>> 8 partitions
  .cache()                       # Cache the expensive operation
)
# materialize the cache
initialDF.count()
```

# Reading and Writing Data
## Read CSV
Add another option to use the first line of all files as headers
Print schema directly upon read
inferSchema to infer the data type
```py
csvFile = "/mnt/path/to/file.csv"

tempDF = (spark.read           # The DataFrameReader
   .option("sep", "\t")        # Use tab delimiter (default is comma-separator)
   .option("header", "true")   # Use first line of all files as header
   .option("inferSchema", "true")  # Automatically infer data types
   .csv(csvFile)               # Creates a DataFrame from CSV after reading in the file
   .printSchema()
)
```
Print the structure of the DataFrame and display the data
```py
tempDF.printSchema()
display(tempDF)
```

Declare a Schema
```py
# Required for StructField, StringType, IntegerType, etc.
from pyspark.sql.types import *

csvSchema = StructType([
  StructField("timestamp", StringType(), False),
  StructField("site", StringType(), False),
  StructField("requests", IntegerType(), False)
])
```

Read the data with a specified schema
```py
(spark.read                   # The DataFrameReader
  .option('header', 'true')   # Ignore line #1 - it's a header
  .option('sep', "\t")        # Use tab delimiter (default is comma-separator)
  .schema(csvSchema)          # Use the specified schema
  .csv(csvFile)               # Creates a DataFrame from CSV after reading in the file
  .printSchema()
)
```
Print Number of partitions and records per partition
```py
print("Partitions: " + str(csvDF.rdd.getNumPartitions()) )
printRecordsPerPartition(csvDF)
```

## Read JSON
```py
jsonFile = "dbfs:/mnt/training/wikipedia/edits/snapshot-2016-05-26.json"

wikiEditsDF = (spark.read           # The DataFrameReader
    .option("inferSchema", "true")  # Automatically infer data types & column names
    .json(jsonFile)                 # Creates a DataFrame from JSON after reading in the file
 )
wikiEditsDF.printSchema()
```
Print number of partitions and records per partition
```py
jsonDF = (spark.read
  .schema(jsonSchema)
  .json(jsonFile)    
)
print("Partitions: " + str(jsonDF.rdd.getNumPartitions()))
printRecordsPerPartition(jsonDF)
print("-"*80)
```

## Read Parquet
```py
parquetFile = "/mnt/training/wikipedia/pageviews/pageviews_by_second.parquet/"

DF = (spark.read              # The DataFrameReader
  .parquet(parquetFile)  # Creates a DataFrame from Parquet after reading in the file
)
print(DF) #Python hack to see the data types
```

Print number of partitions and records per partition
```py
parquetDF = spark.read.schema(parquetSchema).parquet(parquetFile)

print("Partitions: " + str(parquetDF.rdd.getNumPartitions()) )
printRecordsPerPartition(parquetDF)
print("-"*80)
```


## Read from a Table/View
After uploading the data or connecting it in the "Data" tab on Databricks we can read in the "table" as a `DataFrame`
```py
pageviewsBySecondsExampleDF = spark.read.table("pageviews_by_second_example_1_tsv")
pageviewsBySecondsExampleDF.printSchema()
```
Print number of partitions and records per partition
```py
print("Partitions: " + str(pageviewsBySecondsExampleDF.rdd.getNumPartitions()))
printRecordsPerPartition(pageviewsBySecondsExampleDF)
print("-"*80)
```

### Temporary views
Tables loaded with spark.read.table() are also accessible through the SQL APIs
```sql
%sql
select * from pageviews_by_second_example_1_tsv limit(5)
```

Take an existing `DataFrame` and register it as a view exposing it as a table to the SQL API
```py
# create a DataFrame from a parquet file
parquetFile2 = "/mnt/training/wikipedia/pagecounts/staging_parquet_en_only_clean/"
parquetDF = spark.read.parquet(parquetFile)

# create a temporary view from the resulting DataFrame
parquetDF.createOrReplaceTempView("parquet_table")
```
And now use the SQL API to reference that same DataFrame as *parquet_table*
```sql
%sql
select * from parquet_table order by requests desc limit(5)
```

## Write Parquet files from `DataFrame`
```py
fileName = userhome + "/pageviews_by_second.parquet"
print("Output location: " + fileName)

(csvDF.write                       # Our DataFrameWriter
  .option("compression", "snappy") # One of none, snappy, gzip, and lzo
  .mode("overwrite")               # Replace existing files
  .parquet(fileName)               # Write DataFrame to Parquet files
)
```
Display the file in the DBFS
```py
display(
  dbutils.fs.ls(fileName)
)
```

# Describe a DataFrame
Number of rows in the Dataset (Aggregate function: triggers a job)
```py
total = DF.count()

print("Record Count: {0:,}".format( total ))
```

## Transformations (does not trigger a job)
Limit the number of records
```py
newDF = DF.limit(n)
```
Transform the data by selecting columns
```py
newDF = DF.select("c1","c2,)
```
Drop columns
```py
newDF = DF.drop("col1")
```
## cache() & persist()
Cache data for better performance. Moves the data into memory of the local executor instead of reading the data from its source.
Cache is just an allias for persist.
```py
(DF
  .cache()         # Mark the DataFrame as cached
  #.unpresist() #Remove the cache by calling unpresist().
) 
```

### distinct() & dropDuplicates()
Returns a new Dataset that contains only the unique rows from this Dataset
```py
distinctDF = (DF                    # Our original DataFrame from spark.read.parquet(..)
  .select("col1")                   # Drop all columns except the "col1" column
  .distinct()                       # Reduce the set of all records to just the distinct column.
)
```

### groupBy()
Group by two column and aggregate another 
```py
schemaDDL = "col1 STRING, col2 STRING, col3 FLOAT, col4 DATE"

sourcePath = "/mnt/path/to/parquet/"

countsDF = (spark.read
  .format("parquet")
  .schema(schemaDDL)
  .load(sourcePath)
  .groupBy("col1", "col2").count()
  .withColumnRenamed("count", "counts")
  .orderBy("col1")
)
```
Group by two columns and aggregate the count
```py
customerCounts = (deltaDF.groupBy("CustomerID", "Country")
  .count()
  .withColumnRenamed("count", "total_orders"))

display(customerCounts)
```

## Actions: show() & display()
`show(..)` is part of core spark - `display(..)` is specific to Databricks notebooks.
show() is ugly - display() is pretty.
```py
DF.show(n=20, truncate=True) #The standard parameters, can be empty
```



# Column Class
Column-level-transformations, such as sorting in a decending order.
```py
sortedDescDF = (pagecountsEnAllDF
  .orderBy( col("requests").desc() )
)  
sortedDescDF.show(10, False) # The top 10 is good enough for now
```

### filter(..) & where(..)
w/SQL Expression
```py
whereDF = (sortedDescDF
  .where( "col1 = 'row'" )
)
whereDF.show(10, False)
```
w/Column
```py
filteredDF = (sortedDescDF
  .filter( col("col1") == "row")
)
filteredDF.show(10, False)
```

Filter Expression
```py
articlesDF = (filteredDF
  .drop("bytes_served")
  .filter( col("article") != "Main_Page")
  .filter( col("article") != "-")
  .filter( col("article").startswith("Special:") == False)
)
articlesDF.show(10, False)
```

## collect() and take(n)
Convert a DataFrame to a list of n rows (Row class).
collect() and take(n) is in short the same basic function.
```py
rows = articlesDF.take(10)
rows = (articlesDF
  .limit(10)           # We only want the first 10 records.
  .collect()           # The action returning all records in the DataFrame
)

```

## Rename a column
Different ways to rename a column
```py
(initialDF
  .select( col("timestamp").alias("capturedAt"), col("site"), col("requests") )
  .printSchema()
)

(initialDF
  .withColumnRenamed("timestamp", "capturedAt")
  .printSchema()
)

(initialDF
  .toDF("capturedAt", "site", "requests")
  .printSchema()
)

```

## Casting timestamp
Renaming a column and cast a unix_timestamp from string
```py
tempA = (initialDF
  .withColumnRenamed("timestamp", "capturedAt")
  .select( col("*"), unix_timestamp( col("capturedAt"), "yyyy-MM-dd HH:mm:ss") )
)
tempA.printSchema()
```

### Selecting month and year from timestamp
Shows the distinct values of what month and year the data was captured.
```py
(pageviewsDF
  .select( month(col("capturedAt")).alias("month"), year(col("capturedAt")).alias("year"))
  .distinct()
  .show()                     
)
``` 

# groupBy() & GroupedData (RelationalGroupedData)
Where GroupedData is the supports many different aggregations.
```py
(pageviewsDF
  .filter("site = 'mobile'")
  .select( sum( col("requests")), count(col("requests")), avg(col("requests")), min(col("requests")), max(col("requests")) )
  .show()
)
          
(pageviewsDF
  .filter("site = 'desktop'")
  .select( sum( col("requests")), count(col("requests")), avg(col("requests")), min(col("requests")), max(col("requests")) )
  .show()
)
```
We can also format the data and rename the column so it is more verbose.
The second argument is the number of decimals.
```py
format_number(sum(col("requests")), 0).alias("sum")
```

# Azure Key Vault
First we need to Link Azure Databricks to the Key Vault:
To access the Secrets UI add `secrets/createScope` after the `?o=XXXXXXXXXX` when you are inside the Databricks GUI.

### List secrets scope
```py
dbutils.secrets.listScopes()
```
### List secrets within a specific scope
```py
dbutils.secrets.list("name-of-scope-created-in-secrets-createScope-above")
```
### Get a secret
This will be printed as [REDACTED]
```py
print(dbutils.secrets.get(scope="students", key="storageread"))
```

# Mount Storage Account, read & write
Mounting the container like a directory, by default, all users within the workspace will have the same privileges to interact with that directory. 
```py
MOUNTPOINT = "/mnt/commonfiles"
# Add the Storage Account, Container, and reference the secret to pass the SAS Token
STORAGE_ACCOUNT = dbutils.secrets.get(scope="students", key="storageaccount")
CONTAINER = "salesdata"
SASTOKEN = dbutils.secrets.get(scope="students", key="storageread")

# Do not change these values
SOURCE = "wasbs://{container}@{storage_acct}.blob.core.windows.net/".format(container=CONTAINER, storage_acct=STORAGE_ACCOUNT)
URI = "fs.azure.sas.{container}.{storage_acct}.blob.core.windows.net".format(container=CONTAINER, storage_acct=STORAGE_ACCOUNT)

try:
  dbutils.fs.mount(
    source=SOURCE,
    mount_point=MOUNTPOINT,
    extra_configs={URI:SASTOKEN})
except Exception as e:
  if "Directory already mounted" in str(e):
    pass # Ignore error if already mounted.
  else:
    raise e
print("Success.")
```

List the files
```py
dbutils.fs.ls(MOUNTPOINT)
```

Read a file from a mounted directory
```py
salesDF = (spark.read
              .option("header", True)
              .option("inferSchema", True)
              .csv(MOUNTPOINT + "/sales.csv"))

display(salesDF)
```

Write to mounted catalog
```py
try:
  sales2004DF.write.mode("overwrite").parquet(MOUNTPOINT + "/sales2004")
except Exception as e:
  print(e)
```

### Cleaning up mounts
```py
if MOUNTPOINT in [mnt.mountPoint for mnt in dbutils.fs.mounts()]:
  dbutils.fs.unmount(MOUNTPOINT)
```

# Writing directly to blob 
```py
CONTAINER = "salesdata"
SASTOKEN = dbutils.secrets.get(scope="students", key="storageread")

# Redefine the source and URI for the new container
SOURCE = "wasbs://{container}@{storage_acct}.blob.core.windows.net/".format(container=CONTAINER, storage_acct=STORAGE_ACCOUNT)
URI = "fs.azure.sas.{container}.{storage_acct}.blob.core.windows.net".format(container=CONTAINER, storage_acct=STORAGE_ACCOUNT)
               
# Set up container SAS
spark.conf.set(URI, SASTOKEN)
```

List the files 
```py
dbutils.fs.ls(SOURCE)
```

Writing to blob directly 
```py
sales2004DF.write.mode("overwrite").parquet(SOURCE + "/sales2004")
```
Deleting file using SAS token
```py
dbutils.fs.rm(SOURCE + "/sales2004", True)
``` 

# DELTA LAKE
Set up relevant paths, input file and the path to the output data
```py
userhome = "dbfs:/user/username"
inputPath = "/mnt/training/online_retail/data-001/data.csv"
DataPath = userhome + "/delta/customer-data/"
```
Read the data into a DataFrame with supplied schema. Partition based on country.
```py
from pyspark.sql.types import StructType, StructField, DoubleType, IntegerType, StringType

inputSchema = StructType([
  StructField("InvoiceNo", IntegerType(), True),
  StructField("StockCode", StringType(), True),
  StructField("Description", StringType(), True),
  StructField("Quantity", IntegerType(), True),
  StructField("InvoiceDate", StringType(), True),
  StructField("UnitPrice", DoubleType(), True),
  StructField("CustomerID", IntegerType(), True),
  StructField("Country", StringType(), True)
])

rawDataDF = (spark.read
  .option("header", "true")
  .schema(inputSchema)
  .csv(inputPath)
)
```
### Write the rawDataDF to Delta Lake 
```py

# write to Delta Lake
rawDataDF.write.mode("overwrite").format("delta").partitionBy("Country").save(DataPath)
```
Query the data dircetly on a directory (Same command)
```py
display(spark.sql("SELECT * FROM delta.`{}` LIMIT 5".format(DataPath)))
display(spark.sql("SELECT * FROM delta.`dbfs:/user/robert.yousif@kpmg.se/delta/customer-data/` LIMIT 5"))
```

### CREATE Table using Delta Lake
CREATE A Table Using Delta Lake, if LOCATION is specified it is considered unmanaged by the metastore. 
```py
spark.sql("""
  DROP TABLE IF EXISTS customer_data_delta2
""")
spark.sql("""
  CREATE TABLE customer_data_delta
  USING DELTA
  LOCATION '{}'
""".format(DataPath))
```

### Metadata
The Schema is stored in `_delta_log` directory shown below:
```py
display(dbutils.fs.ls(DataPath + "/_delta_log"))
```
Display the Metadata
```sql
%sql
DESCRIBE DETAIL customer_data_delta
```

## Append Using Delte Lake 
Read the file and store it in a new dataframe with the same schedule, keep the header.
```py
(newDataDF
  .write
  .format("delta")
  .partitionBy("Country")
  .mode("append")
  .save(DataPath)
)
```

## UPSERT (UPdate & inSERT)
Read JSON file and store in DF
```py
upsertDF = spark.read.format("json").load("/mnt/training/enb/commonfiles/upsert-data.json")
display(upsertDF)
```
Register it as temporary view so this table doesn't persist in DBFS (but possible to use SQL to query)
```py
upsertDF.createOrReplaceTempView("upsert_data")
```
Use the temorary view to inSERT new data and UPdate some previous records
```sql
%sql
MERGE INTO customer_data_delta
USING upsert_data
ON customer_data_delta.InvoiceNo = upsert_data.InvoiceNo
  AND customer_data_delta.StockCode = upsert_data.StockCode
WHEN MATCHED THEN
  UPDATE SET *
WHEN NOT MATCHED
  THEN INSERT *
```
See changes made to that specific customer
```sql
%sql
SELECT * FROM customer_data_delta WHERE CustomerID=20993
```













# PySpark (RDD)
## Transforming RDD
* **map:** Transform a set of datda given a function, one-to-one relationship. The new RDD will have just as many entries as the original RDD.
* **flatmap:** Similar to map, but has the capability to produce or reduce values. 
* **filter:** Trim out information that you do not need.
* **distinct:** Get all the unique values from an RDD.
* **sample:** Take a random sample to experiment with, useful while testing and finding bugs.
* **union, intersection, subtract, cartesian:**  Take two different RDDs and output a single output.

## RDD Actions
* **collect:** Dump out all the values from an RDD
* **count:** Count the values 
* **countByValue:** Count how many times each value occurs (unique values) 
* **take & top:** Sample a few values from the RDD final results
* **reduce:** Lets you write a function that combines all different values for a given key value (Summation/Aggregate)

**Nothing actually happens in your driver program until an action is called!**

---

### key/value RDD
Create a key/value RDD
```py
totalsByAge = rdd.map(lambda x:(x, 1)) #A single entety of two things, a key and a value

```

* reduceByKey(): combine values with the same key using some function. rdd.reduceByKey(lambda x, y:x+y) adds them up 
* groupByKey(): Group values with the same key
* sortByKey(): Sort RDD by key values
* keys(), values(): Create an RDD of just the keys, or just the values

#### SQL-Style Joins on two key/value RDDs
* join, rightOuterJoin, leftOuterJoin, cogroup, subtractByKey

With key/value data, use mapValues() and flatMapValues() if your transformation doesn't affect the keys.
Less computationaly heavy.


# Verify work
```py
expected = 1783138
assert totalArticles == expected, "Expected the total to be " + str(expected) + " but found " + str(totalArticles)
```
If true nothing happens, if false it will give an error and print the text.
