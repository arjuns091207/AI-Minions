from backend.app.bots.bot_profile import BotProfile


class MinionRegistry:
    def __init__(self):
        self._profiles: dict[str, BotProfile] = {}

    def register(self, profile: BotProfile) -> None:
        if profile.bot_id in self._profiles:
            raise ValueError(
                f"Minion ID already registered: {profile.bot_id}"
            )

        self._profiles[profile.bot_id] = profile

    def get(self, bot_id: str) -> BotProfile:
        try:
            return self._profiles[bot_id]
        except KeyError:
            raise KeyError(f"Minion not found: {bot_id}") from None

    def list_profiles(self) -> tuple[BotProfile, ...]:
        return tuple(self._profiles.values())