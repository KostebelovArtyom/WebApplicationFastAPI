from fastapi import APIRouter, status, HTTPException

from .crud import storage
from .models import Employee, EmployeeCreate
# создал новый экземпляр APIRouter и указал префикс /employees и тег Employees
router = APIRouter(prefix="/employees", tags=["Employees"])


# объявил view для получения списка сотрудников, указал схему response_model для описания, как будет возвращён
# список из сотрудников
@router.get("", response_model=list[Employee],)
def get_employees_list() -> list[Employee]:
    # внутри view функции при помощи экземпляра storage вернул список известных сотрудников
    return storage.get_employees()


# объявите view для получения сотрудника по id, указал схему response_model для описания, как будет возвращена
# информация о сотруднике
@router.get(
    "/{employee_id}",
    response_model=Employee,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Employee not found",
            "content": {
                "application/json": {
                    "schema": {
                        "title": "Not found",
                        "type": "object",
                        "properties": {
                            "detail": {
                                "title": "Detail",
                                "type": "string",
                                "example": "Could not find employee #7",
                            },
                        },
                    },
                },
            },
        },
    },
)
# внутри view функции при помощи экземпляра storage получил объект по id, проверил полученный объект
def get_employee_by_id(employee_id: int) -> Employee:
    employee = storage.get_employees_by_id(employee_id=employee_id)
    if employee is not None:
        return employee
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Could not find employee #{employee_id}",
    )


# объявил view для создания сотрудника указал схему response_model для описания, как будет возвращена
# информация о созданном сотруднике
@router.post("", response_model=Employee,)
def create_employee(employee_create: EmployeeCreate) -> Employee:
    return storage.create_employee(employee_create=employee_create)


# объявил view для удаления сотрудника по идентификатору;
@router.delete("/{employee_id}", status_code=status.HTTP_404_NOT_FOUND,)
def delete_employee_by_id(employee_id: int) -> None:
    storage.delete_employees_by_id(employee_id=employee_id)
