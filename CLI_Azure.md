Install the Azure CLI
```sh
py -m venv venv
venv\Scirpts\activate
py -m pip install --upgrade pip
pip install azure-cli

az login          #Login to Azure through CLI
az account list   #List the account subscription and tenant id
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
