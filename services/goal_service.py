from sqlalchemy.orm import Session
from repositories.goal_repository import get_goal_by_id as repo_get_goal, create_goal as repo_create_goal, update_goal as repo_update_goal, delete_goal as repo_delete_goal, get_goals as repo_get_all_goals
from exception import GoalNotFoundException
from schemas import GoalCreate
from sqlalchemy.exc import SQLAlchemyError
import models

def get_goal_by_id(db: Session, goal_id: int):
    goal = repo_get_goal(db, goal_id)
    if not goal:
        raise GoalNotFoundException(goal_id)
    return goal

def create_goal_service(goal: GoalCreate, db: Session):
    new_goal = models.Goal(
    title = goal.title,
    description = goal.description,
    startDate = goal.startDate,
    targetDate = goal.targetDate,
    status = "active"
    )
    try:
        repo_create_goal(db, new_goal)
        db.commit()
        db.refresh(new_goal)
        return new_goal
    except SQLAlchemyError as e:
        db.rollback()
        raise

# UPDATE
def update_goal_service(db: Session, goal_id: int, goal_data):
    goal = repo_get_goal(db, goal_id)

    if not goal:
        raise GoalNotFoundException(goal_id)

    goal.title = goal_data.title
    goal.description = goal_data.description
    goal.startDate = goal_data.startDate
    goal.targetDate = goal_data.targetDate

    try:
        repo_update_goal(db, goal)
        db.commit()
        db.refresh(goal)
        return goal
    except SQLAlchemyError:
        db.rollback()
        raise

# DELETE
def delete_goal_service(db: Session, goal_id: int):
    goal = repo_get_goal(db, goal_id)

    if not goal:
        raise GoalNotFoundException(goal_id)
    try:
        repo_delete_goal(db, goal)
        db.commit()
        return {"message": "Goal deleted successfully"}
    except SQLAlchemyError:
        db.rollback()
        raise


def get_goals(db: Session, page, limit):
    total, goals = repo_get_all_goals(db, page, limit)
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": goals
    }