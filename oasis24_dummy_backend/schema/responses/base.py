from flasgger import Schema, fields
from dataclasses import dataclass
from marshmallow.validate import Equal, OneOf

from ...entities.transaction.response_enum import ResponseState, OperationFailCode

# Response

@dataclass
class Response:
    state: ResponseState
    details: str

class ResponseSchema(Schema):
    state = fields.Str(
        required=True,
        validate=OneOf([
            ResponseState.success,
            ResponseState.failed
        ])
    )
    details = fields.Str()

# Response on Success

class ResponseOnSuccessSchema(ResponseSchema):
    state = fields.Str(validate=Equal(
        ResponseState.success
    ))

# Resoponse on Failed

@dataclass
class ResponseOnFailed(Response):
    code: OperationFailCode

class ResponseOnFailedSchema(ResponseSchema):
    state = fields.Str(validate=Equal(
        ResponseState.failed
    ))
    code = fields.Str(validate=OneOf([
        OperationFailCode.undefined,
        OperationFailCode.authorization_failed,
    ]))
