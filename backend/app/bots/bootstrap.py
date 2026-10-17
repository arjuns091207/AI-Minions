from backend.app.bots.default_profiles import get_default_profiles
from backend.app.bots.registry import MinionRegistry


def create_default_registry() -> MinionRegistry:
    registry = MinionRegistry()

    for profile in get_default_profiles():
        registry.register(profile)

    return registry