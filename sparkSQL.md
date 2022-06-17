Select from previous version
```sql
SELECT * FROM STUDENT VERSION AS OF 3
```

Restore table 
```sql
RESTORE TABLE students to VERSION AS OF 8
```

Vacuum table
```sql
VACUUM students RETAIN 0 HOURS
VACUUM students RETAIN 0 HOURS DRY RUN --Test the run without applying it
```

You will need to overwrite some spark settings to enable vacuum with a value less than 168 hours
```sql
SET spark.databricks.delta.retentionDurationCheck.enable = false;
SET spark.databricks.delta.vacuum.logging.enable = true;
```

Review the Table History
```sql
DESCRIBE HISTORY students
```

Create a temporary view from a previous version
```sql
CREATE OR REPLACE TEMP VIEW students AS SELECT * FROM students VERSION AS OF 4
```


Drop database and underlying tables
```sql
DROP DATABASE databasename CASCADE;
```

### Views
Create a temporary view (spark session)
```sql
CREATE OF REPLACE TEMPORARY VIEW temp_delays USING CSV OPTIONS(...)
```
Create a view
```sql
CREATE OR REPLACE VIEW view_delays AS
SELECT * FROM external_table
WHERE column = 'something'
```

Create a global temporary view (cluster based)
```sql
CREATE OR REPLACE GLOBAL TEMPORARY VIEW global_temp_view AS
SELECT * FROM external_table WHERE distance > 1000;
```

CTE (Common Table Expressions)
```sql
WITH(...)
```

### Managed and External tables
Create a database with specified path
```sql
CREATE DATABASE ${da.db_name} LOCATION '${da.paths.working_dir}/${da.db_name}';
USE ${da.db_name};
```

Create a managed table
```sql
CREATE TABLE weather_managed AS
SELECT * 
FROM table1;
```
