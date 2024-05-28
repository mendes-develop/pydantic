from models.book_store import BookStore
from pydantic import BaseModel

class App(BaseModel):

  new_store: BookStore = BookStore()
  
  def run(self):
    while(True):
          self.print_options()
          exit = self.parse_input()
          if exit == "exit":
            break

  def print_options(self):
    print("\n")
    print("1. Add a new user")
    print("2. Add a new book")
    print("3. List all books")
    print("4. List all users")
    print("5. Exit")
    print("\n")
    
  def parse_input(self):
    number = input("What do you want to do?(number): ")
    
    if not number.isdigit():
      print("Please enter a number, don't be a clown")
      return
    
    num_to_int = int(number)
    print("\n")
    if num_to_int == 1:
        return  self.add_user()
    elif num_to_int == 2:
        return self.add_book()
    elif num_to_int == 3:
        return self.list_books()
    elif num_to_int == 4:
        return self.list_users()
    elif num_to_int == 5:
        return "exit"
    print("\n")
    
  def list_users(self):
    self.new_store.userRegistry.read_all_users()
    
  def list_books(self):
    self.new_store.bookRegistry.read_all_books()
    
  def add_book(self):
    title = input("What is the book's title? ")
    author = input("What is the book's author? ")
    self.new_store.bookRegistry.add_book(title, author, 0)
    
  def add_user(self):
    name = input("What is the user's name? ")
    bio = input("What is the user's bio? ")
    self.new_store.addUser(name, bio)
      
if __name__ == "__main__":
  app_instance = App()
  app_instance.run()
  
