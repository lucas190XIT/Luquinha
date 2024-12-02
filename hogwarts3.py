estudantes = [
    {"nome": "hermione", "casa": "grifinoria", "patrono": "lontra",},
    {"nome": "harry", "casa": "grifinoria", "patrono": "veado"},
    {"nome": "Rony", "casa": "grifinoria", "patrono": "jack"},
    {"nome": "draco", "casa": "soserina", "patrono": None},
    ]
    
for estudante in estudantes:
    print(estudante["nome"],estudante["casa"],estudante["patrono"], sep=", ")