from marshmallow_jsonapi import Schema, fields


class TagSchema(Schema):
    class Meta:
        type_ = 'tag'
        self_url = 'tag_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = 'tag_list'

    id = fields.Integer(as_string=True)
    name = fields.String(allow_none=False, required=True)
