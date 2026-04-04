from sqlalchemy.orm import Session
import models

def create_subtask(db: Session, subtask):
    db.add(subtask)
    return subtask

def get_subtask(db: Session, taskId):
    return db.query(models.SubTask).filter(
        models.SubTask.taskId == taskId
    ).all()

def update_subtask(db: Session, data):
    return data

def get_subtask_by_id(db: Session, subtaskId):
    subtask = db.query(models.SubTask).filter(
        models.SubTask.id == subtaskId
    ).first()
    return subtask

def delete_subtask(db: Session, subtask):
    db.delete(subtask)


