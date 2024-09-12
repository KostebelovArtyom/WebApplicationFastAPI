from dataclasses import dataclass, field
from typing import Optional
from .models import Employee, EmployeeCreate


# Этот класс нужен для работы с объектами в оперативной памяти, без использования базы данных. В рамках класса нужно
# будет создавать, читать, удалять объекты типа Employee. Ниже 2 описаны все поля и методы, которые позволят реализовать
# необходимый интерфейс для работы веб-приложения с сущностями Employee.


@dataclass
class EmployeeStorage:
    last_id: int = 0
    # Это поле employees типа словарь (dict), где ключ – целое число, а значение это тип Employee (схема pydantic)
    # число, а значение это тип Employee (схема pydantic). Для словаря нужно вычисляемое значение, достаточно указать
    # dict в поле default_factory Этот словарь будет хранить все созданные экземпляры Employee, где ключ
    # это идентификатор (id) сотрудника
    employees: dict[int, Employee] = field(default_factory=dict)

    # Этот метод позволяет при каждом следующем обращении генерировать новый идентификатор
    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    # метод, который принимает экземпляр EmployeeCreate, создаёт экземпляр Employee, выдаёт ему новый id
    # (на основе next_id), сохраняет этот экземпляр в словарь и возвращает созданный экземпляр Employee
    def create_employee(self, employee_create: EmployeeCreate,) -> Employee:
        employee = Employee(id=self.next_id, **employee_create.model_dump(),)
        self.employees[employee.id] = employee
        return employee

    # объявите метод для получения из кэша списка (list) всех доступных Employee
    def get_employees(self) -> list[Employee]:
        return list(self.employees.values())

    # - объявите метод для получения из кэша экземпляра Employee по id
    def get_employees_by_id(self, employee_id: int,) -> Optional[Employee]:
        return self.employees.get(employee_id)

    # - объявите метод для удаления из кэша экземпляра Employee по id;
    def delete_employees_by_id(self, employees_id: int) -> None:
        self.employees.pop(employees_id, None)


storage = EmployeeStorage()
