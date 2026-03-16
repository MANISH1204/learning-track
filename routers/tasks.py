from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import models
from schemas import Task, TaskCreate

router = APIRouter()

@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task  = models.Task(
        goalId = task.goalId,
        title = task.title,
        plannedHours = task.plannedHours,
        startDate = task.startDate,
        endDate = task.endDate,
        status = "pending"
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task


@router.get("/goals/{goalId}/tasks", response_model=list[Task])
def get_tasks(goalId: int,  db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(
        models.Task.goalId == goalId
    ).all()

    return task