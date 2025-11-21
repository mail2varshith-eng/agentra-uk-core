from agent_core.agent import Agent


def main():
    print("=== Agentra.ai MVP – Autonomous Agent Demo ===")
    goal = input("Enter a goal for the agent:\n> ").strip()

    if not goal:
        print("No goal provided. Exiting.")
        return

    agent = Agent()
    result = agent.run(goal)

    print("\n=== Agent Output ===")
    print(result)
    print("\nLog written to /logs directory.")


if __name__ == "__main__":
    main()
