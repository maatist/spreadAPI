from flask_restx import Namespace, Resource, reqparse
from .utils import get_spreads, spreads_to_json, get_spreads_alert, get_all_markets_id

api = Namespace('spread REST API', description='API para consultar el spread de los mercados de criptomonedas utilizando la api de Buda.com')

parser = reqparse.RequestParser()
parser.add_argument('spread', type=int, help='Ingrese spread limite para informar si es mayor o menor al spread actual')

spread_alert = None
markets_id = None

@api.route('')
class Spread(Resource):
    @api.doc('get_spreads')
    def get(self):
        """
        Obtiene un json con el spread de todos los mercados.
        """
        return {'spreads': spreads_to_json(get_spreads(), get_all_markets_id())}


@api.route('/setSpread')
class SetSpread(Resource):
    @api.expect(parser)
    @api.doc('set_spread_alert')
    def post(self):
        """
        Establece un spread de alerta de tipo numerico para informar si el spread actual de los mercados es mayor o menor al spread establecido.
        """
        global spread_alert
        args = parser.parse_args()
        spread_alert = args['spread']
        return {'mensaje': f'Spread de alerta establecido en {spread_alert}'}

@api.route('/getVerifiedSpread')
class SpreadPolling(Resource):
    @api.doc('get_spread_alert')
    def get(self):
        """
        Obtiene un json con los spreads que son mayores, menores o iguales al spread de alerta.
        """
        if spread_alert is not None:
            return {'spreads_alert': get_spreads_alert(get_spreads(), spread_alert, get_all_markets_id())}
        else:
            return {'mensaje': 'No se ha establecido un spread de alerta'}


