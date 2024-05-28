from pydantic import BaseModel
from typing import Optional
from models.file_create import FileCreate
import os
    
class Book(BaseModel):
  title: str
  author: str
  is_read: bool = False
  borrowedBy: Optional[str] = None
  owner: Optional[int] = None

class BookRegistry(BaseModel):
  file_create: FileCreate = FileCreate(model="book")
  
  def add_book(self, title: str, author: str, owner: int):
    newBook = Book(title=title, author=author, owner=owner)    
    self.file_create.create_json(title, newBook)
    
  def read_all_books(self):
    return self.file_create.read_all_json()
    
