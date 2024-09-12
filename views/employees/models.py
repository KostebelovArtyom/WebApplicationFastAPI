from pydantic import BaseModel, EmailStr  # Объявил pydantic моедлей и формы EmailStr


class EmployeeBase(BaseModel):
    full_name: str
    email: EmailStr


class EmployeeCreate(EmployeeBase):
    ...


class Employee(EmployeeBase):
    id: int
