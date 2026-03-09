from fastapi import FastAPI
from app.api import users
from app.api import auth
from app.api import tasks

app = FastAPI()

app.include_router(
    users.router,
)

app.include_router(
    tasks.router,
)

app.include_router(
    auth.router,
)
