from flasgger import SwaggerView

from .. import api_bp
from ....schema.responses.base import ResponseOnFailedSchema
from ....schema.requests.finish_moving_instance import RequestFinishMovingInstanceSchema
from ....schema.responses.finish_moving_instance import ResponseFinishMovingInstanceOnSuccessSchema

class FinishMovingInstanceApiView(SwaggerView):
    parameters = RequestFinishMovingInstanceSchema
    responses = {
        200: {
            'description': 'Response on Success',
            'schema': ResponseFinishMovingInstanceOnSuccessSchema
        },
        400: {
            'description': 'Response on Failed',
            'schema': ResponseOnFailedSchema
        }
    }
    validation = True

    def post(self):
        '''
        Finish moving instance.
        '''

api_bp.add_url_rule(
    '/moving_instance/finish',
    view_func=FinishMovingInstanceApiView.as_view('api/moving_instance/finish'),
    methods=['POST']
)
