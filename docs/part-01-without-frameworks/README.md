# Building an Agent Without Framework

### Part 01 - Building a Minimal AI Agent

Before using agent frameworks, let's understand the mechanisms that make agent execution possible.

In this chapter, we'll build a minimal loop in Python, starting with a simple implementation and progressively introducing execution states, termination, conditions, and basic failure handling.

The goal is to understand how an application controls execution before integrating a language model or external tools.

### What We'll Build

A small Python application that simulates the execution of an investigation task.

The applicatio will execute predfined steps, track their results, and terminate when the task completes, fails, or reaches its execution limit.

**This is not yet an AI Agent**. It is the execution foundation that we'll extend with an **LLM** and tools in subsequent chapters.

### Contents
1. Building Our First Execution Loop
2. Understanding What the Loop Actually Does
3. Who Controls the Execution?
4. Improving the Implementation 
5. Running and Testing the Execution Loop
6. What We Built, and What's Still Missing

### Implementation

The complete Python implementation and test will be available in the repository.

Eche published chapter will have a correspoding **Git Tag**, allowing readers to reproduce the implementation at that stage.

### Related Article

The accompanying technical articles are published on [**victorhsn.com**.](https://www.victorhsn.com)

It will explain the implementation, architectural decisions, execution behavior, and limitations in greater detail.