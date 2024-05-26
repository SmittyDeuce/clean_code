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

    
    def store_admin(self):
        admin_password = "theBookStore"
        while True:
                enter_password = input("Enter Admin Password: (enter 0 to quit) ")
                
                if enter_password == "0":
                    print("Goodbye")
                    break
                
                if enter_password != admin_password:
                    print("Please enter the correct password. or 0 (Zero) to quit")
                    continue
                
                if enter_password == admin_password:
                    print("Welcome Admin")

                    while True:
                        try:
                            change_status = input("Please Choose an Option:\n1. to mark in stock\n2. for out of stock\n3. to update price\n0. to quit\n")

                            if int(change_status) == 0:
                                break

                            elif int(change_status) == 1:
                                self.in_stock = "yes"
                                print(f'"{self.title}" stock has been marked in stock')
                                break

                            elif int(change_status) == 2:
                                self.in_stock = "no"
                                print(f'"{self.title}" stock has been marked out of stock')
                                break
                            
                            elif int(change_status) == 3:
                                price_change = input("Enter New Price: ")

                                if not price_change.isdigit() or int(price_change) <= 0:
                                    print("Please Enter number greater than 0")
                                    continue

                                else:
                                    self.price = int(price_change)
                                    print(f'"{self.title}" price has been updated')

                            else:
                                print("Error: please enter one of the options")
                        
                        except ValueError:
                            print("Please Enter 0, 1, 2, or 3")
                            continue

book1 = Book("Children's", "Ron Roy", "The Canary Caper", 5, "yes")


print(book1.author)
print(book1.genre)
print(book1.price)
print(book1.in_stock)


# book1.book_details()

book1.store_admin()
print(book1.in_stock)
print(book1.price)