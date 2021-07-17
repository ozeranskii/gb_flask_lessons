from flask_admin import Admin
from flask_combo_jsonapi import Api
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from blog.admin.views import CustomAdminIndexView

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
admin = Admin(
    index_view=CustomAdminIndexView(),
    name='Blog Admin Panel',
    template_mode='bootstrap4',
)
api = Api()
