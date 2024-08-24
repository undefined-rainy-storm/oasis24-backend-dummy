from flasgger import SwaggerView

from .. import api_bp
from ....schema.responses.base import ResponseOnFailedSchema
from ....schema.requests.create_moving_instance import RequestCreateMovingInstanceSchema
from ....schema.responses.create_moving_instance import ResponseCreateMovingInstanceOnSuccessSchema

class CreateMovingInstanceApiView(SwaggerView):
    parameters = RequestCreateMovingInstanceSchema
    responses = {
        200: {
            'description': 'Response on Success',
            'schema': ResponseCreateMovingInstanceOnSuccessSchema
        },
        400: {
            'description': 'Response on Failed',
            'schema': ResponseOnFailedSchema
        }
    }
    validation = True

    def post(self):
        '''
        Create new moving event instance.
        Requires base lat-lng-expressed(WGS84 DMS) coordinate information to create some sketches.
        '''

api_bp.add_url_rule(
    '/moving_instance/create',
    view_func=CreateMovingInstanceApiView.as_view('api/moving_instance/create'),
    methods=['POST']
)
