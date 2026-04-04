from fastapi import FastAPI, Request
from exception import GoalNotFoundException, TaskNotFoundException, SubtaskNotFoundException
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse
from routers import goals, tasks, subtasks, worklogs, analytics
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app.log", maxBytes=5_000_000, backupCount=5)

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[handler, logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

app.include_router(goals.router, prefix="/api/v1")
app.include_router(tasks.router, prefix="/api/v1")
app.include_router(subtasks.router, prefix="/api/v1")
app.include_router(worklogs.router, prefix="/api/v1")
app.include_router(analytics.router, prefix="/api/v1")

@app.get("/")
def home():
    return {"message" : "Learning Tracker API running"}

@app.exception_handler(SQLAlchemyError)
async def db_exception_handler(request: Request, exc: SQLAlchemyError):

    logger.exception("Database error occurred")
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "DB_ERROR",
                "message": "Database operation failed"
            }
        }
    )


@app.exception_handler(GoalNotFoundException)
async def goal_not_found_handler(request:Request, exc: GoalNotFoundException):
    logger.info(f"Goal not found:{str(exc.message)}")
    return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message
            }
        }
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception")

    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "Something went wrong"
            }
        }
    )

@app.exception_handler(TaskNotFoundException)
async def goal_not_found_handler(request:Request, exc: TaskNotFoundException):
    logger.info(f"Goal not found:{str(exc.message)}")
    return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message
            }
        }
    )

@app.exception_handler(SubtaskNotFoundException)
async def goal_not_found_handler(request:Request, exc: SubtaskNotFoundException):
    logger.info(f"Goal not found:{str(exc.message)}")
    return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message
            }
        }
    )

