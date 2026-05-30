from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from openadmin import AdminPanel

from .posts import page as posts_admin
from .users import page as users_admin
from .users_tasks import page as user_tasks_admin
from .welcome_admin import page as welcome_admin

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
admin_panel = AdminPanel()

admin_panel.include_page(posts_admin, tags=["Posts"])
admin_panel.include_page(users_admin, tags=["Users"])
admin_panel.include_page(user_tasks_admin, tags=["Users"])
admin_panel.include_page(welcome_admin)

app.mount("/admin", admin_panel)
