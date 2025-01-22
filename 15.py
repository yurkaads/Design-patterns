from abc import ABC, abstractmethod

# Інтерфейс для ітератора
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Інтерфейс для колекції
class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# Конкретна колекція
class BookCollection(IterableCollection):
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def create_iterator(self):
        return BookIterator(self)

# Конкретний ітератор
class BookIterator(Iterator):
    def __init__(self, collection: BookCollection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection.books)

    def next(self):
        if self.has_next():
            book = self._collection.books[self._index]
            self._index += 1
            return book
        raise StopIteration("У колекції більше немає книг.")

# Використання
book_collection = BookCollection()
book_collection.add_book("Книга 1")
book_collection.add_book("Книга 2")
book_collection.add_book("Книга 3")

iterator = book_collection.create_iterator()
while iterator.has_next():
    print(iterator.next())
