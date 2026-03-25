from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import get_db
from exception import GoalNotFoundException
import models
from schemas import Goal, GoalCreate, GoalPagination
from services.goal_service import get_goal_by_id, create_goal_service, update_goal_service, delete_goal_service, get_goals as sevice_get_goal

router = APIRouter(prefix="/goals", tags=["Goals"])


@router.get("/", response_model=GoalPagination)
def get_goals(page:int=1, limit:int=10, db: Session = Depends(get_db)):
    return sevice_get_goal(db, page, limit)

@router.get("/{goalId}", response_model=Goal)
def get_goal(goalId: int, db: Session = Depends(get_db)):
    return get_goal_by_id(db, goalId)


@router.post("/")
def create_goal(goal: GoalCreate, db: Session = Depends(get_db)):
    return create_goal_service(goal, db)


@router.put("/{goalId}")
def update_goal(goalId: int, goal: GoalCreate, db: Session = Depends(get_db)):
    return update_goal_service(db, goalId, goal)


@router.delete("/{goalId}")
def delete_goal(goalId: int, db: Session = Depends(get_db)):
    return delete_goal_service(db, goalId)