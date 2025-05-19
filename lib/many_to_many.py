class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self._title = title
        Book.all_books.append(self)

    @property
    def title(self):
        return self._title

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        # Return all unique authors who have contracts for this book
        return list({contract.author for contract in self.contracts()})


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self._name = name
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

        Contract.all_contracts.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
