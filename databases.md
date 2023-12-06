# Databases for development

## most popular databases

### 1) SQLite
- SQLite is the most widely used database for Python applications due to its simplicity and ease of use. It’s included by default with Python installs as part of the standard library, making it accessible out-of-the-box.

- SQLite stores data in self-contained, compact, and portable database files that can be easily shared. It’s serverless so no configuration is required, and it interacts through simple function calls. sqlite3 module provides a DB-API-compliant interface.

- Use cases of this database include but are not limited to prototyping, testing, embedded devices, and any scenario where a lightweight, zero-config database is needed. The simplicity and portability of SQLite also make it popular for mobile apps, web browsers, and smart devices using Python.

- Owing to its simplicity and a vast number of features, it is considered one of the best SQL databases for Python development.

### 2) MySQL
- MySQL is a popular open-source relational database that uses SQL and is preferred for web applications at scale needing transactional integrity. It rose to prominence as the database behind early web apps and continues to be widely used.

- The MySQL Python connector allows accessing MySQL natively from Python code while benefiting from its scalability, commercial support offerings, and open-source extensions like MariaDB. The Django framework has built-in support for MySQL.

- Use cases of this database include ecommerce systems, SaaS platforms, and enterprise applications where ACID compliance and sharding support are must-haves. Furthermore, the JSON support also makes MySQL flexible, making it an easy-to-use database with Python.

### 3) PostgreSQL
- PostgreSQL is an advanced open-source object-relational database that offers strong reliability and the full power of SQL. It provides extensive functionality through constraints, data types, operators, functions, and more.

- The psycopg PostgreSQL adapter makes it highly accessible from Python. Django also ships with PostgreSQL integration. The focus on extensibility, standards compliance and robustness makes it suitable for complex transactional systems at enterprise scale.

- Some of the noticeable use cases of this Python database include heavily transactional applications like banking systems, ecommerce marketplaces, IoT platforms, and geospatial and analytics applications.

- In addition to being free and open source, PostgreSQL is highly extensible. For example, you can define your own data types, build out custom functions, even write code from different programming languages without recompiling your database!

### 4) MongoDB
- MongoDB is the most popular document-oriented NoSQL database used with Python web and analytical workloads. It uses JSON-like documents to store data and makes it easy to represent hierarchical relationships.

- Python driver PyMongo provides idiomatic access from Python apps. The Flask framework ships with PyMongo integration. The dynamic schemas, rich querying via operators, indexing, and aggregation pipelines make MongoDB extremely versatile.

- It is advantageous in a number of platforms like OTT and streaming services, content management systems, monitoring systems, real-time analytics, and contextual recommendation engines.


## PostgreSQL basics (to be used mainly)

### step 1: install PostgreSQL. 

### step 2: open pgAdmin 4 application and add the current computer user to PostgreSQL
 - pgAdmin administration and development platform for PostgreSQL
 - add server. name = myserver, host: localhost, port 5432. 
 - with pgAdmin4, you have to create a user called postgres in order to be able to connect with and log in to pgAdmin4
 - Template databases will not show in the pgAdmin. don't use those databases.
 - In case you created your database as template CREATE DATABASE ... IS_TEMPLATE =true, then the database is considered as "system object" and is not shown in the list if PgAdmin4 option "Show system objects?" is set to false.
 
 
### step 3: create database on pgAdmin 4 or psql create mydb.

### step 4: connect to a PostgreSQL server with Python

- please first install the psycopg2 library:
- pip install psycopg2
	
1. Django
```sh
In your settings.py, add an entry to your DATABASES setting:


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "[YOUR_DATABASE_NAME]",
        "USER": "[YOUR_USER_NAME]",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}
```
		
2. Flask
- When using the Flask-SQLAlchemy extension you can add to your application code:

```sh
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[YOUR_DATABASE_NAME]'
db = SQLAlchemy(app)
```

3. SQLAlchemy
```sh
from sqlalchemy import create_engine
engine = create_engine('postgresql://localhost/[YOUR_DATABASE_NAME]')
```


### command for psql
1. psql database : enter the specific database
    - then \dt will list all tables
2. psql -U username : enter as a specific user
    - then you can operate as this use. 
    - \list : list all databases
    - Grant all privileges on database dbname to username 
    - create database dbname



## SQL

### SQL which stands for Structured Query Language which is used to communicate with the database. It provides a path through which we can access the database without going through complicated procedures. All the operations you can do follows the CRUD acronym.

### most common SQL commands
1. Create a Table : CREATE TABLE table_name(column1 datatype, column2 datatype, … columnN datatype);
    - Example: CREATE TABLE Employee (EMP_ID int, NAME varchar (255), SALARY int,  AGE int);
2. Select Query : The SELECT Statement in SQL is used for viewing all records from a table
    - SELECT column1, column2, columnN FROM table_name;
    - example 1: SELECT EMP_ID, NAME, AGE FROM Employee;  
    - example 2 all: SELECT * FROM table_name;

3. Insert Query : insert records into a table. The INSERT INTO declaration is used to insert new records in a table. 
    - INSERT INTO table_name (column1, column2, … columnN) VALUES (value1, value2, … valueN);
    - example : INSERT INTO employee (EMP_ID, NAME, SALARY, AGE) VALUES ('1', 'Rajesh', 25000, 30);

4. Delete Records From a Table : delete some selected records from a table. 
    - DELETE FROM employee WHERE [condition];
    - example : delete from polls_question where id = 3
    
5. Update Data in Records From a Table : update/modify the data in the existing records from a table. 
    - UPDATE table_name SET column1 = value1, column2 = value2, … WHERE [condition];
    - example : update polls_question set question_text = 'how is the wheather today?' where id = 2

    
6. Viewing Only Selected Records From a Table
    - SELECT COUNT (1) FROM table_name;
        - example : 
    - SELECT * FROM table_name WHERE [condition];
        - example : select * from polls_question where question_text like 'how is the wheather today?';
        - example 2: select * from polls_question where question_text like 'How % you?';
        - example 3: select pub_date, question_text from polls_question where id = '1' and pub_date = '2023-12-05 23:23:16+00';


7. EXPLAIN select pub_date, question_text from polls_question where id = '1' and pub_date = '2023-12-05 23:23:16+00';

### Foreign key
- A foreign key is a column or columns in a database that (e.g. table_1.column_a) that are linked to a column in a different table (table_2.column_b).

- The existence of a foreign key column establishes a foreign key constraint – a database rule that ensures that a value can be added or updated in column_a only if the same value already exists in column_b    
    
    
    

