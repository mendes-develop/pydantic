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
    # read file from folder
    file = self.file_create.get_one_json(title)
    if not file:
      print("Not Found")
      return
    
    found_book = Book(**file)
    found_book.borrowed_by = borrower
    print(found_book)
    self.file_create.create_json(title, found_book)
    
    # for book in self.read_all_books():
    #   if book.title == title:
    #     return
    # print("Book not found")
    
