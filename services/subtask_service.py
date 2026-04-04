from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import models
from schemas import SubTaskCreate
from repositories.subtask_repository import (
    create_subtask as repo_create_subtask,
    get_subtask as repo_get_subtask,
    update_subtask as repo_update_subtask,
    get_subtask_by_id as repo_get_subtask_by_id,
    delete_subtask as repo_delete_subtask
)
from exception import SubtaskNotFoundException, TaskNotFoundException
from repositories.task_repository import get_task_by_taskID

def service_create_subtask(subtask: SubTaskCreate, db: Session):
    taskId = get_task_by_taskID(db, subtask.taskId)
    if not taskId:
        raise TaskNotFoundException(subtask.taskId)

    new_subtask = models.SubTask(
        taskId = subtask.taskId,
        title=subtask.title,
        plannedHours = subtask.plannedHours,
        startDate = subtask.startDate,
        endDate= subtask.endDate,
        status = "pending"
    )
    try:
        repo_create_subtask(db, new_subtask)
        db.commit()
        db.refresh(new_subtask)
        return new_subtask
    except SQLAlchemyError:
        db.rollback()
        raise

def service_get_subtask(taskId, db: Session):
    task = get_task_by_taskID(db, taskId)
    if not task:
        raise TaskNotFoundException(taskId)    
    subtasks = repo_get_subtask(db, taskId)
    return subtasks

def service_update_subtask(subtaskId, data, db: Session):
    subtask = repo_get_subtask_by_id(db, subtaskId)
    if not subtask:
        raise SubtaskNotFoundException(subtaskId)
    
    if data.title is not None:
        subtask.title = data.title
    if data.plannedHours is not None:
        subtask.plannedHours = data.plannedHours
    try:
        repo_update_subtask(db, subtask)
        db.commit()
        db.refresh(subtask)
        return subtask
    except SQLAlchemyError:
        db.rollback()
        raise

def service_delete_subtask(subtaskId, db: Session):
    subtask = repo_get_subtask_by_id(db, subtaskId)
    if not subtask:
        raise SubtaskNotFoundException(subtaskId)
    try:
        # db.query(models.WorkLog).filter(models.WorkLog.subtaskId == subtaskId).delete()
        repo_delete_subtask(db, subtask)
        db.commit()
        return {"message": "Subtask deleted successfully"}
    except SQLAlchemyError:
        db.rollback()
        raise