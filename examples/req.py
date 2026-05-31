from typing import Literal

from pydantic import BaseModel


class CreateUserReq(BaseModel):
    name: str
    email: str
    plan: Literal["free", "premium", "enterprise"] = "free"
    active: bool = True
