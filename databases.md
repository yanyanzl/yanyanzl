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

### step 3: manage the users and databases:
    
    - where is the Directory for the data: 
        - SHOW data_directory;
        - select setting from pg_settings where name = 'data_directory';
    - where is the directory for the postgreSQL application:
        - which psql
    

    - in terminal: use command: psql or psql database_name to enter postgresql database mode.
    - SELECT * FROM pg_user;
    - SELECT * FROM pg_roles;
    - \du : list all users/roles
    - \dt : list all tables
    - \l : list all database 
    - \dn : list all schema
    - \conninfo : current connection information : equal to sql: select current_user;
    - \c new_database_name : change to the new database;
    - \c current_db new_user_name : change to new user;
    - \c new_db_name new_user_name : change to new db and new user;
    - \password username   : change the password for username;
    - select CURRENT_SCHEMA;  to get the current schema
    - select CURRENT_SCHEMAS(TRUE);  to get all the current path's schemas
    
    - Create User:
        - CREATE USER myuser WITH PASSWORD 'secret_passwd';
            - This new user does not have any permissions other than the default permissions available to the public role
            - When a new database is created, PostgreSQL by default creates a schema named public and grants access on this schema to a backend role named public
            - Because of this, when a user tries to create a new table without specifying the schema name, the table gets created in the public schema. 
            - As mentioned earlier, by default, all users have access to create objects in the public schema, and therefore the table is created successfully.

    - Revoke permissions on public schema
        - To fix this, you should revoke the default create permission on the public schema from the public role using the following SQL statement:
        - REVOKE CREATE ON SCHEMA public FROM PUBLIC;
        - REVOKE ALL ON DATABASE mydatabase FROM PUBLIC;
            - This makes sure that users can’t connect to the database by default unless this permission is explicitly granted.
        
    - Read-only role
        - CREATE ROLE readonly;  this will create a role readonly
        - GRANT CONNECT ON DATABASE mydatabase TO readonly;   this give the connect right to readonly
        - GRANT USAGE ON SCHEMA myschema TO readonly;    this give the use of the schema to readonly
        - GRANT SELECT ON TABLE mytable1, mytable2 TO readonly;      this give the select right to readponly to tables
        - or GRANT SELECT ON ALL TABLES IN SCHEMA myschema TO readonly;
        - The preceding SQL statement grants SELECT access to the readonly role on all the existing tables and views in the schema myschema. Note that any new tables that get added in the future will not be accessible by the readonly user. To help ensure that new tables and views are also accessible, run the following statement to grant permissions automatically:
        - ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT ON TABLES TO readonly;
        - GRANT readonly TO myuser1;   this will grant the readonly role permission to myuser1
        - REVOKE readwrite FROM myuser1;  this will remove the readwrite role permission from myuser;
        
    - Read/write role
        - -- Read/write role
        - CREATE ROLE readwrite;
        - GRANT CONNECT ON DATABASE mydatabase TO readwrite;
        - GRANT USAGE, CREATE ON SCHEMA myschema TO readwrite;
        - GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA myschema TO readwrite;
        - ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO readwrite;
        - GRANT USAGE ON ALL SEQUENCES IN SCHEMA myschema TO readwrite;
        - ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT USAGE ON SEQUENCES TO readwrite;

### select a schema when using psql/connection;
- In PostgreSQL the system determines which table is meant by following a search path, which is a list of schemas to look in.
- The first matching table in the search path is taken to be the one wanted, otherwise, if there is no match a error is raised, even if matching table names exist in other schemas in the database.
    - To show the current search path you can use the following command:
        - SHOW search_path;
        - SET search_path TO myschema;
        - SET search_path TO myschema, public; 
    
    
