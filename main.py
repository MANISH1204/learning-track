from fastapi import FastAPI
from routers import goals, tasks, subtasks, worklogs, analytics

app = FastAPI()

app.include_router(goals.router)
app.include_router(tasks.router)
app.include_router(subtasks.router)
app.include_router(worklogs.router)
app.include_router(analytics.router)

@app.get("/")
def home():
    return {"message" : "Learnning Tracker API running"}