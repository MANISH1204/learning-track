from sqlalchemy.orm import Session
import models

def create_subtask(subtask, db:Session):
    db.add(subtask)
    db.commit()
    db.refresh(subtask)
    return subtask

def get_subtask(taskId, db:Session):
    return db.query(models.SubTask).filter(
        models.SubTask.taskId == taskId
    ).all()

def update_subtask(data, db:Session):
    db.commit()
    db.refresh(data)
    return data

def get_subtask_byId(subtaskId, db:Session):
    subtask = db.query(models.SubTask).filter(
        models.SubTask.id == subtaskId
    ).first()
    return subtask

def delete_subtask(subtask, db:Session):
    db.delete(subtask)
    db.commit()
    return {"message": "Subtask deleted"}

