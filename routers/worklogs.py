from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import WorkLogCreate
from database import get_db
import models
from services.worklog_service import service_create_worklog

router = APIRouter(prefix="/worklogs", tags=["Worklogs"])

@router.post("/")
def create_worklog(worklog: WorkLogCreate,  db: Session = Depends(get_db)):
    return service_create_worklog(worklog, db)