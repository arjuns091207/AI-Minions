from backend.app.bots.bot_profile import BotProfile


def get_default_profiles() -> tuple[BotProfile, ...]:
    return (
        BotProfile(
            bot_id="backend",
            name="Backend Minion",
            role="Backend development",
            system_prompt=(
                "You are a backend engineering specialist. "
                "Design reliable APIs, implement backend logic, "
                "handle errors, and write maintainable code. "
                "Explain important technical decisions clearly."
            ),
            allowed_tools=(),
            workspace="projects/backend",
        ),
        BotProfile(
            bot_id="frontend",
            name="Frontend Minion",
            role="Frontend development",
            system_prompt=(
                "You are a frontend engineering specialist. "
                "Build accessible, responsive, maintainable user "
                "interfaces. Follow established design patterns "
                "and explain important implementation decisions."
            ),
            allowed_tools=(),
            workspace="projects/frontend",
        ),
        BotProfile(
            bot_id="testing",
            name="Testing Minion",
            role="Software testing",
            system_prompt=(
                "You are a software testing specialist. "
                "Design meaningful test cases, identify edge cases, "
                "verify expected behavior, and report defects with "
                "clear reproduction steps. Never claim a test passed "
                "unless it was actually executed successfully."
            ),
            allowed_tools=(),
            workspace="projects/testing",
        ),
    )