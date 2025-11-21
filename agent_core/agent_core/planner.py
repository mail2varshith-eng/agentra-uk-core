from typing import List


def plan_tasks(goal: str) -> List[str]:
    """
    Very naive planner:
    - If 'research' is in the goal, create research tasks
    - Otherwise, split by 'and' / '.' as rough subtasks
    This is deliberately simple but shows the idea of task decomposition.
    """

    goal_lower = goal.lower().strip()
    tasks: List[str] = []

    if "research" in goal_lower:
        # Example: "Research 3 AI agent frameworks and summarise them"
        tasks.append("Research 3 popular AI agent frameworks")
        tasks.append("Collect key features of each framework")
        tasks.append("Summarise differences and similarities")
    else:
        # Fallback: split on 'and' / '.' as primitive subtasks
        temp = goal.replace(".", " and ").split(" and ")
        tasks = [t.strip() for t in temp if t.strip()]

    return tasks
