print("Cadastro de Fornecedores")

qtde_fornecedores = int(input("Digite a quantidade de fornecedores que deseja cadastrar: "))

for i in range(qtde_fornecedores):
    print(f"\nCadastro do fornecedor {i + 1}:")

    nome_fornecedor = input("Digite o nome do fornecedor:")

    endereco_fornecedor = input("Digite o endereço do fornecedor:")

    telefone_fornecedor = input("Digite o telefone do fornecedor:")

    email_fornecedor = input("Digite o e-mail do fornecedor:")

    print("Cadastro de fornecedor concluído com sucesso!")

    print("\nResumo do cadastro:")
    print(f"Nome: {nome_fornecedor}")
    print(f"Endereço: {endereco_fornecedor}")
    print(f"Telefone: {telefone_fornecedor}")
    print(f"E-mail: {email_fornecedor}")


