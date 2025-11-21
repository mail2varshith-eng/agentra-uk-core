# Agentra.ai Core – Autonomous AI Agent MVP

Agentra.ai Core is an early prototype of an autonomous AI agent system that can:

- Understand a user goal  
- Break it into steps (task decomposition)  
- Execute simple actions  
- Summarise results  
- Log its reasoning  

This MVP demonstrates the core concept behind Agentra.ai:

> **AI that works, not just talks.**

---

## 🚀 Features (MVP 0.1)

- Goal → Tasks → Execution pipeline  
- Simple rule-based task decomposition  
- Mock “tools” (fake web search & summariser)  
- Reasoning logs stored as JSON  
- Example script to run the agent from the command line  

---

## 📂 Folder Structure

```text
agentra-uk-core/
  agent_core/
    agent.py
    planner.py
  tools/
    web_search.py
    text_summarizer.py
  examples/
    run_agent.py
  logs/
    (auto-created log files)
  docs/
    architecture.md
    roadmap.md
