from fastapi import APIRouter

from .types import Stat, Table


class AdminPage(APIRouter):
    def __init__(self, name: str):
        super().__init__(prefix=f"/{name.lower().replace(' ', '-')}")

    def stat(
        self,
        name: str,
        description: str | None = None,
    ):
        kebab_name = name.lower().replace(" ", "-")
        return self.get(
            f"/stat/{kebab_name}", description=description, response_model=Stat
        )

    def table(
        self,
        name: str,
        description: str | None = None,
    ):
        kebab_name = name.lower().replace(" ", "-")
        return self.get(
            f"/table/{kebab_name}",
            description=description,
            response_model=Table,
        )

    def markdown(self, name: str):
        kebab_name = name.lower().replace(" ", "-")
        return self.get(
            f"/markdown/{kebab_name}",
            response_model=str,
        )

    def action_get(
        self,
        name: str,
        description: str | None = None,
    ):
        kebab_name = name.lower().replace(" ", "-")
        return self.get(
            f"/action/{kebab_name}",
            description=description,
        )

    def action_post(
        self,
        name: str,
        description: str | None = None,
    ):
        kebab_name = name.lower().replace(" ", "-")
        return self.post(
            f"/action/{kebab_name}",
            description=description,
        )

    def action_put(
        self,
        name: str,
        description: str | None = None,
    ):
        kebab_name = name.lower().replace(" ", "-")
        return self.put(
            f"/action/{kebab_name}",
            description=description,
        )

    def action_patch(
        self,
        name: str,
        description: str | None = None,
    ):
        kebab_name = name.lower().replace(" ", "-")
        return self.patch(
            f"/action/{kebab_name}",
            description=description,
        )

    def action_delete(
        self,
        name: str,
        description: str | None = None,
    ):
        kebab_name = name.lower().replace(" ", "-")
        return self.delete(
            f"/action/{kebab_name}",
            description=description,
        )
