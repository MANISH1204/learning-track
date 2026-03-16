from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import models
from schemas import SubTaskCreate, SubTaskUpdate

router = APIRouter()



@router.post("/subtasks")
def create_subtask(subtask: SubTaskCreate, db: Session = Depends(get_db)):
    new_subtask = models.SubTask(
        taskId=subtask.taskId,
        title=subtask.title,
        plannedHours=subtask.plannedHours,
        startDate=subtask.startDate,
        endDate=subtask.endDate,
        status="pending"
    )

    db.add(new_subtask)
    db.commit()
    db.refresh(new_subtask)

    return new_subtask

@router.get("/tasks/{taskId}/subtasks")
def get_subtasks(taskId: int, db: Session = Depends(get_db)):
    subtasks = db.query(models.SubTask).filter(
        models.SubTask.taskId == taskId
    ).all()

    return subtasks

@router.put("/subtasks/{subtaskId}")
def update_subtask(subtaskId: int, data: SubTaskUpdate, db: Session = Depends(get_db)):

    subtask = db.query(models.SubTask).filter(
        models.SubTask.id == subtaskId
    ).first()

    if not subtask:
        return {"error": "Subtask not found"}

    if data.title:
        subtask.title = data.title

    if data.plannedHours:
        subtask.plannedHours = data.plannedHours

    db.commit()

    return subtask

@router.delete("/subtasks/{subtaskId}")
def delete_subtask(subtaskId: int, db: Session = Depends(get_db)):
    subtask = db.query(models.SubTask).filter(
        models.SubTask.id == subtaskId
    ).first()

    if not subtask:
        return {"error": "Subtask not found"}

    db.delete(subtask)
    db.commit()

    return {"message": "Subtask deleted"}
