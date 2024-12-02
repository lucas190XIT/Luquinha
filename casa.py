# Dicionário com os personagens e suas casas
personagens = {
    "Harry Potter": "Grifinória",
    "Hermione Granger": "Grifinória",
    "Ron Weasley": "Grifinória",
    "Albus Dumbledore": "Grifinória",
    "Severus Snape": "Sonserina",
    "Draco Malfoy": "Sonserina",
    "Luna Lovegood": "Corvinal",
    "Cedric Diggory": "Lufa-Lufa",
    "Neville Longbottom": "Grifinória",
    "Ginny Weasley": "Grifinória",
    "Minerva McGonagall": "Grifinória"
}

# Função para retornar a casa do personagem
def obter_casa(personagem):
    casa = personagens.get(personagem)
    if casa:
        return f"{personagem} é da casa {casa}."
    else:
        return "Personagem não encontrado."

# Testando a função
nome_personagem = input("Digite o nome de um personagem de Harry Potter: ")
print(obter_casa(nome_personagem))

