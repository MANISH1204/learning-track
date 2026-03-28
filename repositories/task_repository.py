from sqlalchemy.orm import Session
import models

def create_task(task, db:Session):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task(goalID, db:Session):
    return db.query(models.Task).filter(models.Task.goalId == goalID).all()

    
def get_tasks_by_goal(db: Session, goal_id: int):
    return db.query(models.Task).filter(models.Task.goalId == goal_id).all()