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
    resultados = [item for item in itens if termo in item["nome"].lower() or termo in item["quantidade"].lower() or termo in item["tamanho"].lower()]
    return resultados

termoBusca = input("Digite o termo de busca: ")
resultados = buscarItens(termoBusca)
