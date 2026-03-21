from sqlalchemy.orm import Session
from repositories.goal_repository import get_goal_by_id as repo_get_goal
from exception import GoalNotFoundException

def get_goal_by_id(db: Session, goal_id:int):
    goal = repo_get_goal(db, goal_id)
    if not goal:
        raise GoalNotFoundException(goal_id)
    
    return goal