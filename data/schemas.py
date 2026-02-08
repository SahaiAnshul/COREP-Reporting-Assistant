from pydantic import BaseModel

class ScenarioInput(BaseModel):
    cet1: float
    tier1: float
    tier2: float
    rwa: float
