import json
from pathlib import Path
from pydantic import BaseModel

class BaseConfigModel(BaseModel):
    """
    Base class for your configuration model
    To add a configuration you must inherit this class and add a ConfigFileName
    The .json file extension is not required
    
    You should not call load/ save manually.
    """
    ConfigFileName: str = None

    @classmethod
    def load(cls):
        if cls.ConfigFileName is None:
            raise ValueError(f"{cls.__name__} must define ConfigFileName")
        
        # Automatically add .json if missing
        filename = cls.ConfigFileName
        
        if not filename.endswith(".json"):
            filename += ".json"
            
        path = Path("config/generated") / filename
        
        with open(path) as f:
            data = json.load(f)
            
        return cls(**data)
    
    def save(self):
        if self.ConfigFileName is None:
            raise ValueError(f"{self.__class__.__name__} must define ConfigFileName")
        
        filename = self.ConfigFileName
        if not filename.endswith(".json"):
            filename += ".json"
            
        path = Path("config/generated") / filename
        path.parent.mkdir(parents=True, exist_ok=True)  # ensure folder exists
        
        with open(path, "w") as f:
            json.dump(self.model_dump(), f, indent=4)