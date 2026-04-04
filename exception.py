class GoalNotFoundException(Exception):
    def __init__(self, goal_id: int):
        self.goal_id = goal_id
        self.code = "GOAL_NOT_FOUND"
        self.message = f"Goal with id{goal_id} not found"
        super().__init__(self.message)


class TaskNotFoundException(Exception):
    def __init__(self, task_id: int):
        self.task_id = task_id
        self.code = "TASK_NOT_FOUND"
        self.message = f"Subtask for Taskid {task_id} not found"
        super().__init__(self.message)
        
class SubtaskNotFoundException(Exception):
    def __init__(self, subtask_id: int):
        self.subtask_id = subtask_id
        self.code = "SUBTASK_NOT_FOUND"
        self.message = f"Subtask with id {subtask_id} not found"
        super().__init__(self.message)