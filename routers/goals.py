from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import get_db
from exception import GoalNotFoundException
import models
from schemas import Goal, GoalCreate, GoalPagination
from services.goal_service import get_goal_by_id

router = APIRouter(prefix="/goals", tags=["Goals"])


@router.get("/", response_model=GoalPagination)
def get_goals(page:int=1, limit:int=10, db: Session = Depends(get_db)):
    offset = (page -1)*limit
    goals = db.query(models.Goal).order_by(models.Goal.id).offset(offset).limit(limit).all()
    return {
        "page":page,
        "limit":limit,
        "data":goals
    }

@router.post("/")
def create_goal(goal:GoalCreate, db: Session = Depends(get_db)):
    new_goal = models.Goal(
        title=goal.title,
        description=goal.description,
        startDate = goal.startDate,
        targetDate = goal.targetDate,
        status="active"
    )
    try:
        db.add(new_goal)
        db.commit()
        db.refresh(new_goal)
        return new_goal
    except SQLAlchemyError as e:
        db.rollback()
        raise

@router.get("/{goalId}", response_model=Goal)
def get_goal(goalId: int, db: Session = Depends(get_db)):
    return get_goal_by_id(db, goalId)

@router.put("/{goalId}")
def update_goal(goalId: int, updated_goal: GoalCreate, db: Session = Depends(get_db)):
    goal = db.query(models.Goal).filter(
        models.Goal.id == goalId
    ).first()

    if not goal:
        raise GoalNotFoundException(goalId)
    
    goal.title = updated_goal.title
    goal.description = updated_goal.description
    goal.startDate = updated_goal.startDate
    goal.targetDate = updated_goal.targetDate

    try:
        db.commit()
        return goal
    except SQLAlchemyError as e:
        db.rollback()
        raise


@router.delete("/{goalId}")
def delete_goal(goalId: int, db: Session = Depends(get_db)):

    goal = db.query(models.Goal).filter(
        models.Goal.id == goalId
    ).first()

    if not goal:
        raise GoalNotFoundException(goalId)
    
    try:
        db.delete(goal)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise

    return {"message": "Goal deleted"}
