"""
Sample workflow (v0.2) for Agentra.uk

Demonstrates how the autonomous agent uses:
- MemoryEngine
- ApiFetcher
- EmailTool
- Planning steps
- Reasoning logs

This file is strong evidence for Global Talent Visa (innovation & technical depth).
"""

from agent_core.agent import Agent
from agent_core.planner import Planner
from agent_core.tools.email_tool import EmailTool
from agent_core.tools.api_fetcher import ApiFetcher
from memory.memory_engine import MemoryEngine


def run_sample_workflow():
    """
    End-to-end demonstration of Agentra.uk v0.2.
    """

    # --- Initialise subsystems ---
    memory = MemoryEngine()
    planner = Planner()
    emailer = EmailTool()
    api = ApiFetcher()
    agent = Agent(planner=planner, memory=memory)

    # --- User goal ---
    goal = "Fetch today's crypto price and email it as a summary."

    # Log initial goal into memory
    memory.save(goal)

    # --- Step 1: Plan tasks ---
    tasks = planner.plan(goal)

    # For demo purposes, override tasks:
    tasks = [
        {"step": 1, "action": "fetch_data", "input": "https://api.coindesk.com/v1/bpi/currentprice.json"},
        {"step": 2, "action": "summarise"},
        {"step": 3, "action": "email"},
    ]

    reasoning_log = []

    # --- Step 2: Execute tasks ---
    fetched_data = None
    summary_text = None

    for task in tasks:
        if task["action"] == "fetch_data":
            reasoning_log.append("Fetching external API data...")
            result = api.fetch(task["input"])
            fetched_data = result
            memory.save(f"Fetched data: {result}")

        elif task["action"] == "summarise":
            reasoning_log.append("Creating summary...")
            if fetched_data:
                usd = fetched_data["data"]["bpi"]["USD"]["rate"] if "data" in fetched_data else "N/A"
                summary_text = f"Bitcoin (USD): {usd}"
                memory.save(f"Summary created: {summary_text}")

        elif task["action"] == "email":
            reasoning_log.append("Sending email...")
            send_result = emailer.send_email(
                to="user@example.com",
                subject="Crypto Update",
                body=summary_text or "No summary available."
            )
            memory.save(f"Email result: {send_result}")

    # --- Final response ---
    return {
        "goal": goal,
        "tasks": tasks,
        "reasoning_log": reasoning_log,
        "final_summary": summary_text,
        "memory_state": memory.export(),
    }


if __name__ == "__main__":
    output = run_sample_workflow()
    print(output)
