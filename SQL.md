# Azure SQL Database Monitoring
```sql
SELECT @@VERSION --Check the version that you deployed
SELECT SERVERPROPERTY('EngineEdition'); --Check the type of deployment

-- Check databases and the system objects
SELECT * FROM sys.databases;
SELECT * FROM sys.objects;

SELECT * FROM sys.dm_os_schedulers where STATUS = 'VISIBLE ONLINE'; -- View the schedulers

SELECT * FROM sys.dm_os_job_object; -- See resources available 
SELECT * FROM sys.dm_user_db_resource_governance; -- See Deployment tier and Service Level Objective (SLO)

SELECT * FROM sys.dm_exec_requests; --List of active requests


```

# Basic SQL

```sql
SELECT * FROM tbl -- Selects all columns from a table
SELECT DISTINCT column FROM tbl -- Selects all distinct values from a column
-- All the unique values

SELECT columns FROM tbl WHERE column = something
SELECT COUNT(*) FROM tbl -- Gives the amount of rows in tbl

SELECT * FROM tbl LIMIT 5 -- Outputs the first 5 rows
SELECT * FROM tbl ORDER BY column ASC/DESC -- Order the rows, possible to sort multiple columns

```

BETWEEN, IN and LIKE
```sql
SELECT column1, column2 FROM tbl WHERE column1 BETWEEN low AND high 
-- possible to use NOT also to invert and citation for strings and date


SELECT column1 FROM tbl WHERE column1 IN (1,4,23);
-- Filter out specific rows from the column


SELECT column1 FROM tbl WHERE column1 LIKE 'nam%'
-- %: matching any sequence of characters
-- _: matching any single character
-- ILIKE for case insensitivity
```

GROUP BY
```sql
SELECT column1, AVG(column2)
FROM tbl
GROUP BY column1
-- Segments column1 by class and presents the avg of column 2
```

The HAVING clause sets the confition for group rows created by the GROUP BY clause after the GROUP BY clause applies while the WHERE clause sets the condition for individual rows before GROUP BY clause applies.
```sql
SELECT column1, COUNT(column2)
FROM tbl
GROUP BY column1
HAVING COUNT(column2) > 300;
```

