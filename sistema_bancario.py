menu = """

[d] Despositar na Conta
[s] Saque da Conta
[e] Extrato Bancário
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    escolha = input(menu)

    if escolha == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
        else:
            print("Operação inválida: o valor informado está incorreto.")
    
    elif escolha == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação inválida: Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação inválida: O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação inválida: Excedeu o limite de saques.")
        else:
            print("Operação inválida: Valor informado é inválido.")
    elif escolha == "e":
        print("\n ============== Extrato Bancário ==============")
        print("Não houve movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==================================================")
    elif escolha == "q":
        break
    else:
        print("Operação inválida: por favor, selecione novamente a operação desejada.")
