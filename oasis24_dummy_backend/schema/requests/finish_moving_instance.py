from flasgger import Schema, fields

from ..commons.polyline import PolylineField

class RequestFinishMovingInstanceSchema(Schema):
    id = fields.Str(required=True)
    path = PolylineField(required=True)
