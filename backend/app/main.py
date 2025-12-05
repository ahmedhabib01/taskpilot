from fastapi import FastAPI
from app.routers import users, tasks
from app.database import engine, Base

# create tables (for beginners, Alembic is recommended for migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskPilot")

app.include_router(users.router)
app.include_router(tasks.router)

@app.get('/')
def root():
    return {"msg": "TaskPilot API"}