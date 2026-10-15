# AI Minions

A local-first, multi-agent AI workforce platform inspired by persistent AI agents.

## Vision

AI Minions allows a user to delegate tasks to specialized AI agents coordinated by a central agent called the Chief Minion.

The platform aims to support task planning, controlled tool execution, collaboration, persistent state, and evidence-based verification.

## Core Components

- **Chief Minion:** Understands objectives, plans tasks, and coordinates agents.
- **Specialized Minions:** Perform role-specific work such as frontend development, backend development, and testing.
- **Tool Platform:** Provides controlled access to files and other capabilities.
- **Security Layer:** Enforces permissions and workspace boundaries before operations execute.
- **Task Engine:** Tracks tasks, dependencies, failures, and completion.
- **Verification Engine:** Checks results against explicit acceptance criteria.
- **Memory and Storage:** Preserve relevant context, task state, and artifact metadata.
- **Audit Logging:** Records important operations and outcomes.

## Initial Technology Stack

- Python
- FastAPI
- Ollama for local language-model inference
- SQLite for persistent application state

Additional dependencies will be selected as the architecture requires them.

## Engineering Principles

1. Local-first execution where practical.
2. Explicit permissions enforced by application code.
3. Workspace isolation between projects and agents.
4. Evidence-based task completion.
5. Bounded execution and recovery.
6. Testable, modular architecture.
7. Transparent execution logs and documented limitations.

## Current Status

Project foundation is being established. No agent execution functionality has been implemented yet.
