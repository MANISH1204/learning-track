from repositories.subtask_repository import create_subtask as repo_create_subtask, get_subtask as repo_get_subtask, update_subtask as repo_update_subtask, get_subtask_byId, delete_subtask
from sqlalchemy.orm import Session
import models
from schemas import SubTaskCreate

def service_create_subtask(subtask:SubTaskCreate, db:Session):
    new_subtask = models.SubTask(
        taskId = subtask.taskId,
        title=subtask.title,
        plannedHours = subtask.plannedHours,
        startDate = subtask.startDate,
        endDate= subtask.endDate,
        status = "pending"
    )
    return repo_create_subtask(new_subtask, db)

def service_get_subtask(taskId, db:Session):
    subtasks = repo_get_subtask(taskId, db)
    return subtasks

def service_update_subtask(subtaskId, data, db:Session):
    subtask = get_subtask_byId(subtaskId, db)

    if not subtask:
        return {"error", "Subtask not found"}
    if data.title:
        subtask.title = data.title
    if data.planneHours:
        subtask.plannedHours = data.plannedHours
    return repo_update_subtask(subtask, db)

def service_delete_subtask(subtaskId, db:Session):
    subtask = get_subtask_byId(subtaskId, db)
    if not subtask:
        return{"error": "Subtask not found"}
    delete_subtask(subtask, db)
    return{"message": "Subtask deleted"}