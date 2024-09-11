from dataclasses import dataclass, field
from typing import Optional
from .models import Employee, EmployeeCreate


@dataclass
class EmployeeStorage:
    last_id: int = 0
    employees: dict[int, Employee] = field(default_factory=dict)

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create_employee(self, employeecreate: EmployeeCreate) -> Employee:
        employee = Employee(id=self.next_id, **employeecreate.model_dump())
        self.employees[employee.id] = employee
        return employee
