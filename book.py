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
                to_display = int(input("enter an option for information\n1. Genre\n2. Author\n3. Title\n4. Price\n5. In Stock\n6. Quit\n"))

                if to_display == 6:
                    print("Goodbye")
                    break

                elif to_display not in range(1,6):
                    print("please choose one of the options")
                    continue
                
                elif to_display == 1:
                    print(f"Genre: {self.genre}")
                
                elif to_display == 2:
                    print(f"Author: {self.author}")
                
                elif to_display == 3:
                    print(f'Title: "{self.title}"')
                
                elif to_display == 4:
                    print(f"Price: {self.price}")
                
                elif to_display == 5:
                    print(f"InStock: {self.in_stock}")

            except ValueError:
                print("Response must be an integer between 1 and 6")
                continue




book1 = Book("Children's", "Ron Roy", "The Canary Caper", 5, "yes")


print(book1.author)
print(book1.genre)
print(book1.price)
print(book1.in_stock)


book1.book_details()

