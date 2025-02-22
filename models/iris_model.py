from pydantic import BaseModel
import numpy as np

class IrisTemplate(BaseModel):
    user_id: str
    features: list

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_array(cls, user_id: str, features: np.ndarray):
        return cls(user_id=user_id, features=features.tolist())

    def to_array(self) -> np.ndarray:
        return np.array(self.features)

