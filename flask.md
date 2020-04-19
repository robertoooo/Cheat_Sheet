# ***** mentor_flask *****

## Initilize flask

#### Create new project folder
> mkdir mentor_flask
> cd mentor_flask

#### Init git, add and pull master branch
> git init            
> git remote add origin "Remote URL from above"   
> git pull origin master  #Pull the master branch

#### Insatll and create venv (DO THIS BEFORE INSTALLING ANYTHING WITH PIP)
> python -m venv venv (venvvenvname)

> pip install virtualenv

#### Activate venv (In Powershell), install venv if needed
> .\venv\Scripts\activate
> pip install -r requirements.txt **#Install all packages that is needed**
> * pip freeze > requirements.txt **#When installing new packages, export them requirements**
> * deactivate **To deactivate the virtual environment**

#### Install Flask and set it to development mode
> pip install flask



#### Set the Environmental Variables and run flask
> $env:FLASK_APP = "main.py" **#Do this in the app folder & in the virtual env**  
> $env:FLASK_ENV = "development" **#Dev mode makes server update changes instantly instead of restarting the server every time**  
> python -m flaskr run  


## Reference
[Flask Install](http://flask.pocoo.org/docs/1.0/installation/)

[Flask Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/)

