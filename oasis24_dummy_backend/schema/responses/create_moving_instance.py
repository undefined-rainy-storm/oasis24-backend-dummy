from flasgger import fields

from .base import ResponseOnSuccessSchema

class ResponseCreateMovingInstanceOnSuccessSchema(ResponseOnSuccessSchema):
    id = fields.Str()
