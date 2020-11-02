Install the Azure CLI
```sh
py -m venv venv
venv\Scirpts\activate
py -m pip install --upgrade pip
pip install azure-cli

az login          #Login to Azure through CLI
az account list   #List the account subscription and tenant id
```

Gets the details for the currently logged-in user.
```sh
az ad signed-in-user show
```



Create a resource group
```sh
az group create --location westeurope --name myResourceGroup
az group list #List all the RG
az group delete --name myResourceGroup

```

Create a Web App 
```sh
az appservice plan create --name name-app-service --resource-group myResourceGroup   #Creates an App Service plan.
az webapp create            #Creates an Azure web app.
az webapp deployment source config --name name-app-service --resource-group myResourceGroup 
    --is-linux #To make it a Linux instance
    #Get the details for available web app deployment profiles.

az webapp deployment source config 
  --name name-app-service 
  --resource-group myResourceGroup 
  --repo-url https://github.com/Azure-Samples/php-docs-hello-world 
  --branch master 
  --manual-integration #Disable automatic sync between source control and web. 
```


# Visual Studio Code
Install the Azure CLI Tools in VSC
Ctrl+Shift+P to access the terminal in VS Code
```sh
azure sign in #Will sign you in through web to your tenant
```

# Create a Service provider
Creates an app-service with a client secret 
```sh
az ad sp create-for-rbac -n "<AppName>" --skip-assignment
```

Set key-vault/app access policy for a service prinicple (app registration) 
```sh
az keyvault set-policy --name "<MyKeyVaultName>" --spn $AZURE_CLIENT_ID --secret-permissions backup delete get list set
```

Set key-vault/app access policy for another azure application (Managed Identity)
```sh
az keyvault set-policy --name "<MyKeyVaultName>" --object-id "<PrincipalId>" --secret-permissions get
```

# Azure SQL
Set the name of your resource group and the name of your Azure SQL logical server (to save typing)
```sh
az configure --defaults group=[resource-group-name] sql-server=[server-name]
```
List all databases on your Azure SQL logical server
```sh
az sql db list

az sql db list | jq '[.[] | {name: .name}]'
```

Get details about the DB
```sh
az sql db show --name [db-name]
az sql db show --name [db-name] | jq '{name: .name, maxSizeBytes: .maxSizeBytes, status: .status}'
```

Get the connection string to a database in a format that *sqlcmd* can use
```sql
az sql db show-connection-string --client sqlcmd --name [db-name]
```

T-SQL statement to create a table named Drivers
```sh
CREATE TABLE Drivers (DriverID int, LastName varchar(255), FirstName varchar(255), OriginCity varchar(255));
GO
```

Run the following T-SQL statement to verify that the Drivers table exists
```sql
SELECT name FROM sys.tables;
GO
```
Add a sample row to the table. *create* operation.
```sql
INSERT INTO Drivers (DriverID, LastName, FirstName, OriginCity) VALUES (123, 'Zirne', 'Laura', 'Springfield');
GO
```
List the *DriverID* and *OriginCity* columns from all rows in the table. *read* operation.
```sql
SELECT DriverID, OriginCity FROM Drivers;
GO
```

Update the city from Springfield to Boston. *update* operation.
```sql
UPDATE Drivers SET OriginCity='Boston' WHERE DriverID=123;
GO
```

Delete the record. *delete* operation.
```sql
DELETE FROM Drivers WHERE DriverID=123;
GO
```
