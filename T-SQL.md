# Create user and grant OBJECT permissions

List logins & users
```sql
SELECT * FROM sys.sql_logins; --list logins, must run in master db
SELECT * FROM sys.sysusers --list users in db of choice
```

Create login with password and User 
```sql
CREATE LOGIN login_username WITH password='password';
CREATE USER readonlyuser_1 FROM LOGIN login_username;

```

Grant object permission
```sql
GRANT SELECT ON schema.table TO readonlyuser_1
```

List current Object permissions for all users
```sql
SELECT DISTINCT pr.principal_id, pr.name AS [UserName], pr.type_desc AS [User_or_Role], pr.authentication_type_desc AS [Auth_Type], pe.state_desc,
    pe.permission_name, pe.class_desc, o.[name] AS 'Object' 
    FROM sys.database_principals AS pr 
    JOIN sys.database_permissions AS pe ON pe.grantee_principal_id = pr.principal_id
    LEFT JOIN sys.objects AS o on (o.object_id = pe.major_id) 
```

List what user each login object belongs to
```sql
TBD
```
