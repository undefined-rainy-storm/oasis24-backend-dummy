from flasgger import fields

from .base import ResponseOnSuccessSchema
from ..commons.polyline import PolylineField

class ResponseGetSketchesOnSuccessSchema(ResponseOnSuccessSchema):
    sketches = fields.List(
        PolylineField(required=True),
        required=True
    )
