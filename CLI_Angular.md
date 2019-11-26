### Angluar CLI Cheat Sheet

```shell
ng new angular-tour-of-heroes   #Opens a new project

ng serve --open                 #Builds the app, starts the development server, watches the source files, and rebuilds the app as you make changes
	--open                      #Flag that opens a browser to http://localhost:4200**
ng serve --prod --host 0.0.0.0  #Open to the whole network and in production mode 

ng generate component heroes    #Generate a new component named heroes**

ng generate service hero        #Generates skeleton HeroService class**

ng generate component messages  #Generates a MessageComponent in Appmodule**

ng generate service message     #Generates skeleton**
	
code FILE                       #Opens VS with the file you specify**

ii .                            #Opens current folder with GUI (Invoke Item)**


ng generate module app-routing --flat --module=app	    #Generate a new module app-routing
    --flat                      #puts the file in src/app instead of its own root folder
    --moduele=app               #tells the CLI to register it in the imports array of the AppModule
    
```

**Initialize existing project (git).**
```shell
npm install
npm start/serve 
npm install @angular/cli@x.x.x #Installs the x.x.x version of angular, leave empty for latest
```

**Create a project build**
```shell
ng build 		
  --aot #Build using Ahead of Time compilation (default=false)
  
ng version #see angular version
```
