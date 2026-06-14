from src.manager import GerenciadorGastos, CATEGORIAS
def exibir_menu():
    from src.cotacao import buscar_cotacao_dolar
    cotacao = buscar_cotacao_dolar()
    print("\n===== Gerenciador de Gastos Pessoais =====")
    if cotacao:
        print(f"💵 Cotação do dólar: R$ {cotacao:.2f}")
    print("1. Adicionar gasto")
    print("2. Listar gastos")
    print("3. Ver total gasto")
    print("4. Ver gastos por categoria")
    print("0. Sair")
    print("5. Remover gasto")
    

def main():
    gerenciador = GerenciadorGastos()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            descricao = input("Descrição: ").strip()
            try:
                valor = float(input("Valor (R$): ").strip())
            except ValueError:
                print("Valor inválido! Digite um número.")
                continue
            print(f"Categorias: {', '.join(CATEGORIAS)}")
            categoria = input("Categoria: ").strip().lower()
            try:
                gerenciador.adicionar(descricao, valor, categoria)
                print("Gasto adicionado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            gastos = gerenciador.listar()
            if not gastos:
                print("Nenhum gasto registrado.")
            else:
                print("\n--- Seus gastos ---")
                for i, g in enumerate(gastos, 1):
                    print(f"{i}. {g.descricao} | R$ {g.valor:.2f} | {g.categoria} | {g.data}")

        elif opcao == "3":
            print(f"\nTotal gasto: R$ {gerenciador.saldo_total():.2f}")

        elif opcao == "4":
            cats = gerenciador.por_categoria()
            if not cats:
                print("Nenhum gasto registrado.")
            else:
                print("\n--- Por categoria ---")
                for cat, total in cats.items():
                    print(f"{cat}: R$ {total:.2f}")
                    
                    elif opcao == "5":
    elif opcao == "5":
    listar_gastos(gerenciador)
    indice = int(input("Digite o número do gasto que deseja remover: "))
    gerenciador.remover(indice)
    print("Gasto removido com sucesso!")

        elif opcao == "0":
            print("Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()