# Databases

## What is a database
- Special software to store data

## Where does the database live?
- Cloud
    - place where you can run database
    - renting PC
- Providers
    - AWS
    - Azure
    - Google Cloud Platform

----

- Renting servers -> scalability
- vertical and horizontal scalability
- accomodating more users
- Distribution Denial Of Service
    - auto-scaling opens your website up for malcious traffic 
    - dummy website to redirect bots
    - you redirect them by using the "are you a bot?" verification test

## Why do you need a database?
- faq will have it in the ram
- querying becomes easier
- CRUD - easy
- backups are inbuilt 
- undo - easily with no time limit 
- performance 

## SQL vs NoSQL
- relational vs non relational dbs
- SQL is relational has tables, rows and columns 
    - PLSQL - Oracle -> high cost
    - PostgreSQL -> free and open
    - MySQL - Microsoft -> free
    - Microsoft Server
    - amazon RDS - relational database system
- NoSQL is non and it is stored by key and values in documents
    - mongoDB
    - couchDB
    - redis -> vry fast cache
    - cassandra
    - dynamoDB -> amazon, can only use within aws
    - neo4j
    - Firebase


## Normalisation
- normalisation - reduces risk of annomaly
- annomaly - data mismatch
- 3NF 
- higher the normal form the more safe
- first normal form:
    - row order to convey info not permitted
    - mixing data types is not permitted
    - has to have a PK
    - repeating groups not allowed

- primary key is necessary
    - unique
    - not null
    - only one column

- second normal form:
    - each non-key attributes must depend on the entire PK

- third normal form:
    - Non primary key attributes do not depend on each other
    - every 

- DML vs DDL