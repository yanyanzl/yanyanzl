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



### common sql command:
    ``` SQL
    - CREATE USER myuser WITH PASSWORD 'secret_passwd';
        - This new user does not have any permissions other than the default permissions available to the public role
        - When a new database is created, PostgreSQL by default creates a schema named public and grants access on this schema to a backend role named public
        - Because of this, when a user tries to create a new table without specifying the schema name, the table gets created in the public schema. As mentioned earlier, by default, all users have access to create objects in the public schema, and therefore the table is created successfully.
        
        
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




    