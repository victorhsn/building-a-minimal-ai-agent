from agent import Step, run

investigation_steps = [
    Step(
        action="Check API latency",
        observation="P95 latency increased to 850 ms.",
    ),
    Step(
        action="Check recent deployments",
        observation="A deployment occurred 15 minutes ago.",
    ),
    Step(
        action="Evaluate findings",
        observation="The latency increase correlates with the deployment.",
    ),
]

if __name__ == "__main__":
    state = run(investigation_steps)

    for index, (step, observation) in enumerate(zip(investigation_steps, state.observation),
        start=1,
    ):
        print(f"\n[Step {index}] {step.action}")
        print(f"Observation: {observation}")

        print(f"\nExecution stats: {state.status.value}")
        print(f"Steps executed: {state.step_index}")
