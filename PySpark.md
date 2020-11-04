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

# Reading Data
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





# PySpark
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

