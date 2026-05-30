from openadmin import AdminPanel

from .posts import page as posts_admin
from .users import page as users_admin

panel = AdminPanel()

panel.include_page(posts_admin, tags=["Posts"])
panel.include_page(users_admin, tags=["Users"])
