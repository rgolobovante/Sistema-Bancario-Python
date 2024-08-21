saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 3

    
menu = '''
    1 - Despositar
    2 - Sacar
    3 - Extrato
    0 - Sair
'''

while True:
    print("Escolha uma das opçoes abaixo:") 
    opcao = int(input(menu))

    if opcao == 1:
            print(f'Seu saldo é de: R${saldo:.2f}')
            print(f'Deseja depositar? s(sim) ou n(nao):')
            resposta_depositar = input()

            if resposta_depositar == 's':
                print(f'Digite o valor do deposito:')
                deposito = float(input())
                if deposito > 0:
                    saldo += deposito
                    print(f'Voce depositou R${deposito:.2f}, seu saldo atual é: R${saldo:.2f}')
                    extrato += (f'Deposito: R${deposito:.2f}\n')
                else:
                    print("Não é permitido depositar valores negativos!")
            

    elif opcao == 2:
            print(f'Quanto deseja sacar?')
            valor_sacado = float(input())
            saldo_excedido = valor_sacado > saldo
            limite_excedido = valor_sacado > limite
            limite_saque_excedido = numero_saques > LIMITE_SAQUE 

            if saldo_excedido or limite_excedido or limite_saque_excedido:
                print('Saldo insuficiente ou limite de saque diário atingido!')
            else:
            
                saldo -= valor_sacado
                limite -= valor_sacado
                numero_saques+= 1
                print(f'Seu saque foi de R${valor_sacado:.2f}, saldo restante: R${saldo:.2f}')
                print(f'Total numero de saques diarios disponiveis (3), atual ({numero_saques})')
                print(f'Total Limite diario disponivel: {limite}')
                extrato += (f'Saque: R${valor_sacado:.2f}\n')

    elif opcao == 3:
         print("############ EXTRATO ############")
         print(extrato)

    elif opcao == 0:
         break
    else:
         print("Operação invalida, insira uma opçao da lista")
         
         

