import requests


def get_all_markets_id():
    response = requests.get('https://www.buda.com/api/v2/markets').json()
    markets = response['markets']
    markets_id = [market['id'] for market in markets]
    return markets_id

def get_all_tickers():
    markets_id = get_all_markets_id()
    tickers = []
    for market_id in markets_id:
        ticker = requests.get(f'https://www.buda.com/api/v2/markets/{market_id}/ticker').json()
        tickers.append(ticker)
    return tickers

def get_spread(ticker):
    min_ask = float(ticker['ticker']['min_ask'][0])
    max_bid = float(ticker['ticker']['max_bid'][0])
    return min_ask - max_bid

def get_spreads():
    tickers = get_all_tickers()
    spreads = []
    for ticker in tickers:
        spread = get_spread(ticker)
        spreads.append(spread)
    return spreads

def spreads_to_json(spreads, markets_id):
    spreads_json = []
    for i in range(len(spreads)):
        spread_json = {
            'market_id': markets_id[i],
            'spread': spreads[i]
        }
        spreads_json.append(spread_json)
    return spreads_json

def get_spreads_alert(spreads, spread_alert, markets_id):
    spreads_alert = []
    if spread_alert is None:
        spread_alert_json = {
            'market_id': None,
            'spread': None,
            'alert': 'No se ha establecido un spread de alerta'
        }
        spreads_alert.append(spread_alert_json)
        return spreads_alert
    for i in range(len(spreads)):
        if spreads[i] < spread_alert:
            spread_alert_json = {
                'market_id': markets_id[i],
                'spread': spreads[i],
                'alert': 'Menor al spread de alerta'
            }
        elif spreads[i] > spread_alert:
            spread_alert_json = {
                'market_id': markets_id[i],
                'spread': spreads[i],
                'alert': 'Mayor al spread de alerta'
            }
        else:
            spread_alert_json = {
                'market_id': markets_id[i],
                'spread': spreads[i],
                'alert': 'Igual al spread de alerta'
            }
        spreads_alert.append(spread_alert_json)
    order_spreads_alert(spreads_alert)
    return spreads_alert

def order_spreads_alert(spreads_alert):
    spreads_alert.sort(key=lambda x: x['spread'])
    return spreads_alert