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
        gastos = listar_gastos()
        return sum(float(g["valor"]) for g in gastos)

    def por_categoria(self):
        gastos = listar_gastos()
        resultado = {}
        for g in self.gastos:
            resultado[g.categoria] = (
                resultado.get(g.categoria, 0) + g.valor
            )
        return resultado
    def remover(self, indice: int):
        if indice < 0 or indice >= len(self.gastos):
            raise ValueError("Índice inválido.")
        self.gastos.pop(indice)
