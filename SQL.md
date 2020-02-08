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

