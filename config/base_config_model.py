import json
from pathlib import Path
from pydantic import BaseModel

class BaseConfigModel(BaseModel):
    ConfigFileName: str = None

    @classmethod
    def load(cls, env: str = None):
        if cls.ConfigFileName is None:
            raise ValueError(f"{cls.__name__} must define ConfigFileName")
        
        # Construct the filename
        filename = cls.ConfigFileName
        if env:
            filename += f"-{env}"
        filename += ".json"  # always append .json internally

        path = Path("config/generated") / filename
        if not path.exists():
            raise FileNotFoundError(f"Config file {path} not found")

        with open(path, "r") as f:
            data = json.load(f)

        return cls(**data)

    def save(self, env: str = None):
        if self.ConfigFileName is None:
            raise ValueError(f"{self.__class__.__name__} must define ConfigFileName")

        filename = self.ConfigFileName
        if env:
            filename += f"-{env}"
        filename += ".json"  # always append .json internally

        path = Path("config/generated") / filename
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w") as f:
            json.dump(self.model_dump(), f, indent=4)
