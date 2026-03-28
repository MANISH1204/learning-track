from sqlalchemy.orm import Session
import models

def get_tasks_by_goal(db: Session, goal_id: int):
    return db.query(models.Task).filter(models.Task.goalId == goal_id).all()

def get_subtasks_by_task(db: Session, task_id: int):
    return db.query(models.SubTask).filter(models.SubTask.taskId == task_id).all()

def get_worklogs_by_subtask(db: Session, subtask_id: int):
    return db.query(models.WorkLog).filter(models.WorkLog.subtaskId == subtask_id).all()
