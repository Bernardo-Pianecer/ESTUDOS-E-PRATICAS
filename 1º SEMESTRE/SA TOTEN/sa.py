import os
import time

pao = ["pao australiano",  #index 0
    "pao brioche", #index 1
    "pao com gergelim",] #index 2
    
valor_pao = [3.00, #index 0
            2.50, #index 1
            2.00,] #index 2

carne = ["carne bovina", #index 0
        "carne de frango", #index 1
        "carne de porco",] #index 2

valor_carne = [5.00, #index 0
            4.00, #index 1
            4.50,] #index 2

ponto_carne = ["mal passada", #index 0
        "ao ponto", #index 1
        "bem passada", #index 2
        "Sem ponto"] #index 3


salada = ["alface", #index 0
        "tomate",  #index 1
        "cebola", #index 2
        "picles", #index 3
        "Sem salada"] #index 4

valor_salada = [0.50, #index 0
            0.50, #index 1
            0.50, #index 2
            0.50, #index 3
            0.00] #index 4

molhos = ["maionese", #index 0
        "ketchup", #index 1
        "mostarda", #index 2
        "barbecue", #index 3
        "Sem molho"] #index 4
        
valor_molhos = [0.50, #index 0
            0.50, #index 1
            0.50, #index 2
            0.50, #index 3
            0.00] #index 4

pedido_atual = []
valor_acumulado = 0.00

senhaOficial = None  # Variável global para armazenar a senha oficial

listaPedidos = []  # Lista para armazenar os pedidos realizados

pedidosAtivos = []  # Lista para armazenar os pedidos ativos

def telaInicial():
    os.system("cls")
    print("=================================")
    print("BEM VINDO AO SISTEMA BURGUER TECH")
    print("=================================")
    print("Voce é:")
    print("(1) - Cozinheiro")
    print("(2) - User")
    tipoLogin = int(input("Digite aqui a opção(NUMERO): -> "))
    if tipoLogin == 1:
        tipoLoginCoz()
    elif tipoLogin == 2:
        telaPedido()
    else:
        os.system("cls")
        print("CODIGO INVALIDO")
        time.sleep(3)
        telaInicial()

def tipoLoginCoz():
    os.system("cls")
    print("=================================")
    print("----------TELA LOGIN-------------")
    print("=================================")
    print("É seu primeiro acesso?")
    print("(1) - Sim")
    print("(2) - Não")
    print("(3) - Voltar")
    primeiroAcesso = int(input("Digite aqui a opção(NUMERO): -> "))
    if primeiroAcesso == 1:
        primeiroAcessoSim()
    elif primeiroAcesso == 2:
        primeiroAcessoNão(senhaOficial)
    elif primeiroAcesso == 3:
        telaInicial()
    else:
        os.system("cls")
        print("senhas não coincidem")
        time.sleep(1)
        primeiroAcessoSim()

def primeiroAcessoSim():
        os.system("cls")
        print("=================================")
        print("-------CRIAÇÃO DA SENHA----------")
        print("=================================")
        voltar = int(input("Deseja voltar? (1) - Sim (2) - Não: -> "))
        if voltar == 1:
            telaInicial()
        elif voltar == 2:
            print("Coloque a sua Senha")
            senha = str(input("Aqui: ->"))
            os.system("cls")
            print("=================================")
            print("-------CRIAÇÃO DA SENHA----------")
            print("=================================")
            print("Confirme sua senha:")
            confirmarSenha = str(input("Aqui ->"))
            if senha == confirmarSenha:
                senhaOficial = confirmarSenha
                primeiroAcessoNão(senhaOficial)
            else:
                os.system("cls")
                print("senhas não coincidem")
                time.sleep(1)
                primeiroAcessoSim()
        else:
            os.system("cls")
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(2)
            primeiroAcessoSim()

