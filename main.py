from fastapi import FastAPI, Request
from exception import GoalNotFoundException
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse
from routers import goals, tasks, subtasks, worklogs, analytics
import logging

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="app.log",   # 👈 THIS is where logs are written
    filemode="a"          # append mode
)

logger = logging.getLogger("app")

app.include_router(goals.router)
app.include_router(tasks.router)
app.include_router(subtasks.router)
app.include_router(worklogs.router)
app.include_router(analytics.router)

@app.get("/")
def home():
    return {"message" : "Learnning Tracker API running"}

@app.exception_handler(SQLAlchemyError)
async def db_exception_handler(request: Request, exc: SQLAlchemyError):

    logger.error(f"Database error:{str(exc)}")
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