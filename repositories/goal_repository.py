from sqlalchemy.orm import Session
import models

def get_goal_by_id(db: Session, goal_id: int):
    return db.query(models.Goal).filter(models.Goal.id == goal_id).first()

def create_goal(db:Session, goal):
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

def update_goal(db: Session, goal):
    db.commit()
    db.refresh(goal)
    return goal

def delete_goal(db: Session, goal):
    db.delete(goal)
    db.commit()

def get_goals(db: Session, page, limit):
    offset = (page -1)*limit
    return db.query(models.Goal).order_by(models.Goal.id).offset(offset).limit(limit).all()

