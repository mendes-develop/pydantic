from datetime import datetime
from typing import Tuple
from models.user_registry import UserRegistry
from models.book_registry import BookRegistry

from pydantic import BaseModel

class BookStore:
    bookRegistry: BookRegistry = BookRegistry()
    userRegistry: UserRegistry = UserRegistry()
    
    def addUser(self, name: str, bio: str) -> None:
      # guarantee that it doesn't repeat
      self.userRegistry.add_user(name, bio)
      print(f"add_user({name}, {bio})")
      
    def borrow_book(self, title: str, borrower: str) -> None:
      # check if the book exists
      # check if users exists
      self.bookRegistry.borrow_book(title, borrower)
      print(f"borrow_book({title}, {borrower})")