def primeiroAcessoNão(senha):
        os.system("cls")
        print("=================================")
        print("----------TELA LOGIN-------------")
        print("=================================")
        voltar = int(input("Deseja voltar? (1) - Sim (2) - Não: -> "))
        if voltar == 1:
            telaInicial()
        elif voltar == 2:
            print("Qual a senha?")
            tentarSenha = str(input("Aqui ->"))
            if tentarSenha == senha:
                telaInicialChef()
            else:
                os.system("cls")
                print("SENHA INCORRETA")
                time.sleep(1)
                primeiroAcessoNão(senha)
        else:
            os.system("cls")
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(2)
            primeiroAcessoNão(senha)


def telaInicialChef():
    os.system("cls")
    print("=================================")
    print("---------TELA INICIAL------------")
    print("=================================")
    qualPedidosVer = int("Qual pedidos você quer acessar?" \
    "(1) - Pedidos Ativos" \
    "(2) - Pedidos Realizados")
    if qualPedidosVer == 1:
        verPedidosAtivos()
    elif qualPedidosVer == 2:
        mostrarPedidos()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        telaInicialChef()




def mostrarPedidos():
    os.system("cls")
    print("=================================")
    print("---------PEDIDOS REALIZADOS-------")
    print("=================================")
    if not listaPedidos:
        print("Nenhum pedido realizado ainda.")
    else:
        for i, pedido in enumerate(listaPedidos, start=1):
            print(f"Pedido {i}:")
            for item in pedido:
                print(f"  - {item['nome']}: {item['descricao']} - R${item['preco']:.2f}")
            total = sum(item['preco'] for item in pedido)
            print(f"  Total: R${total:.2f}")
            print("-" * 40)
            ativo = input("Deseja marcar este pedido como ativo? (1) - Sim (2) - Não: -> ")
            if ativo == '1':
                pedidosAtivos.append(pedido)
                print("Pedido marcado como ativo.")
            elif ativo == '2':
                print("Pedido não marcado como ativo.")
            else:
                print("Opção inválida. Pedido não marcado como ativo.")    
    input("Pressione Enter para voltar ao menu inicial...")
    verPedidosAtivos()

def verPedidosAtivos():
    os.system("cls")
    print("=================================")
    print("---------PEDIDOS ATIVOS----------")
    print("=================================")

    if not pedidosAtivos:
        print("Nenhum pedido ativo no momento.")
    else:
        for i, pedido in enumerate(pedidosAtivos, start=1):
            print(f"Pedido Ativo {i}:")
            for item in pedido:
                print(f"  - {item['nome']}: {item['descricao']} - R${item['preco']:.2f}")
            total = sum(item['preco'] for item in pedido)
            print(f"  Total: R${total:.2f}")
            print("-" * 40)
    input("Pressione Enter para voltar ao menu inicial...")











def telaPedido():
    os.system("cls")
    print("=================================")
    print("---------INICIAR PEDIDO----------")
    print("=================================")
    print("--------MONTAR O HAMBURGUER------")
    print("=================================")
    print("Deseja comecar")
    print("(1) - Sim")
    print("(2) - Não")
    pedido= int(input("Digite aqui a opcao(NUMERO): -> "))
    if pedido == 1:
        telaPedidoPão()
    else:
        print("Voce saiu")
        time.sleep(1.5)
        telaInicial()

def telaPedidoPão():    
        os.system("cls")
        print("=" * 40)
        print(f"{'Nº':<4} | {'ITEM':<20} | {'PREÇO':<10}")
        print("-" * 40)
        escolhaPao=int(input("Deseja escolher o pão? (1) - Sim (2) - Não: -> "))
        if escolhaPao == 1:
            cardapioPão()
        elif escolhaPao == 2:
            print("Você optou por não escolher o pão.")
            time.sleep(1.5)
            telaPedidoCarne()
        else:
            os.system("cls")
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(2)
            telaPedidoPão()

