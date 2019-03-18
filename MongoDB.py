# Python with MongoClient

### Create a MongoClient against the running mongod instance

```py
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
```

### Accessing a Database
With a single instance of MongoDB, we can use multiple independent databases. 
Using PyMongo, we can access databases via attribute style accss on MongoClientInstancs.

```py
mydb = client.test_database_1
mydb = client['test_database_1']
```


### Accessing a Collection 
A collection is a group of documents stored in MongoDB. It is eq to a table in a RDBMS.
We can access a collection in PyMongo the same as we access a database

```py
my_collection = mydb.test-database-1
my_collection = mydb['test-database-1']
```
### BSON
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed to be lightweight, traverable, and efficient.
BSON, like JSON, supports the embedding of objects and arrays within other objects and arrays.

### Document Insert
Use the **insert()** method to insert a document into the collection
```py
import datetime
myrecord = {"author": "Duke",
          "title" : "PyMongo 101",
          "tags" : ["MongoDB", "PyMongo", "Tutorial"],
          "date" : datetime.datetime.utcnow()


record_id = mydb.mytable.insert(myrecord)
```
At the **insert()**, a special key, **_id** is automatically added 
if the document do not already contain an **_id** key which must be unique across the collectio.




