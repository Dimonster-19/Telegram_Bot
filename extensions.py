import requests
import json
from Config import money

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base:str, quote:str, amount:str):
        if base == quote:
            raise APIException(f"Не получится перевести {base} в {base}")

        try:
            base_ticker = money[base]
        except KeyError:
            raise APIException (f"Не удалось обработать валюту: {base}")

        try:
            quote_ticker = money[quote]
        except KeyError:
            raise APIException (f"Не удалось обработать валюту: {quote}")

        try:
            amount = float(amount)
        except KeyError:
            raise APIException(f"Не удалось обработать количество {amount}")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        conversion_rate = json.loads(r.content)[money[quote]]
        result = conversion_rate*amount
        return result
