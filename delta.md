# Delta Tables

## Create Hive metastore-based tables
```py
from delta.tables import *
#Creates a hive metastore-based table
DeltaTable.createIfNotExists(spark) \
  .tableName("default.hej") \
  .addColumn("code_nr", "INT") \
  .addColumn("lastName", "STRING", comment = "surname") \
  .execute()
```

```sql
  
CREATE OR REPLACE TABLE default.people10msql (
  id INT,
  firstName STRING COMMENT 'Test',
  middleName STRING,
  lastName STRING,
  gender STRING,
  birthDate TIMESTAMP,
  ssn STRING,
  salary INT
) USING DELTA
```
  
