from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import models
from schemas import Task, TaskCreate
from services.task_service import create_task_service, get_task_service

router = APIRouter(tags=['Tasks'])

@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(task, db)

@router.get("/goals/{goalId}/tasks", response_model=list[Task])
def get_tasks(goalId: int,  db: Session = Depends(get_db)):
    return get_task_service(goalId, db)
