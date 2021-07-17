from combojsonapi.utils import Relationship
from marshmallow_jsonapi import Schema, fields


class ArticleSchema(Schema):
    class Meta:
        type_ = 'article'
        self_url = 'article_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = 'article_list'

    id = fields.Integer(as_string=True)
    title = fields.String(allow_none=False, required=True)
    text = fields.String(allow_none=False, required=True)
    created_at = fields.DateTime(allow_none=False)
    updated_at = fields.DateTime(allow_none=False)

    author = Relationship(
        nested='AuthorSchema',
        attribute='author',
        related_url='author_detail',
        related_url_kwargs={'id': '<id>'},
        schema='AuthorSchema',
        type_='author',
        many=False,
    )

    tags = Relationship(
        nested='TagSchema',
        attribute='tags',
        related_url='tag_detail',
        related_url_kwargs={'id': '<id>'},
        schema='TagSchema',
        type_='tag',
        many=True,
    )
