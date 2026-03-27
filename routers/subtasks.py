from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from services.subtask_service import service_create_subtask, service_get_subtask, service_update_subtask, service_delete_subtask
from schemas import SubTaskCreate, SubTaskUpdate

router = APIRouter(tags=['Subtasks'])

@router.post("/subtasks")
def create_subtask(subtask: SubTaskCreate, db: Session = Depends(get_db)):
    return service_create_subtask(subtask, db)

@router.get("/tasks/{taskId}/subtasks")
def get_subtasks(taskId: int, db: Session = Depends(get_db)):
    return service_get_subtask(taskId, db)

@router.put("/subtasks/{subtaskId}")
def update_subtask(subtaskId: int, data: SubTaskUpdate, db: Session = Depends(get_db)):
    return service_update_subtask(subtaskId, data, db)

@router.delete("/subtasks/{subtaskId}")
def delete_subtask(subtaskId: int, db: Session = Depends(get_db)):
    return service_delete_subtask(subtaskId, db)