def cardapioPão():
        print(f"(1) Pão Brioche {valor_pao[0]:.2f}")
        print(f"(2) Pão com Gergelim {valor_pao[1]:.2f}")
        print(f"(3) Pão Australiano {valor_pao[2]:.2f}")
        pao =int(input("Pão desejado: ->"))
        if pao == 1:
            pao = "Pão Brioche"
            print("pao escolhido",pao)
            pedido_atual.append({"nome": "Pão", "descricao": pao, "preco": valor_pao[0]})
            time.sleep(1.5)
            telaPedidoCarne()
        elif pao == 2:
            pao = "Pão com Gergelim"
            print("pao escolhido",pao)
            pedido_atual.append({"nome": "Pão", "descricao": pao, "preco": valor_pao[1]})
            time.sleep(1.5)
            telaPedidoCarne()
        elif pao == 3:
            pao = "Pão Australiano"
            print("pao escolhido",pao)
            pedido_atual.append({"nome": "Pão", "descricao": pao, "preco": valor_pao[2]})
            time.sleep(1.5)
            telaPedidoCarne()
        else:
            os.system("cls")
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(2)
            telaPedidoPão()

def telaPedidoCarne():
    os.system("cls")
    print("=" * 40)
    print(f"{'Nº':<4} | {'ITEM':<20} | {'PREÇO':<10}")
    print("-" * 40)
    for item in pedido_atual:
        print(f"{item['nome']:<4} | {item['descricao']:<20} | {item['preco']:<10.2f}")
    print("-" * 40)
    escolhaCarne=int(input("Deseja escolher a carne? (1) - Sim (2) - Não: -> "))
    if escolhaCarne == 1:
        cardapioCarne()
    elif escolhaCarne == 2:
        print("Você optou por não escolher a carne.")
        time.sleep(1.5)
        telaPedidoSalada()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        telaPedidoCarne()


def cardapioCarne():
        print(f"(1) Carne Bovina {valor_carne[0]:.2f}")
        print(f"(2) Carne de Frango {valor_carne[1]:.2f}")
        print(f"(3) Carne de Porco {valor_carne[2]:.2f}")
        carne =int(input("Carne desejada: ->"))
        if carne == 1:
            carne = "Carne Bovina"
            print("carne escolhida",carne)
            pedido_atual.append({"nome": "Carne", "descricao": carne, "preco": valor_carne[0]})
            time.sleep(1.5)
            pontosCarne()
        elif carne == 2:
            carne = "Carne de Frango"
            print("carne escolhida",carne)
            pedido_atual.append({"nome": "Carne", "descricao": carne, "preco": valor_carne[1]})
            time.sleep(1.5)
            pontosCarne()
        elif carne == 3:
            carne = "Carne de Porco"
            print("carne escolhida",carne)
            pedido_atual.append({"nome": "Carne", "descricao": carne, "preco": valor_carne[2]})
            time.sleep(1.5)
            pontosCarne()
        else:
            os.system
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(2)
            telaPedidoCarne()

def pontosCarne():
    os.system("cls")
    print("=" * 40)
    print(f"{'Nº':<4} | {'ITEM':<20} | {'PREÇO':<10}")
    print("-" * 40)
    for item in pedido_atual:
        print(f"{item['nome']:<4} | {item['descricao']:<20} | {item['preco']:<10.2f}")
    print("-" * 40)
    
    escolhaPontoCarne=int(input("Deseja escolher o ponto da carne? (1) - Sim (2) - Não: -> "))
    if escolhaPontoCarne == 1:
        cardapioPontoCarne()
    elif escolhaPontoCarne == 2:
        print("Você optou por não escolher o ponto da carne.")
        time.sleep(1.5)
        telaPedidoSalada()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        pontosCarne()

