import json

estoquejson = [
    {
      "id": "496739",
      "nome": " camisa",
      "categoria": "M",
      "quantidade": "M",
      "dataEntrada": "18/06/2025"
    },

    {
    "nome": "Calça",
    "quantidade": 150,
    "tamanho": "G"
    }
]

def buscarItens(termo):
    termo = termo.lower()
    resultados = []

    for item in estoquejson:

        for chave in item:
            valor = str(item[chave]).lower()
            if termo in valor:
                resultados.append(item)
                break  

    return resultados


termoBusca = input("Digite o termo de busca: ")
resultados = buscarItens(termoBusca)


if resultados:
    for item in resultados:
        print("\nItem encontrado:")
        for chave, valor in item.items():
            print(f"{chave.capitalize()}: {valor}")
else:
    print("Nenhum item encontrado.")