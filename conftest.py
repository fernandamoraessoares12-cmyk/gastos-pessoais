import sys
import os

sys.path.insert(0, os.path.abspath("."))
import pytest
from src.manager import GerenciadorGastos

@pytest.fixture
def gerenciador_com_gastos():
    g = GerenciadorGastos()
    g.adicionar("Almoço", 20.0, "alimentação")
    g.adicionar("Ônibus", 5.0, "transporte")
    g.adicionar("Jantar", 30.0, "alimentação")
    return g