def cardapioPontoCarne():
        print("(1) Mal Passada ")
        print("(2) Ao Ponto")
        print("(3) Bem Passada")
        ponto_carne =int(input("Ponto da carne desejado: ->"))
        if ponto_carne == 1:
            ponto_carne = "Mal Passada"
            print("ponto da carne escolhida",ponto_carne)
            
            time.sleep(1.5)
            telaPedidoSalada()
        elif ponto_carne == 2:
            ponto_carne = "Ao Ponto"
            print("ponto da carne escolhida",ponto_carne)
            
            time.sleep(1.5)
            telaPedidoSalada()
        elif ponto_carne == 3:
            ponto_carne = "Bem Passada"
            print("ponto da carne escolhida",ponto_carne)
            
            time.sleep(1.5)
            telaPedidoSalada()
        else:
            os.system
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(2)
            telaPedidoCarne()

def telaPedidoSalada():
    os.system("cls")
    print("=" * 40)
    print(f"{'Nº':<4} | {'ITEM':<20} | {'PREÇO':<10}")
    print("-" * 40)
    for item in pedido_atual:
        print(f"{item['nome']:<4} | {item['descricao']:<20} | {item['preco']:<10.2f}")
    print("-" * 40)
    escolhaSalada=int(input("Deseja escolher a salada? (1) - Sim (2) - Não: -> "))
    if escolhaSalada == 1:
        cardapioSalada()
    elif escolhaSalada == 2:
        print("Você optou por não escolher a salada.")
        time.sleep(1.5)
        telaPedidoMolho()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        telaPedidoSalada()

def cardapioSalada():
        print(f"(1) Alface {valor_salada[0]:.2f}")
        print(f"(2) Tomate {valor_salada[1]:.2f}")
        print(f"(3) Cebola {valor_salada[2]:.2f}")
        print(f"(4) Picles {valor_salada[3]:.2f}")
        salada =int(input("Salada desejada: ->"))
        if salada == 1:
            salada = "Alface"
            print("salada escolhida",salada)
            pedido_atual.append({"nome": "Salada", "descricao": salada, "preco": valor_salada[0]})
            time.sleep(1.5)
            telaPedidoMolho()
        elif salada == 2:
            salada = "Tomate"
            print("salada escolhida",salada)
            pedido_atual.append({"nome": "Salada", "descricao": salada, "preco": valor_salada[1]})
            time.sleep(1.5)
            telaPedidoMolho()
        elif salada == 3:
            salada = "Cebola"
            print("salada escolhida",salada)
            pedido_atual.append({"nome": "Salada", "descricao": salada, "preco": valor_salada[2]})
            time.sleep(1.5)
            telaPedidoMolho()
        elif salada == 4:
            salada = "Picles"
            print("salada escolhida",salada)
            pedido_atual.append({"nome": "Salada", "descricao": salada, "preco": valor_salada[3]})
            time.sleep(1.5)
            telaPedidoMolho()
        else:
            os.system("cls")
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(2)
            telaPedidoSalada()


def telaPedidoMolho():
    os.system("cls")
    print("=" * 40)
    print(f"{'Nº':<4} | {'ITEM':<20} | {'PREÇO':<10}")
    print("-" * 40)
    for item in pedido_atual:
        print(f"{item['nome']:<4} | {item['descricao']:<20} | {item['preco']:<10.2f}")
    print("-" * 40)
    escolhaMolho=int(input("Deseja escolher o molho? (1) - Sim (2) - Não: -> "))
    if escolhaMolho == 1:
        cardapioMolho()
    elif escolhaMolho == 2:
        print("Você optou por não escolher o molho.")
        time.sleep(1.5)
        confirmarPedido()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        telaPedidoMolho()

