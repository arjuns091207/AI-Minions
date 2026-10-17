from backend.app.bots.bot_profile import BotProfile
from backend.app.engine.model_client import ModelClient


class Minion:
    def __init__(
        self,
        profile: BotProfile,
        model_client: ModelClient | None = None,
    ):
        self.profile = profile
        self.model_client = model_client or ModelClient()

    def execute(self, task: str) -> str:
        if not task.strip():
            raise ValueError("Task cannot be empty.")

        return self.model_client.generate(
            prompt=task,
            system_prompt=self.profile.system_prompt,
        )