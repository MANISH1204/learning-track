from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
import models
from repositories.analytics_repository import get_tasks_by_goal
from services.analytics_service import calculate_goal_progress

router = APIRouter()

@router.get("/analytics/goal-progress/{goalId}")
def goal_progress(goalId: int, db: Session = Depends(get_db)):
    tasks = get_tasks_by_goal(db, goalId)
    
    # 2. Run the logic
    return calculate_goal_progress(db, goalId)