def cardapioMolho():
        print(f"(1) Maionese {valor_molhos[0]:.2f}")
        print(f"(2) Ketchup {valor_molhos[1]:.2f}")
        print(f"(3) Mostarda {valor_molhos[2]:.2f}")
        print(f"(4) Barbecue {valor_molhos[3]:.2f}")
        molho =int(input("Molho desejado: ->"))
        if molho == 1:
            molho = "Maionese"
            print("molho escolhido",molho)
            pedido_atual.append({"nome": "Molho", "descricao": molho, "preco": valor_molhos[0]})
            time.sleep(1.5)
            confirmarPedido()
        elif molho == 2:
            molho = "Ketchup"
            print("molho escolhido",molho)
            pedido_atual.append({"nome": "Molho", "descricao": molho, "preco": valor_molhos[1]})
            time.sleep(1.5)
            confirmarPedido()
        elif molho == 3:
            molho = "Mostarda"
            print("molho escolhido",molho)
            pedido_atual.append({"nome": "Molho", "descricao": molho, "preco": valor_molhos[2]})
            time.sleep(1.5)
            confirmarPedido()
        elif molho == 4:
            molho = "Barbecue"
            print("molho escolhido",molho)
            pedido_atual.append({"nome": "Molho", "descricao": molho, "preco": valor_molhos[3]})
            time.sleep(1.5)
            confirmarPedido()
        else:
            os.system
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(2)
            telaPedidoMolho()

def confirmarPedido():
    os.system("cls")
    print("=" * 40)
    print(f"{'Nº':<4} | {'ITEM':<20} | {'PREÇO':<10}")
    print("-" * 40)
    print("Resumo do pedido:")
    for item in pedido_atual:
        print(f"{item['nome']:<4} | {item['descricao']:<20} | {item['preco']:<10.2f}")
    print("-" * 40)
    print(f"{'TOTAL':<4} | {'':<20} | {sum(item['preco'] for item in pedido_atual):<10.2f}")
    print("-" * 40)
    print(f"OBS: {ponto_carne if 'ponto_carne' in locals() else 'Sem ponto'}")
    print("-" * 40)
    print("(1) - Sim")
    print("(2) - Não")
    alterarPedido = int(input("Deseja alterar o pedido?"))
    if alterarPedido == 1:
        qualAteração()
    else:
        os.system("cls")
        print("=" * 40)
        print(f"{'Nº':<4} | {'ITEM':<20} | {'PREÇO':<10}")
        print("-" * 40)
        print("Resumo do pedido:")
        for item in pedido_atual:
            print(f"{item['nome']:<4} | {item['descricao']:<20} | {item['preco']:<10.2f}")
        print("-" * 40)
        print(f"{'TOTAL':<4} | {'':<20} | {sum(item['preco'] for item in pedido_atual):<10.2f}")
        print("-" * 40)
        print(f"OBS: {ponto_carne if 'ponto_carne' in locals() else 'Sem ponto'}")
        print("-" * 40)
        print("Deseja confirmar o pedido?")
        print("(1) - Sim")
        print("(2) - Não")
        confirmarPedido = int(input("Digite aqui a opção(NUMERO): -> "))
        if confirmarPedido == 1:
            os.system("cls")
            print("Pedido confirmado! Obrigado por comprar conosco.")
            time.sleep(2)
            listaPedidos.append(pedido_atual.copy())  # Adiciona o pedido atual à lista de pedidos
            telaInicial()
        elif confirmarPedido == 2:
            os.system("cls")
            print("Pedido cancelado. Retornando ao menu inicial.")
            time.sleep(2)
            telaPedido()
        else:
            os.system("cls")
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(2)
            confirmarPedido()

def qualAteração():
    os.system("cls")
    print("=================================")
    print("O QUE VOCE QUER FAZER?")
    print("=================================")
    print("(1) - Adicionar item")
    print("(2) - Remover item")
    print("(3) - Alterar item")
    print("(4) - Voltar")
    desejoAlterar = int(input("Digite aqui a opcao(NUMERO): -> "))
    if desejoAlterar == 1:
        telaQualAdd()
    elif desejoAlterar == 2:
        telaQualRemover()
    elif desejoAlterar == 3:
        telaQualAlterar()
    elif desejoAlterar == 4:
        confirmarPedido()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        qualAteração()



