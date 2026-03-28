from repositories.analytics_repository import get_subtasks_by_task, get_tasks_by_goal, get_worklogs_by_subtask

def calculate_goal_progress(db, goal_id: int):
    planned_hours = 0
    completed_hours = 0

    # 1. Get Tasks
    tasks = get_tasks_by_goal(db, goal_id)

    for task in tasks:
        # 2. Get Subtasks manually
        subtasks = get_subtasks_by_task(db, task.id)

        for sub in subtasks:
            planned_hours += sub.plannedHours

            # 3. Get Worklogs manually
            logs = get_worklogs_by_subtask(db, sub.id)
            for log in logs:
                completed_hours += log.hoursSpent

    # Logic
    progress = (completed_hours / planned_hours * 100) if planned_hours > 0 else 0
    
    return {
        "plannedHours": planned_hours,
        "completedHours": completed_hours,
        "progressPercentage": min(progress, 100)
    }
