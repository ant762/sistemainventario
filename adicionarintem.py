import json
from datetime import datetime

def adicionarItem():
    nome = input("Digite o nome da roupa: ")
    categoria = input("Digite a categoria da roupa: (ex: camiseta, calça, entre outros tipos.): ")

    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    while True:
        data = input("Digite a data de entrada (ex: 03/07/2025): ")
        try:
            datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")

    novoItem = {
        
        "id": id,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "dataEntrada": data
    }

    try:
        with open(estoque , 'r', encoding='utf-8') as estoque:
            inventario = json.load(estoque )
    except FileNotFoundError:
        inventario = []

    inventario.append(novoItem)

    with open(estoque , 'w', encoding='utf-8') as estoque:
        json.dump(inventario, estoque , indent=4)

    print(f"\n Item '{nome}' foi adicionado com sucesso no estoque '{estoque }'!")
