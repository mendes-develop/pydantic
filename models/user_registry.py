from pydantic import BaseModel
from typing import Tuple
import os
from models.file_create import FileCreate

class User(BaseModel):
  name: str
  bio: str
class UserRegistry :
  file_create: FileCreate = FileCreate(model="user")

  def add_user(self, username: str, bio: str):
    newUser = User(name=username, bio=bio)    
    self.file_create.create_json(username, newUser)
    
  def read_all_users(self):
    return self.file_create.read_all_json()
      
  def get_user(self, id: int)-> Tuple[User, str]:
      return (self.users[id], self.users[id].bio)
    
