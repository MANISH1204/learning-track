from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import WorkLogCreate
from database import get_db
import models

router = APIRouter()

@router.post("/worklogs")
def create_worklog(worklog: WorkLogCreate,  db: Session = Depends(get_db)):

    subtask = db.query(models.SubTask).filter(
        models.SubTask.id == worklog.subtaskId
    ).first()

    if not subtask:
        return {"error": "Subtask not found"}


    new_log = models.WorkLog(
        subtaskId = worklog.subtaskId,
        hoursSpent = worklog.hoursSpent,
        workDate = worklog.workDate,
        notes = worklog.notes
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log