# Basic dotnet commands
See the version and create some components
```sh
dotnet --info #shows the versions installed
dotnet new sln #creates a new solution (sln) file
dotnet new classlib -n Domain #creates a new class library
dotnet new webapi -n API #Creates an ASP.NET Core Web API
```
### Add dependencies and references
Add projects to the sln file
```sh
dotnet sln list #see current projects in our sln file
dotnet sln add nameofproject #add project (dependencies) to the sln file
```
Add references to the underlying classes
```sh
dotnet add reference ../Domain/ 
```

### Run the .NET project output 
Runs the API project 
```sh
dotnet run -p API/
dotnet watch run
```

### Install all dependencies
```sh
dotnet restore #restores dependencies specified in a .NET project
``` 

