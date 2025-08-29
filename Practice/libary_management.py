class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {"title": title, "author": author}
        self.books.append(book)
        print(f"✅ Book '{title}' by {author} added.")

    def view_books(self):
        if not self.books:
            print("📚 No books in the library.")
            return
        print("\n📖 All Books:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book['title']} by {book['author']}")

    def search_book(self, title):
        found = False
        for book in self.books:
            if book["title"].lower() == title.lower():
                print(f"🔍 Found: {book['title']} by {book['author']}")
                found = True
                break
        if not found:
            print(f"❌ Book '{title}' not found.")

# ---------- Testing ----------
library = Library()
library.add_book("Python Basics", "John Doe")
library.add_book("Learn Django", "Jane Smith")
library.view_books()
library.search_book("Python Basics")
library.search_book("C++ Primer")