### common sql command:
    ``` SQL
        
        
    - ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;
    
    - insert into aiinvest_assetdata (asset_name,asset_data_date,asset_close_price,asset_open_price,asset_high_price,asset_low_price,asset_volume,asset_id) values ('tsla', '2023-12-14 00:00:00','239.2899932861328','239.2899932861328','239.2899932861328','239.2899932861328',160569000,1) ON CONFLICT DO NOTHING
    
    - insert into aiinvest_assetdata (asset_name,asset_data_date,asset_close_price,asset_open_price,asset_high_price,asset_low_price,asset_volume,asset_id) 
select 'tsla', '2023-12-13 00:00:00','239.2899932861328','239.2899932861328','239.2899932861328','239.2899932861328',160569000,1 
WHERE NOT EXISTS (
        SELECT id FROM aiinvest_assetdata WHERE asset_data_date = '2023-12-14 00:00:00'
    );
    
    - SELECT EXISTS (
   SELECT FROM information_schema.tables 
   WHERE  table_schema = 'public'
   AND    table_name   = 'aiinvest_assetdata'
   );
   
   - SELECT column_name FROM information_schema.columns
        WHERE table_name = 'aiinvest_assetdata'
        
    - select * from aiinvest_assetdata
    
    - delete from aiinvest_assetdata
    
    - DROP TABLE author;
    
    - The following command can be used to create an index on the id column,in table test1 :
        - CREATE INDEX test1_id_index ON test1 (id);
    ```



### Enable postgreSQL to accept connection from other lan  computers
    - First, edit the postgresql.conf file, and set listen_addresses. The default value of 'localhost' will only listen on the loopback adaptor. 
        - You can change it to '*', meaning listen on all addresses, or specifically list the IP address of the interfaces you want it to accept connections from. 
        - Note that this is the IP address of the postgreSQL server ip address. which the interface has allocated to it. 
    - You must restart postgresql for the changes to listen_addresses to take effect.
    - Next, in pg_hba.conf, you will need an entry like this:
        - # TYPE  DATABASE        USER            ADDRESS                 METHOD
        - host    {dbname}        {user}          192.168.1.0/24          md5
            - {dbname} is the database name you are allowing access to. You can put "all" for all databases.
            - {user} is the user who is allowed to connect. Note that this is the postgresql user, not necessarily the unix user.
            - The ADDRESS part is the network address and mask that you want to allow. The mask I specified will work for 192.168.1.x as you requested.
            - The METHOD part is the authentication method to use. There are a number of options there. md5 means it will use an md5 hashed password. 'trust' which you had in your sample means no authentication at all - this is definitely not recommended.
    - pg_ctl reload -D /Users/yanyanzhou/Library/Application\ Support/Postgres/var-16


    - https://aws.amazon.com/blogs/database/managing-postgresql-users-and-roles/#:~:text=Users%2C%20groups%2C%20and%20roles%20are,for%20the%20CREATE%20ROLE%20statement.


### postgreSQL in Python
- pip install psycopg2

- In psycopg, the connection class is responsible for handling transactions. When you issue the first SQL statement to the PostgreSQL database using a cursor object, psycopg creates a new transaction.

    - From that moment, psycopg executes all the subsequent statements in the same transaction. If any statement fails, psycopg will abort the transaction.

    - The connection class has two methods for ending a transaction: commit() and rollback(). If you want to commit all changes to the PostgreSQL database permanently, you call the commit() method. And in case you want to cancel the changes, you call the rollback() method. Closing the connection object or destroying it using the  del will also result in an implicit rollback.
    
    - It is important to notice that a simple SELECT statement will start a transaction that may result in undesirable effects such as table bloat and locks. Therefore, if you are developing a long-living application, you should call the commit() or rollback() method before leaving the connection unused for a long time.
    
    - Alternatively, you can set the autocommit attribute of the connection object to True. This ensures that psycopg executes every statement and commits it immediately.
    
    - The autocommit mode is also useful when you execute statements required to execute outside a transaction such as CREATE DATABASE  and VACUUM.
    
    - The following shows a typical pattern for handling a transaction in psycopg:
        
        ``` Python
        import psycopg2

        conn = None
        try:
            conn = psycopg2.connect(dsn)
            cur = conn.cursor()
            # execute 1st statement
            cur.execute(statement_1)
            # execute 2nd statement
            cur.execute(statement_1)
            # commit the transaction
            conn.commit()
            # close the database communication
            cur.close()
        except psycopg2.DatabaseError as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        
        ``` 










    