# Agentra.ai Core – MVP Architecture

This document describes the architecture of the **Agentra.ai Core MVP (v0.1)**.

---

## 🧠 High-Level Flow

1. User provides a **goal** (text input).
2. `Agent` sends the goal to the **Planner**.
3. **Planner** breaks it into **tasks**.
4. **Agent** loops through tasks:
   - Chooses a tool (e.g., mock web search)
   - Executes the task
   - Logs the result
5. Agent combines results and sends to **Summariser**.
6. Output is shown to the user.
7. Full session is saved to `/logs`.

---

## 🧱 Components

| File | Purpose |
|------|---------|
| `agent_core/agent.py` | Orchestrates goal → plan → execution → log |
| `agent_core/planner.py` | Converts user goal into smaller tasks |
| `tools/web_search.py` | Fake research tool (simulated) |
| `tools/text_summarizer.py` | Basic text summarisation tool |
| `examples/run_agent.py` | CLI script to demo the agent |
| `logs/` | Stores all logs with timestamps |
| `docs/` | Documentation and roadmap |

---

## 🔁 Diagram

![Architecture Diagram](https://agentra-public.s3.eu-west-2.amazonaws.com/global_talent/agentra_architecture.png)

> (You can replace the above link with your uploaded diagram if needed)

---

## 🔮 Future Architecture Upgrades

- Real APIs for tools (search, documents, GPT)
- Agent collaboration and orchestration
- Web dashboard + API
- Long-term memory module
