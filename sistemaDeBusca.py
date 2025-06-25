import json

estoquejson = [
    {
      "nome": "Camiseta",
      "quantidade": 150,
      "tamanho": "M"
    },

    {
    "nome": "Calça",
    "quantidade": 150,
    "tamanho": "G"
    }
]

itens = json.loads(estoquejson)


def buscarItens(termo):
    termo = termo.lower()
    resultados = [item for item in itens if termo in item["ID"].lower() or item["nome"].lower() or item["categoria"].lower() or termo in item["quantidade"].lower() or termo in item["tamanho"].lower() or termo in item["data"].lower()]
    return resultados

termoBusca = input("Digite o termo de busca: ")
resultados = buscarItens(termoBusca)

if resultados:
    for item in resultados:
        print(f'ID: {item["id"]}, Nome: {item["nome"]}, Categoria: {item["categoria"]}, Quantidade: {item["quantidade"]}, Tamanho: {item["tamanho"]}, Data: {item["data"]}')
else:
    print("Nenhum item encontrado.")