**Disclaimer:** 4 Projects to follow the FastAPI course.


# Project_1 - Clean Architecture API with FastAPI:

A simple books public CRUD API created with Clean Architecture principles, decoupling the adapters from the domains.

Adapters:
- Rest API: created with FastAPI framework.
- Dictionary Repository: to handle books data.
- SQLite Repository: to handle books data.
- PostgreSQL Repository: to handle books data.
- MongoDB Repository: to handle books data.

Goal: create new adapters, like GraphQl and MySQL.

## Unit tests:

unit test were created for:
- Book entity.
- Dict Repository.

Goal: create new tests for API, SQLite, Postgres and MongoDB adapters.

## Routes V1:

Here are routes I already created:

### Books

|`/books`||||
|-|-|-|-|
|**Method**|**Route**|**Description**|
|GET|`/books/:id`|get one book|
|GET|`/books`|get all books|
|DELETE|`/books/:id`|delete one book|
|PUT|`/books/:id`|update one book|
|POST|`/books`|create one book|

## Routes V2:

Here are routes I already created:

### Auth

|`/auth`||||
|-|-|-|-|
|**Method**|**Route**|**Description**|
|POST|`/auth/create`|create a user|
|POST|`/auth/login`|login - get a token|

### Account (passing a Bearer Token)

|`/account`||||
|-|-|-|-|
|**Method**|**Route**|**Description**|
|PUT|`/account/:id`|update account|
|PUT|`/account/:id/password`|change password|
|PUT|`/account/:id/activate`|activate account|
|PUT|`/account/:id/deactivate`|deactivate account|
|DELETE|`/account/:id`|delete account|

### Books (passing a Bearer Token)

|`/books`||||
|-|-|-|-|
|**Method**|**Route**|**Description**|**Query Params**|
|GET|`/books/:id`|get one book|title, author, page, size, order|
|GET|`/books`|get all books||
|DELETE|`/books/:id`|delete one book||
|PUT|`/books/:id`|update one book||
|POST|`/books`|create one book||

### Users (passing a Bearer Token)

|`/users`||||
|-|-|-|-|
|**Method**|**Route**|**Description**|**Query Params**|
|GET|`/users/:id`|get one user||
|GET|`/users`|get all users|users, email, first_name, last_name, page, size, order|

## Environment variables:

.env sample file:

```
# choose a repository to use:
# - mongodb
# - postgresql
# - sqlite
# - dict
REPOSITORY=mongodb

# mongo
MONGO_DB_NAME=books
MONGO_ATLAS_USERNAME=mongo
MONGO_ATLAS_PASSWORD=password
MONGO_URL=mongodb+srv://${MONGO_ATLAS_USERNAME}:${MONGO_ATLAS_PASSWORD}@cluster0.dgilwiw.mongodb.net/?retryWrites=true&w=majority

# postgres
POSTGRES_DB_NAME=books
POSTGRES_DB_USER=postgres
POSTGRES_DB_PASS=password
POSTGRES_DB_HOST=localhost
POSTGRES_DB_URL="postgresql://${POSTGRES_DB_USER}:${POSTGRES_DB_PASS}@${POSTGRES_DB_HOST}/${POSTGRES_DB_NAME}"

# sqlite
SQLITE_DB_NAME=books.db
SQLITE_DB_URL="sqlite:///./${SQLITE_DB_NAME}"

# token
JWT_SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
JWT_ALGORITH=HS256
JWT_EXPIRE_MINUTES=15
```

## Postman Collection:
FastAPI_Project1_RESTAPI.postman_collection.json