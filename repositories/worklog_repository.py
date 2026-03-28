from sqlalchemy.orm import Session
import models
from schemas import WorkLogCreate


def get_worklogId(worklog:WorkLogCreate, db:Session):
    subtask = db.query(models.SubTask).filter(
        models.SubTask.id == worklog.subtaskId
    ).first()
    return subtask

def create_worlog(newlog:WorkLogCreate, db:Session):
    db.add(newlog)
    db.commit()
    db.refresh(newlog)
    return newlog