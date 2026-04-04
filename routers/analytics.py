from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import models
from repositories.analytics_repository import get_tasks_by_goal
from services.analytics_service import calculate_goal_progress
from repositories.goal_repository import get_goal_by_id
from exception import GoalNotFoundException

router = APIRouter()

@router.get("/analytics/goal-progress/{goalId}")
def goal_progress(goalId: int, db: Session = Depends(get_db)):
    goal = get_goal_by_id(db, goalId)
    if not goal:
        raise GoalNotFoundException(goalId)
    # tasks = get_tasks_by_goal(db, goalId)
    
    # 2. Run the logic
    return calculate_goal_progress(db, goalId)
