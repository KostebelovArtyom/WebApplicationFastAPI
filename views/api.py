from fastapi import APIRouter

# подключил роутер employees к роутеру api.
from .employees.api import router as employees_router

api_router = APIRouter(prefix="/api")  # Создал новый api_router, роутер верхнего уровня с префиксом /api
api_router.include_router(employees_router)
