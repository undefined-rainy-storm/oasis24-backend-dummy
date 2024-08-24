from flasgger import Schema, fields

class RequestGetSketchesSchema(Schema):
    id = fields.Str(required=True)
