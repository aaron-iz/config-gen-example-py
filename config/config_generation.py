from abc import ABC, abstractmethod
from typing import List, Dict

from .base_config_model import BaseConfigModel

# ------------------------
# Base class for all generators
# ------------------------
class ConfigGenerator(ABC):
    """
    Base class for configuration generators.
    Child classes must implement the `generate` method.
    """

    @abstractmethod
    def generate(self) -> Dict[str, BaseConfigModel]:
        """
        Generate configuration instances for multiple environments.

        Returns:
            dict: mapping from env name to BaseConfigModel instance.
                  Use None as the key for default environment.
        """
        pass

# ------------------------
# List of all generator instances
# ------------------------
# Developers should register their generators here
GENERATORS: List[ConfigGenerator] = []

# ------------------------
# Runner: generate and save all configs for all environments
# ------------------------
def generate_and_save_all():
    """
    Iterate through all registered generators,
    generate configs, and save them to JSON for each environment.
    """
    for generator in GENERATORS:
        env_configs_map = generator.generate()
        for env, config_def in env_configs_map.items():
            config_def.save(env)
