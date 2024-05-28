from datetime import datetime
from typing import Tuple
from models.user_registry import UserRegistry
from models.book_registry import BookRegistry

from pydantic import BaseModel

class BookStore(BaseModel):
    bookRegistry: BookRegistry = BookRegistry()
    userRegistry: UserRegistry = UserRegistry()
    
    def addUser(self, name: str, bio: str) -> None:
      # guarantee that it doesn't repeat
      self.userRegistry.add_user(name, bio)
      print(f"add_user({name}, {bio})")