from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from openadmin import AdminPanel

from .users import page as users_admin
from .welcome_admin import page as welcome_admin

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
admin_panel = AdminPanel()

admin_panel.include_page(welcome_admin)
admin_panel.include_page(users_admin, tags=["Users"])


app.mount("/admin", admin_panel)
