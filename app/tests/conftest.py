"""Test configuration for the ebab-user microservice."""
from glob import glob


def refactor(string: str) -> str:
    """Reformat filenames to plugin names."""
    return string.replace("/", ".").replace("\\", ".").replace(".py", "")


def find_plugins(sources):
    """Comprehend plugins from a list of target directories."""
    return [
        refactor(plugin)
        for source in sources
        for plugin in glob(source)
        if "__" not in plugin
    ]


pytest_plugins = find_plugins(["tests/cases/*.py", "tests/fixtures/*.py"])
