run:
uvicorn infrastructure/api/book:app --reload

access swagger:
http://localhost:8000/docs#/

tests:
pytest -s -v domain/book/entity/test_book.py
pytest -s -v infrastructure/book/repository/dict/test_book_repository.py