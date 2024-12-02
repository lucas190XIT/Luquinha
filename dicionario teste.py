def criar_dicionario():
    # Criando um dicionário vazio
    dicionario = {}

    # Informações iniciais para o usuário
    print("Vamos criar um dicionário! Você pode adicionar pares chave-valor.")

    # Loop para permitir adicionar múltiplos pares chave-valor
    while True:
        chave = input("Digite o nome da chave (ou 'sair' para finalizar): ")
        
        # Condição para finalizar o loop
        if chave.lower() == 'sair':
            break
        
        valor = input(f"Digite o valor para a chave '{chave}': ")
        
        # Adicionando o par chave-valor no dicionário
        dicionario[chave] = valor
        
        # Pergunta ao usuário se deseja adicionar mais itens
        continuar = input("Você deseja adicionar mais um par chave-valor? (s/n): ").lower()
        if continuar != 's':
            break

    # Exibindo o dicionário final
    print("\nDicionário final criado:")
    print(dicionario)


# Chamando a função para criar o dicionário
criar_dicionario()
