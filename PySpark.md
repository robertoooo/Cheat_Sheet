## Transforming RDD
* **map:** Transform a set of datda given a function, one-to-one relationship. The new RDD will have just as many entries as the original RDD.
* **flatmap:** Similar to map, but has the capability to produce or reduce values. 
* **filter:** 
distinct
sample
union, intersection



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

