from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import models

router = APIRouter()

@router.get("/analytics/goal-progress/{goalId}")
def goal_progress(goalId: int, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).filter(
         models.Task.goalId == goalId
     ).all()
    
    planned_hours = 0
    completed_hours = 0

    for task in tasks:
        subtasks = db.query(models.SubTask).filter(
            models.SubTask.taskId == task.id
        ).all()

        for sub in subtasks:
            planned_hours += sub.plannedHours

            logs = db.query(models.WorkLog).filter(
                models.WorkLog.subtaskId == sub.id
            ).all()

            for log in logs:
                completed_hours += log.hoursSpent

    if planned_hours > 0:
        progress = (completed_hours / planned_hours) * 100
    else:
        progress = 0

    if progress > 100:
        progress = 100    

    return {
        "plannedHours": planned_hours,
        "completedHours": completed_hours,
        "progressPercentage": progress
    }

