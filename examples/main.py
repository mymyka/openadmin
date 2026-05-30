from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from openadmin import AdminPanel

from .analytics import page as analytics_admin
from .api_keys import page as api_keys_admin
from .emails import page as emails_admin
from .logs import page as logs_admin
from .media import page as media_admin
from .notifications import page as notifications_admin
from .orders import page as orders_admin
from .permissions import page as permissions_admin
from .posts import page as posts_admin
from .revenue import page as revenue_admin
from .servers import page as servers_admin
from .support import page as support_admin
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

admin_panel.include_page(welcome_admin)
admin_panel.include_page(analytics_admin, tags=["Analytics"])
admin_panel.include_page(revenue_admin, tags=["Finance"])
admin_panel.include_page(orders_admin, tags=["Finance"])
admin_panel.include_page(users_admin, tags=["Users"])
admin_panel.include_page(user_tasks_admin, tags=["Users"])
admin_panel.include_page(permissions_admin, tags=["Users"])
admin_panel.include_page(posts_admin, tags=["Content"])
admin_panel.include_page(media_admin, tags=["Content"])
admin_panel.include_page(emails_admin, tags=["Messaging"])
admin_panel.include_page(notifications_admin, tags=["Messaging"])
admin_panel.include_page(support_admin, tags=["Support"])
admin_panel.include_page(servers_admin, tags=["Infrastructure"])
admin_panel.include_page(logs_admin, tags=["Infrastructure"])
admin_panel.include_page(api_keys_admin, tags=["Infrastructure"])

app.mount("/admin", admin_panel)
