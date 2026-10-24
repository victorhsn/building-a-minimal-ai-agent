from dataclasses import dataclass, field
from enum import Enum
from typing import Callable

class Status(str, Enum):
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    LIMIT_REACHED = "limit_reached"

@dataclass(frozen=True)
class Step:
    action: str
    observation: str


@dataclass 
class ExecutionState:
    status: Status = Status.RUNNING
    step_index: int = 0
    observation: list[str] = field(default_factory=list)
    error: str | None = None


def execute_step(step: Step):
    return step.observation

def run(
        steps: list[Step],
        max_steps: int = 10,
        executor: Callable[[Step], str] = execute_step,

) -> ExecutionState:
    if max_steps < 1:
        raise ValueError("max_steps must be at least 1")

    state = ExecutionState()

    while state.status == Status.RUNNING:
        if state.step_index >= len(steps):
            state.status = Status.COMPLETED
            break

        if state.step_index >= max_steps:
            state.status = Status.LIMIT_REACHED
            break

        step = steps[state.step_index]

        try:
            observation = executor(step)
        except Exception as exc:
            state.status = Status.FAILED
            state.error = str(exc)
            break

        state.observation.append(observation)
        state.step_index += 1
        
    return state