import pytest

from backend.app.bots.bot_profile import BotProfile
from backend.app.bots.registry import MinionRegistry

from unittest.mock import Mock

from backend.app.bots.factory import MinionFactory

from backend.app.bots.default_profiles import get_default_profiles

from backend.app.bots.bootstrap import create_default_registry

from unittest.mock import Mock, patch

from backend.app.bots.task_service import MinionTaskService

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


def test_factory_creates_minion_with_registered_profile(profile):
    registry = MinionRegistry()
    registry.register(profile)
    model_client = Mock()

    factory = MinionFactory(registry, model_client)
    minion = factory.create("backend-01")

    assert minion.profile == profile
    assert minion.model_client is model_client


def test_factory_rejects_unknown_minion_id():
    factory = MinionFactory(MinionRegistry())

    with pytest.raises(KeyError, match="Minion not found"):
        factory.create("unknown-minion")


def test_default_profiles_have_unique_ids():
    profiles = get_default_profiles()

    profile_ids = [profile.bot_id for profile in profiles]

    assert profile_ids == ["backend", "frontend", "testing"]
    assert len(profile_ids) == len(set(profile_ids))


def test_default_profiles_have_separate_workspaces():
    profiles = get_default_profiles()

    workspaces = [profile.workspace for profile in profiles]

    assert workspaces == [
        "projects/backend",
        "projects/frontend",
        "projects/testing",
    ]
    assert all(profile.allowed_tools == () for profile in profiles)

def test_default_registry_registers_all_specialists():
    registry = create_default_registry()

    assert [
        profile.bot_id for profile in registry.list_profiles()
    ] == ["backend", "frontend", "testing"]

    assert registry.get("backend").name == "Backend Minion"
    assert registry.get("frontend").name == "Frontend Minion"
    assert registry.get("testing").name == "Testing Minion"

def test_task_service_executes_task_with_selected_minion():
    with patch(
        "backend.app.bots.task_service.MinionFactory"
    ) as factory_class:
        model_client = Mock()
        factory = factory_class.return_value
        factory.model_client = model_client

        service = MinionTaskService()
        factory.create.return_value.execute.return_value = "Task completed."

        result = service.assign_task(
            "backend",
            "Create a health endpoint",
        )

        factory.create.assert_called_once_with("backend")
        factory.create.return_value.execute.assert_called_once_with(
            "Create a health endpoint"
        )
        assert result == "Task completed."


def test_task_service_propagates_unknown_minion_error():
    service = MinionTaskService()

    with pytest.raises(KeyError, match="Minion not found"):
        service.assign_task("unknown-minion", "Run a task")