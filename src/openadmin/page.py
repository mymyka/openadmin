from fastapi import APIRouter


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
            f"/stat/{kebab_name}",
            description=description,
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
        )
