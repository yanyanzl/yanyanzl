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
 - pgAdmin is an administration and development platform for PostgreSQL
