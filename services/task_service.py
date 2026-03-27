from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from schemas import TaskCreate
import models
from repositories.task_repository import create_task as repo_create_task, get_task as repo_get_task

def create_task_service(task:TaskCreate, db:Session):
    newtask = models.Task(
        goalId = task.goalId,
        title = task.title,
        plannedHours = task.plannedHours,
        startDate = task.startDate,
        endDate = task.endDate,
        status = "pending"
    )
    try:
        return repo_create_task(newtask, db)
    except SQLAlchemyError as e:
        db.rollback()
        raise

def get_task_service(goalId, db:Session):
    return repo_get_task(goalId, db)