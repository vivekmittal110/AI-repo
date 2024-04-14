from enum import Enum

class vivek(Enum):
    Active = 1
    Inactive = 0
 
print(vivek.Active.value)
print(vivek(1))
print(vivek["Active"])
print(list(vivek))
print(len(vivek))