def telaQualAdd():
    os.system("cls")
    print("=================================")
    print("---------ADICIONAR ITEM----------")
    print("=================================") 
    print("Qual item deseja adicionar?")
    print("(1) - Pão")
    print("(2) - Carne")
    print("3) - Salada")
    print("4) - Molho")
    print("5) - Voltar")
    qualAdd = int(input("Digite aqui a opcao(NUMERO): -> "))
    if qualAdd == 1:
        telaPedidoPão()
    elif qualAdd == 2:
        telaPedidoCarne()
    elif qualAdd == 3:
        telaPedidoSalada()
    elif qualAdd == 4:
        telaPedidoMolho()
    elif qualAdd == 5:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        telaQualAdd()

def telaQualRemover():
    os.system("cls")
    print("=================================")
    print("---------REMOVER ITEM------------")
    print("=================================") 
    print("Qual item deseja remover?")
    print("(1) - Pão")
    print("(2) - Carne")
    print("3) - Salada")
    print("4) - Molho")
    print("5) - Voltar")
    qualRemover = int(input("Digite aqui a opcao(NUMERO): -> "))
    if qualRemover == 1:
        removerPão()
    elif qualRemover == 2:
        removerCarne()
    elif qualRemover == 3:
        removerSalada()
    elif qualRemover == 4:
        removerMolho()
    elif qualRemover == 5:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        telaQualRemover()

def removerPão():
    os.system("cls")
    print("=================================")
    print("---------REMOVER PÃO-------------")
    print("=================================") 
    print("Deseja remover o pão do pedido?")
    print("(1) - Sim")
    print("(2) - Não")
    removerPao = int(input("Digite aqui a opcao(NUMERO): -> "))
    if removerPao == 1:
        for item in pedido_atual:
            if item['nome'] == "Pão":
                print(f"Removendo {item['descricao']} do pedido.")
                confirma = input("Tem certeza que deseja remover o pão do pedido? (1 - Sim, 2 - Não): ")
                if confirma == '1':
                    pedido_atual.remove(item)
                    print("Pão removido do pedido.")
                elif confirma == '2':
                    print("Remoção do pão cancelada.")
                else:
                    print("Opção inválida. Retornando ao menu de alterações.")
                time.sleep(1.5)
                qualAteração()
                return
            
        print("Não há pão no pedido para remover.")
        time.sleep(1.5)
        qualAteração()
    elif removerPao == 2:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        removerPão()

def removerCarne():
    os.system("cls")
    print("=================================")
    print("---------REMOVER CARNE-----------")
    print("=================================") 
    print("Deseja remover a carne do pedido?")
    print("(1) - Sim")
    print("(2) - Não")
    removerCarne = int(input("Digite aqui a opcao(NUMERO): -> "))
    if removerCarne == 1:
        for item in pedido_atual:
            if item['nome'] == "Carne":
                print(f"Removendo {item['descricao']} do pedido.")
                confirma = input("Tem certeza que deseja remover a carne do pedido? (1 - Sim, 2 - Não): ")
                if confirma == '1':
                    pedido_atual.remove(item)
                    print("Carne removida do pedido.")
                elif confirma == '2':
                    print("Remoção da carne cancelada.")
                else:
                    print("Opção inválida. Retornando ao menu de alterações.")
                time.sleep(1.5)
                qualAteração()
                return
            
        print("Não há carne no pedido para remover.")
        time.sleep(1.5)
        qualAteração()
    elif removerCarne == 2:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        removerCarne()

def removerSalada():
    os.system("cls")
    print("=================================")
    print("---------REMOVER SALADA----------")
    print("=================================") 
    print("Deseja remover a salada do pedido?")
    print("(1) - Sim")
    print("(2) - Não")
    removerSalada = int(input("Digite aqui a opcao(NUMERO): -> "))
    if removerSalada == 1:
        for item in pedido_atual:
            if item['nome'] == "Salada":
                print(f"Removendo {item['descricao']} do pedido.")
                confirma = input("Tem certeza que deseja remover a salada do pedido? (1 - Sim, 2 - Não): ")
                if confirma == '1':
                    pedido_atual.remove(item)
                    print("Salada removida do pedido.")
                elif confirma == '2':
                    print("Remoção da salada cancelada.")
                else:
                    print("Opção inválida. Retornando ao menu de alterações.")
                time.sleep(1.5)
                qualAteração()
                return
            
        print("Não há salada no pedido para remover.")
        time.sleep(1.5)
        qualAteração()
    elif removerSalada == 2:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        removerSalada()
    
