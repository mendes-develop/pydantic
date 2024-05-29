from pydantic import BaseModel
from typing import Optional
from models.file_create import FileCreate
import os
    
class Book(BaseModel):
  title: str
  author: str
  is_read: bool = False
  borrowed_by: Optional[str] = None
  owner: Optional[int] = None

class BookRegistry:
  file_create: FileCreate = FileCreate(model="book")
  
  def add_book(self, title: str, author: str, owner: int):
    newBook = Book(title=title, author=author, owner=owner)    
    self.file_create.create_json(title, newBook)
    
  def read_all_books(self):
    return self.file_create.read_all_json()
  
  def borrow_book(self, title: str, borrower: str):
    for book in self.read_all_books():
      if book.title == title:
        book.borrowed_by = borrower
        self.file_create.update_json(title, book)
        return
    print("Book not found")
    
