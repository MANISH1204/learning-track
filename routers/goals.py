from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import Goal, GoalCreate, GoalPagination

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
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return new_goal

@router.get("/{goalId}", response_model=Goal)
def get_goal(goalId: int, db: Session = Depends(get_db)):
    goal = db.query(models.Goal).filter(
        models.Goal.id == goalId
    ).first()
    if not goal:
        return {"error": "goal not found"}
    return goal

@router.put("/{goalId}")
def update_goal(goalId: int, updated_goal: GoalCreate, db: Session = Depends(get_db)):
    goal = db.query(models.Goal).filter(
        models.Goal.id == goalId
    ).first()

    if not goal:
        return {"error": "Goal not found"}
    
    goal.title = updated_goal.title
    goal.description = updated_goal.description
    goal.startDate = updated_goal.startDate
    goal.targetDate = updated_goal.targetDate

    db.commit()
    return goal

@router.delete("/{goalId}")
def delete_goal(goalId: int, db: Session = Depends(get_db)):

    goal = db.query(models.Goal).filter(
        models.Goal.id == goalId
    ).first()

    if not goal:
        return {"error": "Goal not found"}

    db.delete(goal)
    db.commit()

    return {"message": "Goal deleted"}
