import json
from datetime import datetime

def adicionarItem():
    nome = input("Digite o nome da roupa: ").strip()
    categoria = input("Digite a categoria da roupa (ex: camiseta, calça): ").strip()

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
        data = input("Digite a data de entrada (ex: 03/07/2025): ").strip()
        try:
            datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")

    try:
        with open("estoque.json", 'r', encoding='utf-8') as estoque:
            inventario = json.load(estoque)
            inventario = [item for item in inventario if "id" in item]
    except FileNotFoundError:
        inventario = []

    if inventario:
        ultimo_id = max([int(item["id"]) for item in inventario])
    else:
        ultimo_id = 0
    novo_id = ultimo_id + 1

    novoItem = {
        "id": novo_id,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "dataEntrada": data
    }

    inventario.append(novoItem)

    with open("estoque.json", 'w', encoding='utf-8') as estoque:
        json.dump(inventario, estoque, indent=4, ensure_ascii=False)

    print(f"\n Item '{nome}' foi adicionado com sucesso ao estoque!")

adicionarItem()
