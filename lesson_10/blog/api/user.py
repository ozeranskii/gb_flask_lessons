from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.api.permissions.user import UserListPermission, UserPatchPermission
from blog.extensions import db
from blog.models import User
from blog.schemas import UserSchema


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_get': [UserListPermission],
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_patch': [UserPatchPermission],
    }
