class Book:
    def __init__(self, genre, author, title, price, in_stock,):
        
        self.genre = genre
        self.author = author
        self.title = title
        self.price = int(price)
        self.in_stock = in_stock


    def book_details(self):
        while True:
            try:
                to_display = input("enter an option for information\n1. Genre\n2. Author\n3. Title\n4. Price\n5. In Stock\n6. quit")

            except:
                pass




book1 = Book("Children's", "Ron Roy", "The Canary Caper", 5, "yes")


print(book1.author)
print(book1.genre)
print(book1.price)
print(book1.in_stock)


book1.book_details()