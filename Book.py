class Book:
    book_item = []
    def __init__(self, name, author, publish_date, pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        Book.book_item.append(self)
        
    @classmethod
    def get_all_books(cls):
        print(len(cls.book_item))
        return cls.book_item


