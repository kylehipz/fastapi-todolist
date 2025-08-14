from fastapi import FastAPI

from models import SessionDep, Task, create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def main_route():
    return {"message": "Kyle Hipz to hoy!"}


@app.post("/tasks/")
async def create_task(task: Task, session: SessionDep):
    session.add(task)
    session.commit()
    session.refresh(task)

    return task
