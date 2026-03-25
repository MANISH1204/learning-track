from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date, datetime

class Goal(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    startDate: Optional[date] = None
    targetDate: Optional[date] = None
    status: Optional[str] = None

class GoalCreate(BaseModel):
    title: str
    description: Optional[str] = None
    startDate: Optional[date] = None
    targetDate: Optional[date] = None

    # @field_validator("title")
    # @classmethod
    # def validate_title(cls, value: str):
    #     if not value or not value.strip():
    #         raise ValueError("Title cannot be empty or just spaces")
    #     return value.strip()

class Task(BaseModel):
    id: int
    goalId: int
    title: str
    plannedHours: int | None = None
    startDate: date | None = None
    endDate: date | None = None
    status: str | None = None
    progress: float | None = None

class TaskCreate(BaseModel):
    goalId: int
    title: str
    plannedHours: int | None = None
    startDate: date | None = None
    endDate: date | None = None

class SubTaskCreate(BaseModel):
    taskId: int
    title: str
    plannedHours: int | None = None
    startDate: date | None = None
    endDate: date | None = None

class SubTaskUpdate(BaseModel):
    title: str | None = None
    plannedHours: int | None = None
    startDate: date | None = None
    endDate: date | None = None

class WorkLogCreate(BaseModel):
    subtaskId: int
    hoursSpent: float = Field(gt=0)
    workDate: date | None = None
    notes: str | None = None

class GoalPagination(BaseModel):
    page: int
    limit: int
    data: list[Goal]


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str