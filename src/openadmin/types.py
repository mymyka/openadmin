from typing import Dict, List

from pydantic import BaseModel


class Stat[T](BaseModel):
    value: T


class Table(BaseModel):
    data: List[Dict[str, str | bool | int | float]]
