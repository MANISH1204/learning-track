from sqlalchemy.orm import Session
import models

def create_task(db: Session, task):
    db.add(task)
    return task

def get_task(db: Session, goalID):
    return db.query(models.Task).filter(models.Task.goalId == goalID).all()
    
def get_tasks_by_goal(db: Session, goal_id: int):
    return db.query(models.Task).filter(models.Task.goalId == goal_id).all()

def get_task_by_taskID(db: Session, taskID: int):
    return db.query(models.Task).filter(models.Task.id == taskID).first()