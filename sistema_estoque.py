# sistema_estoque.py
# Disciplina: Programação de Computadores - UP
# Empresa simulada: DataCode Solutions
# Objetivo: Simular operacoes basicas de controle de estoque via terminal.
# Estrutura do estoque: dicionario de dicionarios onde cada produto
# contem os atributos quantidade (int) e preco (float).

# Estrutura de dados inicial com 3 produtos pre-cadastrados
estoque = {
    "Arroz": {"quantidade": 50, "preco": 5.99},
    "Feijao": {"quantidade": 30, "preco": 8.49},
    "Macarrao": {"quantidade": 40, "preco": 3.75}
}

# Laco de repeticao principal - mantem o menu ativo ate o usuario sair
while True:

    print("\n===== SISTEMA DE GESTAO DE ESTOQUE =====")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saida de Produto")
    print("4 - Sair do Sistema")
    print("=========================================")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        print("\n---------- ESTOQUE ATUAL ----------")
        for nome, dados in estoque.items():
            print(f"Produto: {nome} | "
                  f"Quantidade: {dados['quantidade']} | "
                  f"Preco: R$ {dados['preco']:.2f}")
        print("-----------------------------------")

    elif opcao == "2":
        nome_produto = input("Digite o nome do produto: ")
        if nome_produto in estoque:
            quantidade_entrada = int(input("Digite a quantidade a adicionar: "))
            if quantidade_entrada > 0:
                estoque[nome_produto]["quantidade"] += quantidade_entrada
                print(f"Entrada registrada! Nova quantidade de {nome_produto}: "
                      f"{estoque[nome_produto]['quantidade']}")
            else:
                print("Quantidade invalida. Digite um valor positivo.")
        else:
            print("Produto nao encontrado.")

    elif opcao == "3":
        nome_produto = input("Digite o nome do produto: ")
        if nome_produto in estoque:
            quantidade_saida = int(input("Digite a quantidade a retirar: "))
            if quantidade_saida > 0:
                if estoque[nome_produto]["quantidade"] >= quantidade_saida:
                    estoque[nome_produto]["quantidade"] -= quantidade_saida
                    print(f"Saida registrada! Quantidade restante de {nome_produto}: "
                          f"{estoque[nome_produto]['quantidade']}")
                else:
                    print("Estoque insuficiente.")
            else:
                print("Quantidade invalida. Digite um valor positivo.")
        else:
            print("Produto nao encontrado.")

    elif opcao == "4":
        print("Encerrando o sistema. Ate logo!")
        break

    else:
        print("Opcao invalida. Por favor, escolha uma opcao entre 1 e 4.")