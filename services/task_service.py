from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from schemas import TaskCreate
import models
from repositories.goal_repository import get_goal_by_id as repo_get_goal
from exception  import GoalNotFoundException
from repositories.task_repository import create_task as repo_create_task, get_task as repo_get_task

def create_task_service(task:TaskCreate, db:Session):
    goal = repo_get_goal(db, task.goalId)
    if not goal:
        raise GoalNotFoundException(task.goalId)
    
    newtask = models.Task(
        goalId = task.goalId,
        title = task.title,
        plannedHours = task.plannedHours,
        startDate = task.startDate,
        endDate = task.endDate,
        status = "pending"
    )
    try:
        repo_create_task(db, newtask)
        db.commit()
        db.refresh(newtask)
        return newtask
    except SQLAlchemyError:
        db.rollback()
        raise

def get_task_service(goal_id: int, db: Session):
    task = repo_get_task(db, goal_id)
    if not task:
        raise GoalNotFoundException(goal_id)
    return task