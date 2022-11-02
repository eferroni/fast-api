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

## Routes:

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

## Environment variables:

.env sample file:

```
# choose a repository to use:
# - postgres
# - sqlite
# - dict
REPOSITORY=postgres

#postgres
POSTGRES_DB_NAME=books
POSTGRES_DB_USER=postgres
POSTGRES_DB_PASS=password

#sqlite
SQLITE_DB_NAME=books.db
SQLITE_DB_URL=sqlite:///./books.db
```