### run:
uvicorn infrastructure.api.main:app --reload

uvicorn infrastructure.graphql.main:app --reload


### access to rest api swagger:
http://localhost:8000/docs#/


### access to graphiql:
http://localhost:8000/graphql/


### tests:
pytest -s -v domain/book/entity/test_book.py
pytest -s -v infrastructure/book/repository/dict/test_book_repository.py