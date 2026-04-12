import pytest
from src.manager import GerenciadorGastos

def test_adicionar_gasto_valido():
    g = GerenciadorGastos()
    g.adicionar("Almoço", 25.0, "alimentação")
    assert len(g.listar()) == 1
    assert g.saldo_total() == 25.0

def test_valor_negativo_raise_error():
    g = GerenciadorGastos()
    with pytest.raises(ValueError):
        g.adicionar("Taxi", -10.0, "transporte")

def test_categoria_invalida_raise_error():
    g = GerenciadorGastos()
    with pytest.raises(ValueError):
        g.adicionar("Algo", 5.0, "categoria_inventada")

def test_por_categoria():
    g = GerenciadorGastos()
    g.adicionar("Almoço", 20.0, "alimentação")
    g.adicionar("Ônibus", 5.0, "transporte")
    g.adicionar("Jantar", 30.0, "alimentação")
    cats = g.por_categoria()
    assert cats["alimentação"] == 50.0
    assert cats["transporte"] == 5.0