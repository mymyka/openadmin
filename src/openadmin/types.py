from typing import Dict, List, Literal

from pydantic import BaseModel


class Stat(BaseModel):
    value: str | bool | int | float


class Table(BaseModel):
    data: List[Dict[str | Literal["__actions__"], str | bool | int | float | Action]]


class Action(BaseModel):
    color: str | Literal["danger", "warning", "info"]
    method: Literal["POST", "GET", "PUT", "PATCH"]
    url: str
    body: dict
