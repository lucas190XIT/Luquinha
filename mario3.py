def print_coluna(tamanho):
    """Imprime a palavra 'Mario' em uma coluna, repetindo-a 'tamanho' vezes."""
    for _ in range(tamanho):
        print("Mario")

def print_linha(tamanho):
    """Imprime a palavra 'Mario' em uma linha, repetindo-a 'tamanho' vezes."""
    for _ in range(tamanho):
        print("Mario", end=" ")
    print()  # Nova linha após a impressão da linha

def print_bloco(linhas, colunas):
    """Imprime um bloco de 'Mario', com base no número de linhas e colunas especificados."""
    for i in range(linhas):
        for j in range(colunas):
            print("Mario", end=" ")
        print()  # Nova linha após imprimir todas as colunas em uma linha

# Função principal para rodar o código
if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1. Imprimir uma coluna de Mario")
    print("2. Imprimir uma linha de Mario")
    print("3. Imprimir um bloco de Mario")
    
    escolha = int(input("Digite o número da opção: "))

    if escolha == 1:
        tamanho = int(input("Digite o número de vezes para a coluna: "))
        print_coluna(tamanho)
    elif escolha == 2:
        tamanho = int(input("Digite o número de vezes para a linha: "))
        print_linha(tamanho)
    elif escolha == 3:
        linhas = int(input("Digite o número de linhas do bloco: "))
        colunas = int(input("Digite o número de colunas do bloco: "))
        print_bloco(linhas, colunas)
    else:
        print("Opção inválida. Tente novamente.")
