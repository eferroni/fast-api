**Disclaimer:** 4 Projects to follow the FastAPI course.


# Project_1 - Clean Architecture API with FastAPI:

A simple books public CRUD API created with Clean Architecture principles, decoupling the adapters from the core domain.

Adapters:
- Rest API: created with FastAPI framework.
- Dictionary Repository: to handle books data.
- SQLite Repository: to handle books data.
- PostgreSQL Repository: to handle books data.

Goal: create new adapters, like CLI and MySQL.

## Unit tests:

unit test were created for:
- Book entity.
- Dict Repository.

Goal: create new tests for API, SQLite and Posgres adapters.

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
|**Method**|**Route**|**Description**|
|GET|`/books/:id`|get one book|
|GET|`/books`|get all books|
|DELETE|`/books/:id`|delete one book|
|PUT|`/books/:id`|update one book|
|POST|`/books`|create one book|

### Users (passing a Bearer Token)

|`/users`||||
|-|-|-|-|
|**Method**|**Route**|**Description**|
|GET|`/users/:id`|get one user|
|GET|`/users`|get all users|

## Environment variables:

.env sample file:

```
# choose a repository to use:
# - postgresql
# - sqlite
# - dict
REPOSITORY=postgres

#postgres
POSTGRES_DB_NAME=books
POSTGRES_DB_USER=postgres
POSTGRES_DB_PASS=password
POSTGRES_DB_HOST=localhost
POSTGRES_DB_URL="postgresql://${POSTGRES_DB_USER}:${POSTGRES_DB_PASS}@${POSTGRES_DB_HOST}/${POSTGRES_DB_NAME}"

#sqlite
SQLITE_DB_NAME=books.db
SQLITE_DB_URL="sqlite:///./${SQLITE_DB_NAME}"

# secret key for generate jwt token
JWT_SECRET_KEY=JKSHdhsdyuashdasydhLDhs8
```

## Postman Collection:
FastAPI_Project1.postman_collection.json