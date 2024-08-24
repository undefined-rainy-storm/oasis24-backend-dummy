from flasgger import Schema, fields

class RequestCreateMovingInstanceSchema(Schema):
    base_point_lat = fields.Float(required=True)
    base_point_lng = fields.Float(required=True)
