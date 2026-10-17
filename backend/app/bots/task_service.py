from backend.app.bots.bootstrap import create_default_registry
from backend.app.bots.factory import MinionFactory
from backend.app.bots.minion import Minion


class MinionTaskService:
    def __init__(self):
        self.registry = create_default_registry()
        self.factory = MinionFactory(self.registry)

    def assign_task(self, bot_id: str, task: str) -> str:
        minion: Minion = self.factory.create(bot_id)
        return minion.execute(task)