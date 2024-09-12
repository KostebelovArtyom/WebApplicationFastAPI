import uvicorn
from fastapi import FastAPI

from views.api import api_router  # Объявил новое приложение FasrAPI

app = FastAPI()
app.include_router(api_router)  # Подключил api.router к основному app


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
