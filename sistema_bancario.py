from datetime import datetime, date
import re

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[c] Criar conta corrente
[a] Acessar conta corrente
[l] Lista de usuários
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contador = 1
usuarios = []

def funcao_deposito(saldo, valor, extrato, /): 

    if valor > 0:
        saldo += valor 
        extrato += f"Depósito: R$ {valor:.2f}\n" 
        print(f"{extrato}Saldo: {saldo:.2f}\n\nDepósito feito com sucesso!") 

    else:
        print("Operação falhou! O valor informado é inválido.") 

    return saldo, extrato 

def funcao_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"{extrato}Saldo: {saldo:.2f}\n\nSaque feito com sucesso! Você tem {LIMITE_SAQUES - numero_saques} saques restantes hoje.")

        else:
            print("Operação falhou! O valor informado é inválido.")
        
        return saldo, extrato, numero_saques

def funcao_extrato(saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def funcao_formata_cpf(cpf):
    return re.sub(r'\D', '', cpf)

def funcao_cpf_existe(cpf):
    global usuarios
    cpf_limpo = funcao_formata_cpf(cpf)
    for usuario in usuarios:
        if funcao_formata_cpf(usuario['cpf']) == cpf_limpo:
            return True
    return False

def funcao_novo_usuario(cpf, nome, data_de_nascimento, logradouro, numero, bairro, cidade, estado, /):    
    global usuarios
    cpf_limpo = re.sub(r'\D', '', cpf)

    if not cpf:
        print("Campo CPF não preenchido. Por favor, preencha com um valor válido.")
    if not nome:
        print("Campo Nome não preenchido. Por favor, preencha com um valor válido.")
    if not data_de_nascimento:
        print("Campo Data de Nascimento não preenchido. Por favor, preencha com um valor válido.")
    if not logradouro:
        print("Campo Logradouro não preenchido. Por favor, preencha com um valor válido.")
    if not numero:
        print("Campo Número não preenchido. Por favor, preencha com um valor válido.")
    if not bairro:
        print("Campo Bairro não preenchido. Por favor, preencha com um valor válido.")
    if not cidade:
        print("Campo Cidade não preenchido. Por favor, preencha com um valor válido.")
    if not estado:
        print("Campo Estado não preenchido. Por favor, preencha com um valor válido.")

    endereco = {"logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade, "estado": estado }
    novo_usuario = { "cpf": cpf_limpo , "nome": nome, "data_de_nascimento": data_de_nascimento, "endereco": endereco}
    
    if funcao_cpf_existe(cpf):
        print("CPF já cadastrado.")
        return "Erro: CPF já cadastrado."    
    usuarios.append(novo_usuario)

    print("Cadastro feito com sucesso!")

    return usuarios

def funcao_cria_conta_corrente(cpf):
    global usuarios
    global contador

    cpf_limpo = funcao_formata_cpf(cpf) 
    conta_corrente = {"agencia" : "0001", "conta_corrente" : contador }

    for usuario in usuarios: 
        if funcao_formata_cpf(usuario['cpf']) == cpf_limpo:  

            if 'contas_correntes' not in usuario: 
                usuario['contas_correntes'] = [] 
            
            contador += 1 
            conta_corrente["conta_corrente"] = str(contador) 
            
            usuario['contas_correntes'].append(conta_corrente) 
            print("Conta criada com sucesso!") 
            
            return contador 
        
        else:
            print("CPF informado não tem uma conta de usuário. Por favor, cadastre-se com a opção Novo usuário.")
 
def funcao_acessar_conta(agencia, conta_corrente, cpf, /):
    global usuarios
    cpf_limpo = funcao_formata_cpf(cpf)

    for usuario in usuarios:
        if funcao_formata_cpf(usuario['cpf']) == cpf_limpo:
            for conta in usuario['contas_correntes']:
                if conta['agencia'] == agencia and conta['conta_corrente'] == conta_corrente:
                    print(f"CPF: {usuario['cpf']}\nAgência: {conta['agencia']}\nConta corrente: {conta['conta_corrente']}\nAcesso à conta autorizado.")
                    return True
            print("Agência ou conta-corrente incorretos.")
            return False
        print("CPF não vinculado a esta conta.")
        return False

while True:

    opcao = input(menu) 

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = funcao_deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = funcao_saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        funcao_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print("\n\nObrigado por usar nossos serviços.\n\n")
        break

    elif opcao == "u":

        cpf = str(input("Informe seu CPF: "))
        nome = str(input("Informe seu nome completo: ")).title()
        data_de_nascimento = str(input("Informe sua data de nascimento (DD/MM/AAAA): "))
        logradouro = str(input("Informe seu logradouro: ")).title()
        numero = str(input("Informe o número do logradouro: "))
        bairro = str(input("Informe o bairro: ")).title()
        cidade = str(input("Informe a cidade: ")).title()
        estado = str(input("Informe o estado: ")).title()

        funcao_novo_usuario(cpf, nome, data_de_nascimento, logradouro, numero, bairro, cidade, estado)

    elif opcao == "c":
        cpf = str(input("Informe seu CPF: "))
        funcao_cria_conta_corrente(cpf)

    elif opcao == "a":
        agencia = str(input("Informe o número de sua agência: "))
        conta_corrente = str(input("Informe o número de sua conta corrente: "))
        cpf = str(input("Informe seu CPF: "))

        funcao_acessar_conta(agencia, conta_corrente, cpf)

    elif opcao == "l":
        print(usuarios)  

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")