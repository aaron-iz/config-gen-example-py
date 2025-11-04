# Configuration System Documentation

This document explains the configuration pattern used in this project. The system provides a **centralized, type-safe, environment-aware configuration framework** for your service.  

With this pattern, you can:

- Define a configuration class once.
- Access it globally from anywhere in your code without worrying about which environment or region you are in.
- Depend on other configs safely.
- Generate JSON configuration files for multiple environments automatically.

---

## 1. Creating a Configuration Model

1. All configuration models must **inherit from `BaseConfigModel`**.  
2. Each model must define a **`ConfigFileName`** (without `.json`).  
3. Add all necessary fields using Pydantic types.

Example:

```python
# models/app_config.py
from config.base_config_model import BaseConfigModel

class AppConfig(BaseConfigModel):
    ConfigFileName = "app_config"

    Title: str
    AuthExtension: str
```

- The `ConfigFileName` will be used to load/save JSON files: `app_config.json` by default, or `app_config-<env>.json` for environment-specific configs.  
- Environment-specific files are handled automatically when using the container or generators.

---

## 2. Registering Your Config in the Container

All configuration models must be **registered in `config_container.py`** to expose a global object that can be used anywhere in your code:

```python
config.AppConfig = AppConfig.load(config.env)
```

- The container automatically loads **environment-specific configs** if `SERVICE_ENV_NAME` is set.  
- You can access configs globally:

```python
from config.config_container import config

print(config.AppConfig.Title)
```

---

## 3. Creating a Generator

Generators allow you to **programmatically create and save JSON configs** for one or more environments.

1. Inherit from `ConfigGenerator`.  
2. Implement the `generate()` method.  
3. Return a dictionary mapping **environment → BaseConfigModel instance**.  

Example for `AppConfig`:

```python
# generators/app_config_gen.py
from config.config_generation import ConfigGenerator
from config.models.app_config import AppConfig
from config.environment_keys import LOCAL_ENV, STAGE_ENV, PROD_ENV, IL_PROD_ENV
from typing import Dict

class AppConfigGenerator(ConfigGenerator):
    def generate(self) -> Dict[str, AppConfig]:
        default_config = AppConfig(
            Title="Infra-AuthenticationService",
            AuthExtension="/api/auth"
        )
        return {
            LOCAL_ENV: default_config,
            STAGE_ENV: default_config,
            PROD_ENV: default_config,
            IL_PROD_ENV: default_config,
        }
```

---

## 4. Registering Generators

All generators must be **registered in the `GENERATORS` list** in `run_generate_configs.py`:

```python
# Register your configurations here:
GENERATORS.append(AppConfigGenerator())
```

- Only registered generators will be used when generating JSON files.

---

## 5. Running the Generation

To generate JSON configuration files for all environments:

```bash
poetry run python config.run_generate_configs.py
```

- This will create the corresponding files in `config/generated/`  
- Files will be named automatically based on `ConfigFileName` and environment:  
  - `app_config.json` → default  
  - `app_config-stage.json` → stage  
  - `app_config-prod.json` → prod  
  - `app_config-il-prod.json` → il-prod

This setup ensures that your configuration system is:

- Centralized and easy to use  
- Environment-aware  
- Type-safe  
- Automatically persisted to JSON files via generators  
- Ready for multi-environment deployments
