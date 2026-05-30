from typing import Dict, List

from pydantic import BaseModel


class Stat(BaseModel):
    value: str | bool | int | float


class Table(BaseModel):
    data: List[Dict[str, str | bool | int | float]]
