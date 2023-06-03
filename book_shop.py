# make a class for book description
class book:
  def __init__(self,name,author,price):
    self.name = name
    self.author = author
    self.price = price

  def enter_name(self):
    return self.name
    
  def enter_author(self):
    return self.author
    
  def enter_price(self):
    return self.price

# make the main bookshop description
class Book_Shop:
  Books_List= []
  def Add_Book(self):
    name = input("🕮 Enter book name 🕮: ")
    author = input("𐀪 Enter author name 𐀪: ")
    price = int(input("$ Enter price $: "))
    self.Books_List.append(book(name, author, price))
    print("🎊 Congrats Book has been added 🎊\n\n")

  def Print_Books(self):
    for book in self.Books_List:
      print("Name:",book.enter_name(), "\nAuthor:",book.enter_author(),"\nPrice:",book.enter_price(),"\n\n")
     



#the main code
libirary = Book_Shop()
while True:
  print("Enter[1]: 🕮  Add Book 🕮")
  print("Enter[2]: 🕮  Print Books 🕮")
  print("Enter[3]: ✖ Exit ✖")
  choice = int(input("Enter your choice ^_^: "))
  if choice == 1:
        libirary.Add_Book()
  elif choice == 2:
        libirary.Print_Books()
  elif choice == 3:
        break
