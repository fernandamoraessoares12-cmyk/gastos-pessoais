import urllib.request
import json


def buscar_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            dados = json.loads(response.read())
            cotacao = float(dados["USDBRL"]["bid"])
            return cotacao
    except Exception:
        return None
    