from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Goal(Base):

    __tablename__ = "Goals"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    startDate = Column(Date)
    targetDate = Column(Date)
    status = Column(String)

    tasks = relationship(
        "Task",
        back_populates="goal",
        cascade="all, delete-orphan"
    )

class Task(Base):

    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True)
    goalId = Column(Integer, ForeignKey("Goals.id", ondelete="CASCADE"))
    title = Column(String)
    plannedHours = Column(Integer)
    startDate = Column(Date)
    endDate = Column(Date)
    status = Column(String)

    goal = relationship("Goal", back_populates="tasks")

    subtasks = relationship(
        "SubTask",
        back_populates="task",
        cascade="all, delete-orphan"
    )

class SubTask(Base):

    __tablename__ = "SubTasks"

    id = Column(Integer, primary_key=True)
    taskId = Column(Integer, ForeignKey("Tasks.id", ondelete="CASCADE"))
    title = Column(String)
    plannedHours = Column(Integer)
    startDate = Column(Date)
    endDate = Column(Date)
    status = Column(String)   

    task = relationship("Task", back_populates="subtasks")

    worklogs = relationship(
        "WorkLog",
        back_populates="subtask",
        cascade="all, delete-orphan"
    )    

class WorkLog(Base):
    __tablename__ = "WorkLogs"

    id = Column(Integer, primary_key=True)
    subtaskId = Column(Integer, ForeignKey("SubTasks.id", ondelete="CASCADE"))
    hoursSpent = Column(Float)
    workDate = Column(Date)
    notes = Column(String)
    subtask = relationship("SubTask", back_populates="worklogs")    

class User(Base):

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)