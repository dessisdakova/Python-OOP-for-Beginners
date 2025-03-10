class Book:

    def __init__(self, title, author, num_pages, ISBN, publisher):
        self._title = title
        self._author = author
        self._num_pages = num_pages
        self._ISBN = ISBN
        self._publisher = publisher

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def num_pages(self):
        return self._num_pages

    @property
    def ISBN(self):
        return self._ISBN

    @property
    def publisher(self):
        return self._publisher