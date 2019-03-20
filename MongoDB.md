# Python with MongoClient
Database - Collection - Document - Field
A databas can contain multiple collections which can contain multiple document. 
Each document can contain muliple fields with more nested fields.

### Create a MongoClient against the running mongod instance

```python
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
```

### Accessing a Database
With a single instance of MongoDB, we can use multiple independent databases. 
Using PyMongo, we can access databases via attribute style accss on MongoClientInstancs.

```python
mydb = client.test_database_1
mydb = client['test_database_1']
```


### Accessing a Collection 
A collection is a group of documents stored in MongoDB. It is eq to a table in a RDBMS.
We can access a collection in PyMongo the same as we access a database

```python
my_collection = mydb.test-database-1
my_collection = mydb['test-database-1']
```
### BSON
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed to be lightweight, traverable, and efficient.
BSON, like JSON, supports the embedding of objects and arrays within other objects and arrays.

### Document Insert
Use the **insert()** method to insert a document into the collection
```python
import datetime
myrecord = {"author": "Duke",
          "title" : "PyMongo 101",
          "tags" : ["MongoDB", "PyMongo", "Tutorial"],
          "date" : datetime.datetime.utcnow()


record_id = mydb.mytable.insert(myrecord)
```
At the **insert()**, a special key, **_id** is automatically added 
if the document do not already contain an **_id** key which must be unique across the collectio.


### Querying List of Documents - find()
To get more than a single document as the result of a query we use the **find()** method. 
**find()** returns a Cursor instance, which allows us to iterate over all matching documents.
```python
for post in mydb.mytable.find():
    print(post)
```

We can also pass a document to **find()** to limit the returned results.
```python
for post in mydb.mytable.find({"author": "Adja"}):
``` 

### count() & drop() & sort() & Range
**count()** when we just want to know how many documents match a query
**drop()** when we want to delete documents from the collection.
**sort()** sorts the result on a key name

```python
mydb.posts.count() #Counts all the documents that match the query, in this case all documents in collection posts.
mydb.posts.drop() #Removes all the documents in the collection posts.
``` 

Let's perform a query where we limit results to posts older than a certain date
```python
for post in mydb.mytable.find({"date": {"$lt": datetime.datetime(2015, 12, 1)}}).sort("author"):
    print (post)
```
Where "$lt": means lower then.  

### replace_one()
Replace a document based on a field name
```python
# replace one of the employee data whose name is Mr.Shaurya 
result = collection.replace_one( 
        {"name":"Mr.Shaurya"}, 
        { 
                "name":"Mr.GfG", 
                "eid":45, 
                "location":"noida"
                  
                } 
        ) 
```

---

## Update Specific Fields of documents
Replace is used to replace a whole document, when using replace we must specify all the fields.
Update can be used for the same reasen, however update also enables us to replace specific fields inside a document.

### Replacing field values of a document using the $set operator
The *$set* operator will override the old value of a specific field.

```python
db.customers.update(
{"firstname": "Max"}, #Finding the first document with the fieldname "firstname" and the value "Max"
  {
    $set: {
      "lastname": "Maier"
      "address.street" : "another street"
    }
  },
{"multi": true} #Set this to update specific fields of multiple documents
} 
```

#### Increment numeric field values of document using the $inc operator
For numerical values it is possible to modify the value regarding their old value.

[Source](https://specify.io/how-tos/mongodb-update-documents)

