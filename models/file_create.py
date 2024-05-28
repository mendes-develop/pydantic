import os
from pydantic import BaseModel
class FileCreate(BaseModel):
  model: str
  
  def get_base_path(self):
    current = os.getcwd()
    return current + "/data" + f"/{self.model}/"

  def get_full_path(self, filename: str):
    return self.get_base_path() + filename + ".json"
  
  def read_all_json(self):
    dir_path = self.get_base_path()
    files = os.listdir(dir_path)
    print(files)
    
    for file in files:
      fullpath = dir_path + file
      with open(fullpath, "r") as f:
        print(f.read())
  
  def create_json(self, name:str, new_book: BaseModel):
    fullpath = self.get_full_path(name)
    os.makedirs(os.path.dirname(fullpath), exist_ok=True)    
    
    with open(fullpath, "w") as f:
      f.write(new_book.model_dump_json())