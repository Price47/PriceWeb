import requests

def eth_token_to_usd(token, key):
    response = requests.get("https://api.hitbtc.com/api/2/public/ticker/ETHUSD")
    base_usd = float(response.json()[key])
    token_eth = float(token[key])

    return token_eth*base_usd


def ticker_difference(current, yesterday):
    delta = float(current) - float(yesterday)
    if delta>0:
        status = "Up"
    else:
        status = "Down"

    return status, abs(delta)

def get_coin_info_eth(coin_json):
    price = eth_token_to_usd(coin_json, 'last')
    prev = eth_token_to_usd(coin_json, 'open')
    high = eth_token_to_usd(coin_json, 'high')
    low = eth_token_to_usd(coin_json, 'low')

    return price, prev, high, low


def get_coin_info(coin_json):
    price = coin_json['last']
    prev = coin_json['open']
    high = coin_json['high']
    low = coin_json['low']

    return price, prev, high, low