def removerMolho():
    os.system("cls")
    print("=================================")
    print("---------REMOVER MOLHO-----------")
    print("=================================") 
    print("Deseja remover o molho do pedido?")
    print("(1) - Sim")
    print("(2) - Não")
    removerMolho = int(input("Digite aqui a opcao(NUMERO): -> "))
    if removerMolho == 1:
        for item in pedido_atual:
            if item['nome'] == "Molho":
                print(f"Removendo {item['descricao']} do pedido.")
                confirma = input("Tem certeza que deseja remover o molho do pedido? (1 - Sim, 2 - Não): ")
                if confirma == '1':
                    pedido_atual.remove(item)
                    print("Molho removido do pedido.")
                elif confirma == '2':
                    print("Remoção do molho cancelada.")
                else:
                    print("Opção inválida. Retornando ao menu de alterações.")
                time.sleep(1.5)
                qualAteração()
                return
            
        print("Não há molho no pedido para remover.")
        time.sleep(1.5)
        qualAteração()
    elif removerMolho == 2:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        removerMolho()


def telaQualAlterar():
    os.system("cls")
    print("=================================")
    print("---------ALTERAR ITEM------------")
    print("=================================") 
    print("Qual item deseja alterar?")
    print("(1) - Pão")
    print("(2) - Carne")
    print("3) - Salada")
    print("4) - Molho")
    print("5) - Voltar")
    qualAlterar = int(input("Digite aqui a opcao(NUMERO): -> "))
    if qualAlterar == 1:
        alterarPão()
    elif qualAlterar == 2:
        alterarCarne()
    elif qualAlterar == 3:
        alterarSalada()
    elif qualAlterar == 4:
        alterarMolho()
    elif qualAlterar == 5:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        telaQualAlterar()

def alterarPão():
    os.system("cls")
    print("=================================")
    print("---------ALTERAR PÃO-------------")
    print("=================================") 
    print("Deseja alterar o pão do pedido?")
    print("(1) - Sim")
    print("(2) - Não")
    alterarPao = int(input("Digite aqui a opcao(NUMERO): -> "))
    if alterarPao == 1:
        for item in pedido_atual:
            if item['nome'] == "Pão":
                print(f"Removendo {item['descricao']} do pedido.")
                confirma = input("Tem certeza que deseja alterar o pão do pedido? (1 - Sim, 2 - Não): ")
                if confirma == '1':
                    pedido_atual.remove(item)
                    print("Pão removido do pedido. Agora você pode escolher um novo pão.")
                    telaPedidoPão()
                elif confirma == '2':
                    print("Alteração do pão cancelada.")
                else:
                    print("Opção inválida. Retornando ao menu de alterações.")
                time.sleep(1.5)
        print("Não há pão no pedido para alterar.")
        time.sleep(1.5)
        qualAteração()
    elif alterarPao == 2:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        alterarPão()

def alterarCarne():
    os.system("cls")
    print("=================================")
    print("---------ALTERAR CARNE-----------")
    print("=================================") 
    print("Deseja alterar a carne do pedido?")
    print("(1) - Sim")
    print("(2) - Não")
    alterarCarne = int(input("Digite aqui a opcao(NUMERO): -> "))
    if alterarCarne == 1:
        for item in pedido_atual:
            if item['nome'] == "Carne":
                print(f"Removendo {item['descricao']} do pedido.")
                confirma = input("Tem certeza que deseja alterar a carne do pedido? (1 - Sim, 2 - Não): ")
                if confirma == '1':
                    pedido_atual.remove(item)
                    print("Carne removida do pedido. Agora você pode escolher uma nova carne.")
                    telaPedidoCarne()
                elif confirma == '2':
                    print("Alteração da carne cancelada.")
                else:
                    print("Opção inválida. Retornando ao menu de alterações.")
                time.sleep(1.5)
        print("Não há carne no pedido para alterar.")
        time.sleep(1.5)
        qualAteração()
    elif alterarCarne == 2:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        alterarCarne()

