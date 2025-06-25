import json

def removerItem():
    try:
        with open( estoque, 'r', encoding='utf-8') as abrir:
            lista = json.load(abrir)
    except FileNotFoundError:
        print(" Arquivo não foi encontrado.")
        return

    print("\n Itens no inventário:")
    for numero, roupa in enumerate(lista, start=1):
        print(f"{numero}. {roupa['nome']} - {roupa['categoria']} - {roupa['quantidade']} unidades")

    nomeRemover = input("\nDigite o nome da roupa que deseja remover: ")

    novaLista = [roupa for roupa in lista if roupa['nome'].lower() != nomeRemover.lower()]

    if len(novaLista) == len(lista):
        print("Item não encontrado.")
    else:
        with open(estoque, 'w', encoding='utf-8') as salvar:
            json.dump(novaLista, salvar, indent=4)
        print(f"Item '{nomeRemover}' removido com sucesso!")
