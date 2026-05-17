from unittest.mock import patch, MagicMock
import json
from src.cotacao import buscar_cotacao_dolar


def test_cotacao_retorna_valor_valido():
    dados_fake = {"USDBRL": {"bid": "5.05"}}
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(dados_fake).encode()
    mock_response.__enter__ = lambda s: s
    mock_response.__exit__ = MagicMock(return_value=False)

    with patch("urllib.request.urlopen", return_value=mock_response):
        resultado = buscar_cotacao_dolar()
        assert resultado == 5.05


def test_cotacao_retorna_none_em_erro():
    with patch("urllib.request.urlopen", side_effect=Exception("Erro")):
        resultado = buscar_cotacao_dolar()
        assert resultado is None