def alterarSalada():
    os.system("cls")
    print("=================================")
    print("---------ALTERAR SALADA----------")
    print("=================================") 
    print("Deseja alterar a salada do pedido?")
    print("(1) - Sim")
    print("(2) - Não")
    alterarSalada = int(input("Digite aqui a opcao(NUMERO): -> "))
    if alterarSalada == 1:
        for item in pedido_atual:
            if item['nome'] == "Salada":
                print(f"Removendo {item['descricao']} do pedido.")
                confirma = input("Tem certeza que deseja alterar a salada do pedido? (1 - Sim, 2 - Não): ")
                if confirma == '1':
                    pedido_atual.remove(item)
                    print("Salada removida do pedido. Agora você pode escolher uma nova salada.")
                    telaPedidoSalada()
                elif confirma == '2':
                    print("Alteração da salada cancelada.")
                else:
                    print("Opção inválida. Retornando ao menu de alterações.")
                time.sleep(1.5)
        print("Não há salada no pedido para alterar.")
        time.sleep(1.5)
        qualAteração()
    elif alterarSalada == 2:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        alterarSalada()

def alterarMolho():
    os.system("cls")
    print("=================================")
    print("---------ALTERAR MOLHO-----------")
    print("=================================") 
    print("Deseja alterar o molho do pedido?")
    print("(1) - Sim")
    print("(2) - Não")
    alterarMolho = int(input("Digite aqui a opcao(NUMERO): -> "))
    if alterarMolho == 1:
        for item in pedido_atual:
            if item['nome'] == "Molho":
                print(f"Removendo {item['descricao']} do pedido.")
                confirma = input("Tem certeza que deseja alterar o molho do pedido? (1 - Sim, 2 - Não): ")
                if confirma == '1':
                    pedido_atual.remove(item)
                    print("Molho removido do pedido. Agora você pode escolher um novo molho.")
                    telaPedidoMolho()
                elif confirma == '2':
                    print("Alteração do molho cancelada.")
                else:
                    print("Opção inválida. Retornando ao menu de alterações.")
                time.sleep(1.5)
        print("Não há molho no pedido para alterar.")
        time.sleep(1.5)
        qualAteração()
    elif alterarMolho == 2:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        alterarMolho()
    
def alterarPontoCarne():
    os.system("cls")
    print("=================================")
    print("-----ALTERAR PONTO DA CARNE------")
    print("=================================") 
    print("Deseja alterar o ponto da carne do pedido?")
    print("(1) - Sim")
    print("(2) - Não")
    alterarPontoCarne = int(input("Digite aqui a opcao(NUMERO): -> "))
    if alterarPontoCarne == 1:
        for item in pedido_atual:
            if item['nome'] == "Carne":
                print(f"Removendo {item['descricao']} do pedido.")
                confirma = input("Tem certeza que deseja alterar o ponto da carne do pedido? (1 - Sim, 2 - Não): ")
                if confirma == '1':
                    pedido_atual.remove(item)
                    print("Ponto da carne removido do pedido. Agora você pode escolher um novo ponto.")
                    pontosCarne()
                elif confirma == '2':
                    print("Alteração do ponto da carne cancelada.")
                else:
                    print("Opção inválida. Retornando ao menu de alterações.")
                time.sleep(1.5)
        print("Não há ponto da carne no pedido para alterar.")
        time.sleep(1.5)
        qualAteração()
    elif alterarPontoCarne == 2:
        qualAteração()
    else:
        os.system("cls")
        print("Opção inválida. Por favor, escolha uma opção válida.")
        time.sleep(2)
        alterarPontoCarne()









telaInicial()


# # else tipoLogin != 1 or tipoLogin != 2:
#     print("Numero invalido:")