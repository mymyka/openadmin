from typing import Any, Dict, List, Literal

from fastapi import Query
from pydantic import BaseModel, Field, model_validator


class Stat(BaseModel):
    value: str | bool | int | float


class Action(BaseModel):
    color: str | Literal["danger", "warning", "info"]
    method: Literal["POST", "GET", "PUT", "PATCH", "DELETE"]
    url: str
    body: dict | None = Field(None)


class TableRow(BaseModel):
    model_config = {"extra": "allow", "populate_by_name": True}

    actions: List[Action] = Field(
        default=[],
        alias="__actions__",
        serialization_alias="__actions__",
    )


class Table(BaseModel):
    data: List[TableRow | Dict[str, Any]] = Field(default=[])

    @model_validator(mode="after")
    def coerce_rows(self) -> Table:
        """Coerce raw dicts into TableRow at runtime."""
        self.data = [
            TableRow.model_validate(row) if isinstance(row, dict) else row
            for row in self.data
        ]
        return self


class PaginationParams(BaseModel):
    page: int = Query(ge=0, description="Page number")
    per_page: int = Query(ge=1, description="Number of items per page")
