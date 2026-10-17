import pytest

from backend.app.bots.bot_profile import BotProfile
from backend.app.bots.registry import MinionRegistry


@pytest.fixture
def profile():
    return BotProfile(
        bot_id="backend-01",
        name="Backend Minion",
        role="Backend development",
        system_prompt="You are a backend engineer.",
        allowed_tools=(),
        workspace="projects/backend-01",
    )


def test_register_and_get_profile(profile):
    registry = MinionRegistry()

    registry.register(profile)

    assert registry.get("backend-01") == profile


def test_list_profiles(profile):
    registry = MinionRegistry()

    registry.register(profile)

    assert registry.list_profiles() == (profile,)


def test_duplicate_registration_is_rejected(profile):
    registry = MinionRegistry()
    registry.register(profile)

    with pytest.raises(ValueError, match="already registered"):
        registry.register(profile)


def test_missing_profile_raises_key_error():
    registry = MinionRegistry()

    with pytest.raises(KeyError, match="Minion not found"):
        registry.get("unknown-minion")