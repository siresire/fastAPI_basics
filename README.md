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

### Create the SQLAlchemy parts¶
ORMs -> object-relational mapping
is used to map objects into the database field 

1. 1st we will use an in-memory-only SQLite database. To connect we use create_engine():
2. Then we qlalchemy.ext.declarativ and extend the base 
3. last we create the sessionmaker

#### Tables and models 

### Storing blogs to the database

