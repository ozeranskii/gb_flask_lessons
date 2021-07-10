from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.extensions import db
from blog.models import Author
from blog.schemas import AuthorSchema


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }
