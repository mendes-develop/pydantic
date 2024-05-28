from pydantic import BaseModel
from typing import Optional
import os
    
class Book(BaseModel):
  title: str
  author: str
  is_read: bool = False
  borrowedBy: Optional[str] = None
  owner: Optional[int] = None

class BookRegistry(BaseModel):
  counter: int = 0
  books: dict[int, Book] = {}
  
  def get_book_path(self, filename: str):
    current = os.getcwd()
    return current + "/books/" + filename + ".json"
    
  
  def add_book(self, title: str, author: str, owner: int):
    newBook = Book(title=title, author=author, owner=owner)
    self.books[self.counter] = newBook
    self.counter += 1
    
    fullpath = self.get_book_path(title)
    
    os.makedirs(os.path.dirname(fullpath), exist_ok=True)    
    with open(fullpath, "w") as f:
      f.write(newBook.model_dump_json())