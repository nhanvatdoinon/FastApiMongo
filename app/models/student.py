from pydantic import BaseModel,Field,EmailStr

class Student(BaseModel):
    name: str = Field(...)
    address : str = Field(...)
    email : EmailStr = Field(...)
    phone : str = Field(...)
    age : int = Field(...,gt=1,lt=120)
    gpa : float = Field(...,le=4.0)
