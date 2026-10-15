from dataclasses import dataclass


@dataclass(frozen=True)
class BotProfile:
    bot_id: str
    name: str
    role: str
    system_prompt: str
    allowed_tools: tuple[str, ...]
    workspace: str