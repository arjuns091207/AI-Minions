from backend.app.bots.minion import Minion
from backend.app.bots.registry import MinionRegistry
from backend.app.engine.model_client import ModelClient


class MinionFactory:
    def __init__(
        self,
        registry: MinionRegistry,
        model_client: ModelClient | None = None,
    ):
        self.registry = registry
        self.model_client = model_client

    def create(self, bot_id: str) -> Minion:
        profile = self.registry.get(bot_id)

        return Minion(
            profile=profile,
            model_client=self.model_client,
        )