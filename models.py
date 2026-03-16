from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Goal(Base):

    __tablename__ = "Goals"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    startDate = Column(Date)
    targetDate = Column(Date)
    status = Column(String)

class Task(Base):

    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True)
    goalId = Column(Integer, ForeignKey("Goals.id"))
    title = Column(String)
    plannedHours = Column(Integer)
    startDate = Column(Date)
    endDate = Column(Date)
    status = Column(String)

class SubTask(Base):

    __tablename__ = "SubTasks"

    id = Column(Integer, primary_key=True)
    taskId = Column(Integer, ForeignKey("Tasks.id"))
    title = Column(String)
    plannedHours = Column(Integer)
    startDate = Column(Date)
    endDate = Column(Date)
    status = Column(String)   

class WorkLog(Base):
    __tablename__ = "WorkLogs"

    id = Column(Integer, primary_key=True)
    subtaskId = Column(Integer, ForeignKey("SubTasks.id"))
    hoursSpent = Column(Float)
    workDate = Column(Float)
    notes = Column(String)

class User(Base):

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)