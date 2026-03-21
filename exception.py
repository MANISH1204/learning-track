class GoalNotFoundException(Exception):
    def __init__(self, goal_id: int):
        self.goal_id = goal_id
        self.code = "GOAL_NOT_FOUND"
        self.message = f"Goal with id{goal_id} not found"
        