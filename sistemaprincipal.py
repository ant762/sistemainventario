import json
from datetime import datetime

estoqueLimite = 500
arquivoEstoque = "estoque.json"

def carregarProdutos():
    try:
        with open(arquivoEstoque, "r", encoding="utf-8") as f:
            produtos = json.load(f)
            # Garante que produtos seja uma lista
            if isinstance(produtos, list):
                return produtos
            else:
                return []
    except FileNotFoundError:
        return []

def salvarProdutos(produtos):
    with open(arquivoEstoque, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

def totalEstoque(produtos):
    return sum(produto.get("quantidade", 0) for produto in produtos)

def adicionarProduto(id, nome, dataEntrada, categoria, quantidade):
    produtos = carregarProdutos()

    for p in produtos:
        if str(p["id"]) == str(id):
            print("Erro: ID já existe.")
            return False

    if totalEstoque(produtos) + quantidade > estoqueLimite:
        print("Erro: estoque limite ultrapassado. Não é possível adicionar mais produtos.")
        return False

    try:
        datetime.strptime(dataEntrada, "%d/%m/%Y")
    except ValueError:
        print("Data inválida. Use o formato dd/mm/aaaa.")
        return False

    novo_produto = {
        "id": str(id),
        "nome": nome.strip(),
        "categoria": categoria.strip(),
        "quantidade": quantidade,
        "dataEntrada": dataEntrada
    }

    produtos.append(novo_produto)
    salvarProdutos(produtos)
    print(f"✅ Produto '{nome}' adicionado com sucesso!")
    return True

def removerProduto(id):
    produtos = carregarProdutos()
    novos_produtos = [p for p in produtos if str(p["id"]) != str(id)]

    if len(produtos) == len(novos_produtos):
        print(f"Nenhum produto com ID '{id}' foi encontrado.")
        return False

    salvarProdutos(novos_produtos)
    print(f"✅ Produto com ID '{id}' removido com sucesso.")
    return True

def listarProdutos():
    produtos = carregarProdutos()
    if not produtos:
        print("Estoque vazio.")
        return

    print("\n📦 Produtos no Estoque:")
    for p in produtos:
        print(f"🆔 {p['id']} | {p['nome']} | Categoria: {p['categoria']} | Quantidade: {p['quantidade']} | Entrada: {p['dataEntrada']}")

# Interface
while True:
    print("\n=== SISTEMA DE INVENTÁRIO ===")
    print("1 - Adicionar Produto")
    print("2 - Listar Produtos")
    print("3 - Remover Produto")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if opcao == 1:
        id = input("ID: ")
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        dataEntrada = input("Data de entrada (dd/mm/aaaa): ")

        try:
            quantidade = int(input("Quantidade: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa.")
                continue
        except ValueError:
            print("Quantidade inválida.")
            continue

        adicionarProduto(id, nome, dataEntrada, categoria, quantidade)

    elif opcao == 2:
        listarProdutos()

    elif opcao == 3:
        id_remover = input("Digite o ID do produto a remover: ")
        removerProduto(id_remover)

    elif opcao == 0:
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida.")
