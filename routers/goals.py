from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from database import get_db
from schemas import Goal, GoalCreate, GoalPagination
from services.goal_service import get_goal_by_id, create_goal_service, update_goal_service, delete_goal_service, get_goals as service_get_goal

router = APIRouter(prefix="/goals", tags=["Goals"])

@router.get("/", response_model=GoalPagination)
def get_goals(page: int = Query(1, gt=0), limit: int = Query(10, gt=0, le=100), db: Session = Depends(get_db)):
    return service_get_goal(db, page, limit)

@router.get("/{goalId}", response_model=Goal)
def get_goal(goalId: int, db: Session = Depends(get_db)):
    return get_goal_by_id(db, goalId)

@router.post("/", response_model=Goal, status_code=status.HTTP_201_CREATED)
def create_goal(goal: GoalCreate, db: Session = Depends(get_db)):
    return create_goal_service(goal, db)

@router.patch("/{goalId}",response_model=Goal)
def update_goal(goalId: int, goal: GoalCreate, db: Session = Depends(get_db)):
    return update_goal_service(db, goalId, goal)

@router.delete("/{goalId}", status_code = status.HTTP_200_OK)
def delete_goal(goalId: int, db: Session = Depends(get_db)):
    return delete_goal_service(db, goalId)
