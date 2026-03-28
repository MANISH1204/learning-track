from sqlalchemy.orm import Session
import models
from repositories.worklog_repository import create_worlog, get_worklogId

def service_create_worklog(worklog, db:Session):
    subtask = get_worklogId(worklog, db)

    if not subtask:
        return{"error": "Subtask not found"}
    
    newlog = models.WorkLog(
        subtaskId = worklog.subtaskId,
        hoursSpent = worklog.hoursSpent,
        workDate = worklog.workDate,
        notes = worklog.notes
    )

    return create_worlog(newlog, db)