**Disclaimer:** 4 Projects to follow the FastAPI course.


# Project_1 - Clean Architecture API with FastAPI:

A simple books public CRUD API created with Clean Architecture principles, decoupling the adapters from the domains.

Adapters:
- Rest API: created with FastAPI framework.
- GraphQL: created with FastAPI framework and strawberry.
- Dictionary Repository: to handle books data.
- SQLite Repository: to handle books data using sqlalchemy.
- PostgreSQL Repository: to handle books data using sqlalchemy.
- MongoDB Repository: to handle books data using pymongo.

Goal: create new adapters, for JSON Server and MySQL.

## Unit tests:

unit test were created for:
- Book entity.
- Dict Repository.

Goal: create new tests for API, SQLite, Postgres and MongoDB adapters.

## Rest API Routes V1:

Here are routes I already created:

### Books

|`/books`|||
|-|-|-|
|**Method**|**Route**|**Description**|
|GET|`/books/:id`|get one book|
|GET|`/books`|get all books|
|DELETE|`/books/:id`|delete one book|
|PUT|`/books/:id`|update one book|
|POST|`/books`|create one book|

## Rest API Routes V2:

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

## GraphQL Schemas:

### Query
book(bookId:ID!)

books(title: String = null, author: String = null, size: Int! = 10, page: Int! = 1, order: String! = "title")
login(username: String!, password: String!)
user(userId: String!)
users(username: String = null, email: String = null, firstName: String = null, lastName: String = null, page: Int! = 1, size: Int! = 10, order: String! = "username")

### Mutation
createBook(title: String!, author: String!)
updateBook(bookId: ID!, title: String!, author: String!)
deleteBook(bookId: ID!)
createUser(username: String!, email: String!, firstName: String!, lastName: String!, password: String!)
updateAccount(userId: String!, email: String!, firstName: String!, lastName: String!)
updatePassword(userId: String!, username: String!, password: String!, newPassword: String!)
activateAccount(userId: String!)
deactivateAccount(userId: String!)
deleteAccount(userId: String!)

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