from fastapi import FastAPI
from views.api import api_router

app = FastAPI(), api_router()

