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
