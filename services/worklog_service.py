from sqlalchemy.orm import Session
import models
from repositories.worklog_repository import create_worlog, get_worklogId
from exception import SubtaskNotFoundException

def service_create_worklog(worklog, db:Session):
    subtask = get_worklogId(worklog, db)

    if not subtask:
        raise SubtaskNotFoundException(worklog.subtaskId)
    
    newlog = models.WorkLog(
        subtaskId = worklog.subtaskId,
        hoursSpent = worklog.hoursSpent,
        workDate = worklog.workDate,
        notes = worklog.notes
    )

    create_worlog(newlog, db)
    db.commit()
    db.refresh(newlog)
    return newlog