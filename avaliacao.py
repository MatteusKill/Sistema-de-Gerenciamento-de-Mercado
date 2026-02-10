import time

cores = {

    "limpa":"\033[m",

    "amarela":"\033[33m",

    "vermelho":"\033[31m",

    "verde":"\033[32m"
}

produtos = []
clientes = []
carrinho = []

menuCadastroProdutos = [1,2,3,4,5,6,0]
menuClientes = [1,2,3,0]
menuVenda = [1,2,3,4,0]

# print("""

# ======= SISTEMA DE GERENCIAMENTO THIAGO ALMEIDA  ======

# 1 - Cadastrar produto

# 2 - Listar produtos cadastrados

# 3 - Atualizar o nome de um produto (pelo código informado)

# 4 - Atualizar o estoque de um produto

# 5 - Atualizar o código de um produto

# 6 - Atualizar o preço de um produto

# 0 - Encerrar

# """)

while True:
    print(f"""

{cores['amarela']}=== SISTEMA SUPERMERCADO THIAGO ALMEIDA ==={cores['limpa']}

1 - Cadastro e manutenção de produtos
2 - Cadastro de clientes
3 - Passar carrinho de compras
0 - Encerrar sistema
""")
    try:
        opcaoGeral = int(input("Informe a ação a ser realizada(0-3): "))
    except ValueError:
        print(f"{cores['vermelho']}Erro! Somente números inteiros.{cores['limpa']}")
        continue

    if opcaoGeral == 1:

        print("\nEntrando em Cadastro e Manutenção de Produtos...")

        time.sleep(3)

        print("Ação realizada com sucesso!\n")

        print("""====== MENU MANUTENÇÃO DE PRODUTOS ======

1 - Cadastrar produto
2 - Listar produtos cadastrados
3 - Atualizar o nome de um produto (pelo código informado)
4 - Atualizar o estoque de um produto
5 - Atualizar o código de um produto
6 - Atualizar o preço de um produto
0 - Sair da ferramenta 'Manutenção de Produtos'

""")
        while True:
            try:
                opcaoCadastroProdutos = int (input("Informe a ação a ser realizada(0-6): "))
            except ValueError:
                print(f"{cores['vermelho']}Erro! Somente números inteiros.{cores['limpa']}")
                continue
                

            if opcaoCadastroProdutos in menuCadastroProdutos:
                print("\nEntrando em Cadastrar Produtos...")
                time.sleep(3)
                print("Ação realizada com sucesso!\n")
                
                while True:
                    try:
                        codProduto = int(input("Informe um código para o produto que deseja cadastrar: "))
                    except ValueError:
                        print(f"{cores['vermelho']}Erro! Somente números inteiros.{cores['limpa']}")
                        continue
                    
                    verificaCodigoProduto = False
                    for produtoCadastrado in produtos:
                        if produtoCadastrado["Codigo"] == codProduto:
                            verificaCodigoProduto = True
                            break
                        
                    if verificaCodigoProduto == True:
                        print(f"{cores['vermelho']}Erro! O código inserido já existe.{cores['limpa']}")
                        continue
                    else:
                        break
                    
                while True:
                    nomeProduto = str(input("Informe o nome do produto que deseja cadastrar: "))
                    
                    verificaNomeProduto = False
                    for produtosCadastrados in produtos:
                        if produtosCadastrados["Nome"].lower() == nomeProduto.lower():
                            verificaNomeProduto = True
                            break
                        
                    if verificaNomeProduto == True:
                        print(f"{cores['vermelho']}Erro! O nome inserido já existe.")
                        continue
                    else:
                        break
                while True:
                    try:
                        precoProduto = float(input("Informe um preço para o produto:"))
                        
                        if precoProduto <=0:
                            print(f"{cores['vermelho']}Erro! O preço não pode ser negativo.{cores['limpa']}")
                            continue
                        else:
                            break
                    except ValueError:
                        print(f"{cores['vermelho']}Erro! Somente números.{cores['limpa']}")
                        continue
                    
                while True:
                        try:
                            qntdEstoque = int(input("Informe a unidade disponível deste produto:"))
                            
                            if qntdEstoque < 0:
                                print(f"{cores['vermelho']}Erro! O estoque não pode ser negativo.{cores['limpa']}")
                                continue
                            else:
                                break
                        
                        except ValueError:
                            print(f"{cores['vermelho']}Erro! Somente números inteiros.{cores['limpa']}")
                            continue
                        
                novoProduto = {
                    "Codigo": codProduto,
                    "Nome": nomeProduto,
                    "Preco": precoProduto,
                    "Estoque": qntdEstoque
                }
                produtos.append(novoProduto)
                print(f"{cores['verde']}Produto cadastrado com sucesso!{cores['limpa']}")
                continue
        
            elif opcaoCadastroProdutos == 2:
                print(f"\n{cores['amarela']}=== LISTA DE PRODUTOS ==={cores['limpa']}")
                if len(produtos) == 0:
                    print(f"{cores['vermelho']}Não há nenhum produto cadastrado.{cores['limpa']}")
                    time.sleep(3)
                    continue
                else:
                    print("-" * 75)
                    print(f"{'CÓDIGO':<10} | {'NOME':<30} | {'PREÇO':<10} | {'ESTOQUE'}")
                    print("-" * 70)
                    
                    for produto in produtos:
                        print(f"{produto['Codigo']:<10} | {produto['Nome']:<30} | R$ {produto['Preco']:<7.2f} | {produto['Estoque']} un")
                    
                    print("-" * 70)
                    input("Pressione ENTER para voltar...")
            
            elif opcaoCadastroProdutos == 3:
                print(f"\n{cores['amarela']}--- ATUALIZAR NOME DO PRODUTO --- {cores['limpa']}")
                if len(produtos) == 0:
                    print(f"{cores['vermelho']}Erro! Nenhum produto cadastrado.{cores['limpa']}")
                    time.sleep(3)
                    continue
                else:
                    try:
                        codPesquisa = int(input("Informe o CÓDIGO do produto a ser alterado: "))
                    except ValueError:
                        print(f"{cores['vermelho']}Erro! Digite apenas números.")
                        continue
                    
                    produtoEncontrado = False
                    
                    for produto in produtos:
                        if produto['Codigo'] == codPesquisa:
                            produtoEncontrado = True
                            print(f"Produto Selecionado: {produto['Nome']}")
                            
                            while True:
                                novoNome = str(input("Informe o NOVO NOME: ")).strip()
                                
                                if not novoNome:
                                    print(f"{cores['vermelho']}O nome não pode ser vazio.{cores['limpa']}")
                                    continue
                                
                                nomeExiste = False
                                for verificaNomeProduto in produtos:
                                    if verificaNomeProduto['Nome'].lower() == novoNome.lower() and verificaNomeProduto['Codigo'] != codPesquisa:
                                        nomeExiste = True
                                        break
                                    
                                if nomeExiste == True:
                                    print(f"{cores['vermelho']}Erro! Já existe outro produto como o nome '{novoNome}'.{cores['limpa']}")
                                else:
                                    produto['Nome'] = novoNome
                                    print(f"{cores['verde']}Sucesso! Nome atualizado para '{novoNome}'.{cores['limpa']}")
                                    break
                            break
                    if not produtoEncontrado:
                        print(f"{cores['vermelho']}Produto com código {codPesquisa} não encontrado.{cores['limpa']}")
                        time.sleep(3)
                        continue
                    
            elif opcaoCadastroProdutos == 4:
                print(f"{cores['amarela']}--- ATUALIZAR ESTOQUE --- {cores['limpa']}")
                if len(produtos) == 0:
                    print(f"{cores['vermelho']}Erro! Nenhum produto cadastrado.{cores['limpa']}")
                    time.sleep(3)
                    continue
                
                try:
                    codPesquisa = int(input("Informe o CÓDIGO atual do produto: "))
                except ValueError:
                    print(f"{cores['vermelho']}Erro! Digite apenas números inteiros.{cores['limpa']}")
                    continue
                
                produtoEncontrado = False
                for produto in produtos:
                    if produto['Codigo'] == codPesquisa:
                        produtoEncontrado = True
                        
                        print(f"Produto: {produto['Nome']} | Estoque atual: {produto['Estoque']} unidade(s)")
                        
                        while True:
                            try:
                                novoEstoque = int(input("Informe a NOVA QUANTIDADE: "))
                                
                                if novoEstoque < 0:
                                    print(f"{cores['vermelho']}Erro! O estoque não pode ser negativo.{cores['limpa']}")
                                    continue
                                else:
                                    produto['Estoque'] = novoEstoque
                                    print(f"{cores['verde']}Suceeso! Estoque atualizado para {novoEstoque}.{cores['limpa']}")
                                    break
                                
                            except ValueError:
                                print(f"{cores['vermelho']}Erro! Digite somente números inteiros.")
                                continue
                        break
                
                if not produtoEncontrado:
                    print(f"{cores['vermelho']}Erro! Produto com código {codPesquisa} não encontrado.{cores['limpa']}")
                    time.sleep(3)
                    continue
                
            elif opcaoCadastroProdutos == 5:
                print(f"{cores['amarela']}--- ATUALIZAR CÓDIGO --- {cores['limpa']}")
                if len(produtos) == 0:
                    print(f"{cores['vermelho']}Erro! Nenhum produto cadastrado.{cores['limpa']}")
                    time.sleep(3)
                    continue
                
                try:
                    codPesquisa = int(input("Informe o CÓDIGO do produto: "))
                    
                except:
                    print(f"{cores['vermelho']}Erro! Digite somente numeros inteiros.{cores['limpa']}")
                    continue
                    
                produtoEncontrado = False
                for produto in produtos:
                    if produto['Codigo'] == codPesquisa:
                        produtoEncontrado = True
                        print(f"Produto selecionado: {produto['Nome']}(Código atual: {produto['Codigo']}).")
                        
                        while True:
                            try:
                                novoCodigo = int(input("Informe o NOVO CÓDIGO:"))
                                
                                if novoCodigo <=0:
                                    print(f"{cores['vermelho']}Erro! O código não pode ser nulo e negativo.{cores['limpa']}")
                                    continue
                                else:
                                    if novoCodigo == codPesquisa:
                                        print(f"{cores['vermelho']}O novo código deve ser diferente do código atual.{cores['limpa']}")
                                        continue
                                    
                                    codigoJaExiste = False
                                    for codigoProdutoEncontrado in produtos:
                                        if codigoProdutoEncontrado['Codigo'] == novoCodigo:
                                            codigoJaExiste = True
                                            break
                                        
                                    if codigoJaExiste:
                                        print(f"{cores['vermelho']}Erro! O código {novoCodigo} já está em uso por outro produto.{cores['limpa']}")
                                        continue
                                    else:
                                        produto['Codigo'] = novoCodigo
                                        print(f"{cores['verde']}Sucesso! Código atualizado para {novoCodigo}.{cores['limpa']}")
                                        break
                            except ValueError:
                                print(f"{cores['vermelho']}Erro! Digite somente números inteiros.")
                                continue
                        break
                    if not produtoEncontrado:
                        print(f"{cores['vermelho']}Erro! Produto com código {codPesquisa} não encontrado.{cores['limpa']}")
                        time.sleep(3)
                        continue
            elif opcaoCadastroProdutos == 6:
                print(f"{cores['amarela']}--- ATUALIZAR PREÇO --- {cores['limpa']}")
                if len(produtos) == 0:
                    print(f"{cores['vermelho']}Erro! Nenhum produto cadastrado.{cores['limpa']}")
                    time.sleep(3)
                    continue
                
                try:
                    codPesquisa = int(input("Informe o CÓDIGO do produto: "))
                except ValueError:
                    print(f"{cores['vermelho']}Erro! Somente números inteiros.")
                    continue
                
                produtoEncontrado = False
                for produto in produtos:
                    if produto['Codigo'] == codPesquisa:
                        produtoEncontrado = True
                        print(f"Produto: {produto['Nome']} | Preço Atual: {produto['Preco']:.2f}")
                        
                        while True:
                            try:
                                novoPreco = float(input("Informe o NOVO PREÇO: "))
                                
                                if novoPreco <=0:
                                    print(f"{cores['vermelho']}Erro! O preço deve ser maior que 0.")
                                    continue
                                else:
                                    produto['Preco'] = novoPreco
                                    print(f"{cores['verde']}Sucesso! Preço atualizado para R${novoPreco:.2f}.{cores['limpa']}")
                                    break
                            except ValueError:
                                print(f"{cores['vermelho']}Erro! Digite um valor numérico (Ex: 12.50).{cores['limpa']}")
                                continue
                        break
                if not produtoEncontrado:
                    print(f"{cores['vermelho']}Erro! O produto com códgo {codPesquisa} não encontrado.{cores['limpa']}")
                    time.sleep(3)
                    continue
                
            elif opcaoCadastroProdutos == 0:
                print(f"{cores['amarela']}Saindo da ferramenta 'Manutenção de Produtos'...{cores['limpa']}")
                time.sleep(3)
                break
            
            else:
                print(f"{cores['vermelho']}Erro! Opção inválida.{cores['limpa']}")
                time.sleep(2)
                continue

    elif opcaoGeral == 2:
        print("\nEntrando em Cadastro de Clientes...")
        time.sleep(2)
        print("Ação realizada com sucesso!\n")

        while True:
            print(f"""{cores['verde']}====== GESTÃO DE CLIENTES ======

1 - Cadastrar Cliente
2 - Listar Clientes
3 - Atualizar Cliente (pelo CPF)
4 - Excluir Cliente
0 - Voltar ao Menu Principal
{cores['limpa']}""")
            try:
                opcaoClientes = int(input("Informe a ação (0-4): "))
            except ValueError:
                print(f"{cores['vermelho']}Erro! Somente números inteiros.{cores['limpa']}")
                continue

            if opcaoClientes in menuClientes:
                if opcaoClientes == 0:
                    print(f"{cores['amarela']}Voltando ao menu principal...{cores['limpa']}")
                    time.sleep(2)
                    break

                elif opcaoClientes == 1:
                    print(f"\n{cores['amarela']}--- NOVO CLIENTE ---{cores['limpa']}")
                    
                    while True:
                        cpfCliente = str(input("Informe o CPF: ")).strip()
                        if not cpfCliente:
                            print(f"{cores['vermelho']}O CPF não pode ser vazio.{cores['limpa']}")
                            continue
                        
                        cpfExiste = False
                        for cliente in clientes:
                            if cliente["CPF"] == cpfCliente:
                                cpfExiste = True
                                break
                        
                        if cpfExiste:
                            print(f"{cores['vermelho']}Erro! CPF já cadastrado.{cores['limpa']}")
                        else:
                            break
                    
                    nomeCliente = str(input("Nome Completo: ")).strip()
                    emailCliente = str(input("E-mail: ")).strip()
                    foneCliente = str(input("Telefone: ")).strip()
                    cidadeCliente = str(input("Cidade: ")).strip()

                    novoCliente = {
                        "CPF": cpfCliente,
                        "Nome": nomeCliente,
                        "Email": emailCliente,
                        "Fone": foneCliente,
                        "Cidade": cidadeCliente
                    }
                    clientes.append(novoCliente)
                    print(f"{cores['verde']}Cliente cadastrado com sucesso!{cores['limpa']}")
                    time.sleep(1)

                elif opcaoClientes == 2:
                    print(f"\n{cores['amarela']}=== LISTA DE CLIENTES ==={cores['limpa']}")
                    if len(clientes) == 0:
                        print(f"{cores['vermelho']}Nenhum cliente cadastrado.{cores['limpa']}")
                        time.sleep(2)
                    else:
                        print("-" * 80)
                        print(f"{'CPF':<15} | {'NOME':<25} | {'CIDADE':<15} | {'FONE'}")
                        print("-" * 80)
                        for c in clientes:
                            print(f"{c['CPF']:<15} | {c['Nome']:<25} | {c['Cidade']:<15} | {c['Fone']}")
                        print("-" * 80)
                        input("Pressione ENTER para voltar...")

                elif opcaoClientes == 3:
                    if len(clientes) == 0:
                        print(f"{cores['vermelho']}Nenhum cliente cadastrado.{cores['limpa']}")
                        time.sleep(2)
                        continue

                    cpfPesquisa = str(input("Informe o CPF do cliente para atualizar: ")).strip()
                    encontrado = False
                    
                    for c in clientes:
                        if c['CPF'] == cpfPesquisa:
                            encontrado = True
                            print(f"Cliente selecionado: {c['Nome']}")
                            
                            novoNome = str(input("Novo Nome: ")).strip()
                            if novoNome:
                                c['Nome'] = novoNome
                                print(f"{cores['verde']}Nome atualizado com sucesso!{cores['limpa']}")
                            break
                    
                    if not encontrado:
                        print(f"{cores['vermelho']}Cliente não encontrado.{cores['limpa']}")
                        time.sleep(2)

                elif opcaoClientes == 4:
                    if len(clientes) == 0:
                        print(f"{cores['vermelho']}Nenhum cliente cadastrado.{cores['limpa']}")
                        time.sleep(2)
                        continue

                    cpfPesquisa = str(input("Informe o CPF para excluir: ")).strip()
                    encontrado = False

                    for c in clientes:
                        if c['CPF'] == cpfPesquisa:
                            encontrado = True
                            clientes.remove(c)
                            print(f"{cores['verde']}Cliente removido do sistema.{cores['limpa']}")
                            break
                    
                    if not encontrado:
                        print(f"{cores['vermelho']}Cliente não encontrado.{cores['limpa']}")
                        time.sleep(2)

            else:
                print(f"{cores['vermelho']}Opção inválida! Escolha entre 0 e 4.{cores['limpa']}")
                time.sleep(2)

    elif opcaoGeral == 3:
        print(f"\n{cores['verde']}Entrando no Sistema de Vendas (Caixa)...{cores['limpa']}")
        time.sleep(2)

        while True:
            print(f"""{cores['verde']}
====== CAIXA / VENDAS ======
1 - Adicionar Produto ao Carrinho
2 - Ver Carrinho de Compras
3 - Finalizar Venda (Checkout)
0 - Cancelar e Voltar
{cores['limpa']}""")
            try:
                opcaoVenda = int(input("Informe a ação (0-3): "))
            except ValueError:
                print(f"{cores['vermelho']}Erro! Somente números inteiros.{cores['limpa']}")
                continue
            
            if opcaoVenda in menuVenda:
                if opcaoVenda == 0:
                    if len(carrinho) > 0:
                        print(f"{cores['vermelho']}Cancelando venda... Devolvendo itens ao estoque...{cores['limpa']}")
                        for item in carrinho:
                            for produto in produtos:
                                if produto['Codigo'] == item['Codigo']:
                                    produto['Estoque'] += item['Quantidade']
                        carrinho = []
                    
                    print("Voltando ao menu principal...")
                    time.sleep(2)
                    break

                elif opcaoVenda == 1:
                    print(f"\n{cores['amarela']}--- ADICIONAR ITEM ---{cores['limpa']}")
                    
                    if len(produtos) == 0:
                        print(f"{cores['vermelho']}Não há produtos cadastrados no sistema.{cores['limpa']}")
                        time.sleep(2)
                        continue

                    try:
                        codVenda = int(input("Informe o CÓDIGO do produto: "))
                    except ValueError:
                        print(f"{cores['vermelho']}Erro! Digite apenas números.{cores['limpa']}")
                        continue

                    produtoEncontrado = False
                    for produto in produtos:
                        if produto['Codigo'] == codVenda:
                            produtoEncontrado = True
                            print(f"Produto: {produto['Nome']} | Preço: R$ {produto['Preco']:.2f} | Disponível: {produto['Estoque']}")
                            
                            while True:
                                try:
                                    qtdVenda = int(input("Quantidade a vender: "))
                                    
                                    if qtdVenda <= 0:
                                        print(f"{cores['vermelho']}A quantidade deve ser maior que zero.{cores['limpa']}")
                                        continue
                                    
                                    if qtdVenda > produto['Estoque']:
                                        print(f"{cores['vermelho']}Erro! Estoque insuficiente. Só temos {produto['Estoque']} un.{cores['limpa']}")
                                        continue
                                    
                                    produto['Estoque'] -= qtdVenda
                                    
                                    subtotal = qtdVenda * produto['Preco']
                                    
                                    itemCarrinho = {
                                        "Codigo": produto['Codigo'],
                                        "Nome": produto['Nome'],
                                        "Preco": produto['Preco'],
                                        "Quantidade": qtdVenda,
                                        "Subtotal": subtotal
                                    }
                                    carrinho.append(itemCarrinho)
                                    print(f"{cores['verde']}Item adicionado ao carrinho!{cores['limpa']}")
                                    break
                                
                                except ValueError:
                                    print(f"{cores['vermelho']}Erro! Quantidade inválida.{cores['limpa']}")
                            break
                    
                    if not produtoEncontrado:
                        print(f"{cores['vermelho']}Produto não encontrado.{cores['limpa']}")
                        time.sleep(2)

                elif opcaoVenda == 2:
                    print(f"\n{cores['amarela']}=== SEU CARRINHO ==={cores['limpa']}")
                    
                    if len(carrinho) == 0:
                        print(f"{cores['vermelho']}O carrinho está vazio.{cores['limpa']}")
                    else:
                        print("-" * 70)
                        print(f"{'PRODUTO':<20} | {'QTD':<5} | {'UNITÁRIO':<10} | {'SUBTOTAL'}")
                        print("-" * 70)
                        
                        totalTemporario = 0
                        for item in carrinho:
                            print(f"{item['Nome']:<20} | {item['Quantidade']:<5} | R$ {item['Preco']:<8.2f} | R$ {item['Subtotal']:.2f}")
                            totalTemporario += item['Subtotal']
                        
                        print("-" * 70)
                        print(f"{cores['verde']}TOTAL PARCIAL: R$ {totalTemporario:.2f}{cores['limpa']}")
                    
                    input("Pressione ENTER para voltar...")

                elif opcaoVenda == 3:
                    if len(carrinho) == 0:
                        print(f"{cores['vermelho']}Erro! Carrinho vazio. Adicione itens antes.{cores['limpa']}")
                        time.sleep(2)
                        continue
                    
                    print(f"\n{cores['amarela']}================ CUPOM FISCAL =============={cores['limpa']}")
                    print("-" * 70)
                    print(f"{'PRODUTO':<20} | {'QTD':<5} | {'PREÇO':<10} | {'SUBTOTAL'}")
                    print("-" * 70)
                    
                    totalGeral = 0
                    for item in carrinho:
                        print(f"{item['Nome']:<20} | {item['Quantidade']:<5} | R$ {item['Preco']:<8.2f} | R$ {item['Subtotal']:.2f}")
                        totalGeral += item['Subtotal']
                    
                    impNacional = totalGeral * 0.05
                    impEstadual = totalGeral * 0.08
                    impMunicipal = totalGeral * 0.12
                    
                    print("-" * 70)
                    print(f"Subtotal dos Itens:   R$ {totalGeral:.2f}")
                    print(f"Imposto Nacional (5%): R$ {impNacional:.2f}")
                    print(f"Imposto Estadual (8%): R$ {impEstadual:.2f}")
                    print(f"Imposto Municipal(12%):R$ {impMunicipal:.2f}")
                    print("=" * 70)
                    print(f"{cores['verde']}TOTAL A PAGAR:        R$ {totalGeral:.2f}{cores['limpa']}")
                    print("=" * 70)
                    
                    try:
                        confirma = int(input("Confirmar venda? (1-SIM / 0-NÃO): "))
                        if confirma == 1:
                            print(f"\n{cores['verde']}VENDA FINALIZADA COM SUCESSO! OBRIGADO.{cores['limpa']}")
                            carrinho = []
                            time.sleep(3)
                            break
                        else:
                            print(f"{cores['vermelho']}Venda não finalizada. Volte ao carrinho.{cores['limpa']}")
                            time.sleep(2)
                    except ValueError:
                        print("Opção inválida.")
            
            else:
                print(f"{cores['vermelho']}Opção inválida! Escolha entre 0 e 3.{cores['limpa']}")
                time.sleep(2)
                
    elif opcaoGeral == 0:
        print(f"{cores['amarela']}Encerrando o sistema... até mais!{cores['limpa']}")
        time.sleep(2)
        break
    else:
        print(f"{cores['vermelho']}Opção inváçida!{cores['limpa']}")
        time.sleep(2)