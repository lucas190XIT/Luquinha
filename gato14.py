def main():
    n = pegar_numeros()
    miar(n)



    def miar(n):
        for _ in range(n):
            print("miau")

def pegar_numeros():
    while True:
        n = int(input("quantas vezes o gatos deve miar ? "))
        if n > 0:
            return n
        
main()

