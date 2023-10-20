# python_API

git clone the repo and run this in the terminal



```python
source venv/bin/activate < to activate virtual environment>

pip install -r requirements.txt
```

#### Starting the server 

```python
uvicorn blog.main:app --reload
```

### 1. The GET Method

A simple GET request
  
```python
<!-- A simple GET request -->
@app.get("/")
def index_():
    return {"message": "Hello World"}

<!-- A simple GET with path parameter request -->
@app.get("/about")
def about():
    return {"data": "about page"}

<!-- A simple GET with id parameter request -->

@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}
```

### use of pydantic for data validation    
Dococumentaion of Pydantic [https://docs.pydantic.dev/latest/](https://docs.pydantic.dev/latest/)

#### How to use pydantic
 ```python
from pydantic import BaseModel

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]
 ```


 ## Creating a CRUD operation and connectiong with a database 
 ### using  SQLAlchemy

1. Create a database.py file 
- we import creat engine and create engine
2. Declear a mapping
3. Using the database
    Model and tables

    - creat a model and Declare a Mapping¶


full documentaiton on that [https://docs.sqlalchemy.org/en/20/orm/quickstart.html#create-an-engine](https://docs.sqlalchemy.org/en/20/orm/quickstart.html#create-an-engine)


### Create the SQLAlchemy parts¶
ORMs -> object-relational mapping
is used to map objects into the database field 

1. 1st we will use an in-memory-only SQLite database. To connect we use create_engine():
2. Then we qlalchemy.ext.declarativ and extend the base 
3. last we create the sessionmaker
   
### Storing blog into the database


### Responce Model

You can declare the type used for the response by annotating the path operation function return type.

full documentaiton on that [Responce Model](https://fastapi.tiangolo.com/tutorial/response-model/)

### Creating new user

same as posting a new blog, we create a new fucntion at the main file
creat a new schema and the models.User in the model file to create a new database

#### Tables and models 

### Storing blogs to the database

define the db in create_blog function
