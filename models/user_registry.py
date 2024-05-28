from pydantic import BaseModel
from typing import Tuple

class User(BaseModel):
  name: str
  bio: str
class UserRegistry(BaseModel) :
  counter: int = 0
  users: dict[int, User] = {}

  def add_user(self, username: str, bio: str):
    newUser = User(name=username, bio=bio)
    self.users[self.counter] = newUser
    self.counter += 1
    
def get_user(self, id: int)-> Tuple[User, str]:
    return (self.users[id], self.users[id].bio)
