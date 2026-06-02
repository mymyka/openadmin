from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from openadmin import AdminPanel

from .analytics import page as analytics_admin
from .users import page as users_admin
from .welcome_admin import page as welcome_admin

app = FastAPI()
app.mount(
    "/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
admin_panel = AdminPanel()

admin_panel.include_page(welcome_admin)
admin_panel.include_page(users_admin, tags=["Users"])
admin_panel.include_page(analytics_admin, tags=["Analytics"])


app.mount("/admin", admin_panel)
