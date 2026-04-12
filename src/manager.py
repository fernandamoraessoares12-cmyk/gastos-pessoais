from dataclasses import dataclass, field
from datetime import date

CATEGORIAS = ["alimentação", "transporte",
              "saúde", "lazer", "outros"]

@dataclass
class Gasto:
    descricao: str
    valor: float
    categoria: str
    data: str = field(
        default_factory=lambda: str(date.today())
    )

class GerenciadorGastos:
    def __init__(self):
        self.gastos: list[Gasto] = []

    def adicionar(self, descricao, valor, categoria):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo.")
        if categoria not in CATEGORIAS:
            raise ValueError(f"Categoria inválida: {categoria}")
        self.gastos.append(Gasto(descricao, valor, categoria))

    def listar(self):
        return list(self.gastos)

    def saldo_total(self):
        return sum(g.valor for g in self.gastos)

    def por_categoria(self):
        resultado = {}
        for g in self.gastos:
            resultado[g.categoria] = (
                resultado.get(g.categoria, 0) + g.valor
            )
        return resultado