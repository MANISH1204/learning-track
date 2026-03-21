from sqlalchemy.orm import Session
import models

def get_goal_by_id(db: Session, goal_id: int):
    return db.query(models.Goal).filter(models.Goal.id == goal_id).first()