# ***** mentor_flask *****


### Install Flask and set it to development mode
```sh
pip install flask
```


### Set the Environmental Variables and run flask
```sh
$env:FLASK_APP = "main.py" **#Do this in the app folder & in the virtual env**  
$env:FLASK_ENV = "development" **#Dev mode makes server update changes instantly instead of restarting the server every time**  
python -m flaskr run  
```

## Reference
[Flask Install](http://flask.pocoo.org/docs/1.0/installation/)

[Flask Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/)


### flask setup 
```py
from flask import Flask, request
from flask_restful import Resource, Api
import json
from flask_cors import CORS, cross_origin
from flask_ssl import *


app = Flask(__name__)
CORS(app)
api = Api(app)

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':2, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

class HR(Resource):
    def get(self):
        return {'data': (data)} 
    
class IT(Resource):
    def get(self):
        return {'data': (it)} 


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(HR, '/hr') # Route_2
api.add_resource(IT, '/it') # Route_3


if __name__ == '__main__':
     app.run(ssl_context='adhoc') #Enables HTTPS instead of HTTP
```
