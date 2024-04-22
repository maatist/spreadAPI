from . import utils
from unittest.mock import patch
from app.routes import SetSpread

markets_id = []

def test_get_all_markets_id():
    markets_id = utils.get_all_markets_id()
    assert isinstance(markets_id, list)
    assert all(isinstance(id, str) for id in markets_id)

def test_get_all_tickers():
    tickers = utils.get_all_tickers()
    assert isinstance(tickers, list)
    assert all(isinstance(ticker, dict) for ticker in tickers)

def test_get_spreads_alert_no_alert():
    spreads = [10000.0, 20000.0, 30000.0]
    spreads_alert = utils.get_spreads_alert(spreads, None, markets_id)
    assert isinstance(spreads_alert, list)
    assert all(isinstance(spread_alert, dict) for spread_alert in spreads_alert)
    assert all('market_id' in spread_alert for spread_alert in spreads_alert)
    assert all('spread' in spread_alert for spread_alert in spreads_alert)
    assert all('alert' in spread_alert for spread_alert in spreads_alert)
    assert all(spread_alert['alert'] == 'No se ha establecido un spread de alerta' for spread_alert in spreads_alert)

def test_set_spread():
    args = {'spread': 1000.0}
    with patch('app.routes.parser.parse_args', return_value=args):
        instance = SetSpread()
        result = instance.post()
    assert result == {'mensaje': f'Spread de alerta establecido en {args["spread"]}'}

def test_get_spread():
    ticker = {
        'ticker': {
            'min_ask': ['50000.0'],
            'max_bid': ['40000.0']
        }
    }
    spread = utils.get_spread(ticker)
    assert spread == 10000.0

def test_get_spreads():
    spreads = utils.get_spreads()
    assert isinstance(spreads, list)
    assert all(isinstance(spread, float) for spread in spreads)

def test_spreads_to_json():
    spreads = [10000.0, 20000.0, 30000.0]
    markets_id = ['btc-clp', 'eth-clp', 'xrp-clp']
    spreads_json = utils.spreads_to_json(spreads, markets_id)
    assert isinstance(spreads_json, list)
    assert all(isinstance(spread_json, dict) for spread_json in spreads_json)
    assert all('market_id' in spread_json for spread_json in spreads_json)
    assert all('spread' in spread_json for spread_json in spreads_json)

def test_get_spreads_alert():
    spreads = [10000.0, 20000.0, 30000.0]
    markets_id = ['btc-clp', 'eth-clp', 'xrp-clp']
    spreads_alert = utils.get_spreads_alert(spreads, 15000.0, markets_id)
    assert isinstance(spreads_alert, list)
    assert all(isinstance(spread_alert, dict) for spread_alert in spreads_alert)
    assert all('market_id' in spread_alert for spread_alert in spreads_alert)
    assert all('spread' in spread_alert for spread_alert in spreads_alert)
    assert all('alert' in spread_alert for spread_alert in spreads_alert)

def test_order_spreas_alert():
    spreads_alert = [
        {'market_id': 'btc-clp', 'spread': 20000.0, 'alert': 'Mayor al spread de alerta'},
        {'market_id': 'eth-clp', 'spread': 40000.0, 'alert': 'Mayor al spread de alerta'},
        {'market_id': 'xrp-clp', 'spread': 30000.0, 'alert': 'Mayor al spread de alerta'}
    ]
    ordered_spreads_alert = utils.order_spreads_alert(spreads_alert)
    assert ordered_spreads_alert == [
        {'market_id': 'btc-clp', 'spread': 20000.0, 'alert': 'Mayor al spread de alerta'},
        {'market_id': 'xrp-clp', 'spread': 30000.0, 'alert': 'Mayor al spread de alerta'},
        {'market_id': 'eth-clp', 'spread': 40000.0, 'alert': 'Mayor al spread de alerta'}
    ]

