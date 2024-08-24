from json import dumps, loads
from marshmallow import fields, ValidationError

from ...entities.commons.polyline import Polyline
from ...entities.commons.vector2 import Vector2

class PolylineField(fields.Field):
    '''
    Field that contains polyline requirements
    '''

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ''
        if type(value) != type(Polyline()):
            raise ValidationError(f'`value`({value[:10]}) is not Polyline type.')
        for each in value.path:
            if len(each) != 2 and type(each) != type(Vector2()):
                raise ValidationError(f'path data of `value` is neither Vector2D nor containing content length of 2.')
        return repr(value)

    def _deserialize(self, value, attr, data, **kwargs):
        loaded = None
        try:
            loaded = loads(value)
        except ValueError:
            raise ValidationError('`value` cannot be deserialize.')
        if 'path' not in loaded:
            raise ValidationError('parameter `path` required but not found.')
        for each in loaded['path']:
            if len(each) != 2:
                raise ValidationError('Each content of `value.path`\'s length must be 2.')
        return Polyline(loaded['path'])
