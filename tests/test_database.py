from unittest.mock import patch, MagicMock
import pytest


@pytest.fixture
def mock_supabase():
    with patch("src.database.get_client") as mock:
        cliente = MagicMock()
        mock.return_value = cliente
        yield cliente


def test_listar_gastos(mock_supabase):
    mock_supabase.table.return_value.select.return_value\
        .order.return_value.execute.return_value.data = [
        {"id": "1", "descricao": "Mercado", "valor": 150.0,
         "categoria": "alimentação", "data": "2025-06-01"}
    ]
    from src.database import listar_gastos
    resultado = listar_gastos()
    assert len(resultado) == 1
    assert resultado[0]["descricao"] == "Mercado"


def test_adicionar_gasto(mock_supabase):
    mock_supabase.table.return_value.insert.return_value\
        .execute.return_value.data = [
        {"id": "2", "descricao": "Uber", "valor": 25.0,
         "categoria": "transporte", "data": "2025-06-01"}
    ]
    from src.database import adicionar_gasto
    resultado = adicionar_gasto("Uber", 25.0, "transporte", "2025-06-01")
    assert resultado["descricao"] == "Uber"
    assert resultado["valor"] == 25.0


def test_deletar_gasto_sucesso(mock_supabase):
    mock_supabase.table.return_value.delete.return_value\
        .eq.return_value.execute.return_value.data = [{"id": "1"}]
    from src.database import deletar_gasto
    assert deletar_gasto("1") is True


def test_deletar_gasto_nao_encontrado(mock_supabase):
    mock_supabase.table.return_value.delete.return_value\
        .eq.return_value.execute.return_value.data = []
    from src.database import deletar_gasto
    assert deletar_gasto("999") is False
