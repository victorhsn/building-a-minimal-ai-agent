import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from agent import Status, Step, run

class ExecutionLoopTests(unittest.TestCase):
    def setUp(self):
        self.steps = [
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

    def test_completes_all_steps(self):
        state = run(self.steps)

        self.assertEqual(state.status, Status.COMPLETED)
        self.assertEqual(state.step_index, 3)
        self.assertEqual(len(state.observation), 3)

    def test_stops_at_execution_limit(self):
        state = run(self.steps, max_steps=2)

        self.assertEqual(state.status, Status.LIMIT_REACHED)
        self.assertEqual(state.step_index, 2)
        self.assertEqual(len(state.observation), 2) 

    def test_stops_when_execution_fails(self):

        def failing_executor(step):
            raise RuntimeError("Metrics service unavailable.")

        state = run(self.steps, executor=failing_executor)

        self.assertEqual(state.status, Status.FAILED)
        self.assertEqual(state.step_index, 0)
        self.assertEqual(state.observation, [])
        self.assertEqual(
            state.error,
            "Metrics service unavailable.",
        )

if __name__ == "__main__":
    unittest.main()
