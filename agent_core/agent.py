import json
import os
from datetime import datetime
from agent_core.planner import plan_tasks
from tools.web_search import mock_web_search
from tools.text_summarizer import simple_summarise


class Agent:
    """
    Very simple MVP agent:
    - Takes a goal
    - Plans tasks
    - Executes mock tools
    - Produces a final summary
    - Logs reasoning to /logs
    """

    def __init__(self):
        self.log = {
            "goal": None,
            "tasks": [],
            "steps": [],
            "final_output": None,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }

    def run(self, goal: str) -> str:
        self.log["goal"] = goal

        # 1. Plan tasks
        tasks = plan_tasks(goal)
        self.log["tasks"] = tasks

        # 2. Execute tasks with simple logic
        research_results = []
        for idx, task in enumerate(tasks, start=1):
            step_record = {"task": task, "step_index": idx}

            if "research" in task.lower() or "find" in task.lower():
                step_record["tool_used"] = "mock_web_search"
                result = mock_web_search(task)
                step_record["result"] = result
                research_results.append(result)
            else:
                step_record["tool_used"] = "none"_]()_
