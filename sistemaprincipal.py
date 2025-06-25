import json

estoqueLimite = 500

arquivoEstoque = "estoque.json"


def carregarProdutos():
    try:
        with open(arquivoEstoque, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return ["Não há estoque."]


def removerProduto(id):
    produtos = carregarProdutos()

    novos_produtos = [p for p in produtos if p["ID"] != id]

    if len(produtos) == len(novos_produtos):
        print(f"Nenhum produto com ID {id} foi encontrado.")
        return False

    salvarProdutos(novos_produtos)
    print(f"Produto com ID {id} removido com sucesso.")
    return True


def salvarProdutos(produtos):
    with open(arquivoEstoque, "w") as f:
        json.dump(produtos, f, indent=4)


def totalEstoque(produtos):
    return sum(produto["quantidade"] for produto in produtos)


def adicionarProduto(id, nome, data, categoria, quantidade, dataEntrada):
    produtos = carregarProdutos()
    
    if totalEstoque(produtos) + quantidade > estoqueLimite:
        print("Erro: estoque limite ultrapassado, não é possível adicionar mais produtos.")
        return False

    # Verificação de id
    for p in produtos:
        if p["id"] == id:
            print("Erro: ID já existe.")
            return False
    
    novo_produto = {
        "ID": id,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "data": data,
    }

    produtos.append(novo_produto)
    salvarProdutos(produtos)
    print(f"Produto '{nome}' adicionado com sucesso!")
    return True

def listarProdutos():
    produtos = carregarProdutos()
    for p in produtos:
        print(f"{p['id']}: {p['nome']} - Categoria: {p['categoria']} - {p['quantidade']} unidades - data de entrada: {p['data']}")


while True:
    print("\nSISTEMA DE INVENTÁRIO")
    print("1 - Adicionar Produto")
    print("2 - Listar Produtos")
    print("3 - Remover Produto")
    print("4 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if opcao == 1:
        id = input("ID: ")
        nome = input("Nome: ")
        data = input("Data de entrada: ")
        categoria = input("Categoria: ")
        try:
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Quantidade inválida.")
            continue
        adicionarProduto(id, nome, data, categoria, quantidade, data)

    elif opcao == 2:
        listarProdutos()

    elif opcao == 3:
        idRemover = input("Digite o ID do produto a remover: ")
        removerProduto(idRemover)

    elif opcao == 0:
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida.")
