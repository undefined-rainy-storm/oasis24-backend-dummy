from flasgger import SwaggerView

from .. import api_bp
from ....schema.responses.base import ResponseOnFailedSchema
from ....schema.requests.get_sketches import RequestGetSketchesSchema
from ....schema.responses.get_sketches import ResponseGetSketchesOnSuccessSchema

class GetSketchesApiView(SwaggerView):
    parameters = RequestGetSketchesSchema
    responses = {
        200: {
            'description': 'Response on Success',
            'schema': ResponseGetSketchesOnSuccessSchema
        },
        400: {
            'description': 'Response on Failed',
            'schema': ResponseOnFailedSchema
        }
    }
    validation = True

    def post(self):
        '''
        Get available moving path that sketches image.
        '''
    
api_bp.add_url_rule(
    '/moving_instance/get_sketch',
    view_func=GetSketchesApiView.as_view('api/moving_instance/get_sketches'),
    methods=['POST']
)
