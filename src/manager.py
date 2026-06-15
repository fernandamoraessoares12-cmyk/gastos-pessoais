from datetime import date
from src.database import listar_gastos, adicionar_gasto

CATEGORIAS = ["alimentação", "transporte",
              "saúde", "lazer", "outros"]


class GerenciadorGastos:

    def adicionar(self, descricao, valor, categoria):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo.")
        if categoria not in CATEGORIAS:
            raise ValueError(f"Categoria inválida: {categoria}")
        data = str(date.today())
        return adicionar_gasto(descricao, valor, categoria, data)

    def listar(self):
        return listar_gastos()

    def saldo_total(self):
        result = listar_gastos()
        return sum(float(g["valor"]) for g in result)

    def por_categoria(self):
        result = listar_gastos()
        resultado = {}
        for g in result:
            cat = g["categoria"]
            resultado[cat] = resultado.get(cat, 0) + float(g["valor"])
        return resultado
