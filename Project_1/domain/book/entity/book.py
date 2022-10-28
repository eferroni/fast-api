class Book:
    _id: str
    _title: str
    _author: str

    def __init__(self, id: str, title: str, author: str):
        self._id = id
        self._title = title
        self._author = author
        self.validate()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    def change_title(self, new_title: str):
        self._title = new_title
        self.validate()

    @property
    def author(self):
        return self._author

    def change_author(self, new_author: str):
        self._author = new_author
        self.validate()

    def validate(self):
        if self._id == "":
            raise ValueError("Id is required")
        if self._title == "":
            raise ValueError("Title is required")
        if self._author == "":
            raise ValueError("Author is required")


