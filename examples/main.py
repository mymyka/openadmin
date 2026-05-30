from fastapi import FastAPI

from openadmin import AdminPanel

from .posts import page as posts_admin
from .users import page as users_admin

app = FastAPI()
admin_panel = AdminPanel()

admin_panel.include_page(posts_admin, tags=["Posts"])
admin_panel.include_page(users_admin, tags=["Users"])

app.mount("/admin", admin_panel)
