from enum import Enum

from fastapi import FastAPI

from .page import AdminPage


class AdminPanel(FastAPI):
    def include_page(
        self,
        page: AdminPage,
        tags: list[str | Enum] | None = None,
    ):
        return self.include_router(router=page, tags=tags)
