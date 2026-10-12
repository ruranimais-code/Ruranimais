import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
from rich import print as rprint
import os

# Cores Utilizadas Frequentemente
amarelo = "#EEA103"
vermelho = "#D74013"
azul = "#2B283B"
verde = "#719029"
bege = "#F8E8CF"

def cadastrar_usuario():
    rprint(f"\n[{vermelho}]=============================[/{vermelho}]")
    rprint(f":green_heart: :heart:[bold]CADASTRO DE USUÁRIO[/bold]:heart: :green_heart:")
    rprint(f"[{vermelho}]=============================[/{vermelho}]\n")

    while True:
        nome_usuario = input("Digite seu nome de usuário: ")
        if len(nome_usuario) > 12:
            rprint("[#d74013]Nome inválido. Digite um nome com no máximo 12 caracteres.[/#d74013]")
        elif len(nome_usuario) < 3:
            rprint("[#d74013]Nome inválido. Digite um nome com pelo menos 3 caracteres.[/#d74013]")
        else:
            break
    while True:
        email = input("E-mail: ")
        if "@" not in email or "." not in email:
            rprint("[#d74013]E-mail inválido. Email não contém @ ou endereço válido.[/#d74013]")
        elif email.endswith ("@ufrpe.br") == False:
            rprint("[#d74013]E-mail inválido. Digite um e-mail institucional da UFRPE.[/#d74013]")
        else:
            break
    while True:
        senha = input("Senha: ")
        break
    while True:
        cpf = input("blablabla")
        break
    cursor.execute('''INSERT INTO usuarios_ruranimais (nome_usuario, email, senha, cpf) VALUES (?, ?, ?, ?)''', (nome_usuario, email, senha, cpf))
    conexao.commit()

    rprint(f"\n[{verde}]Usuário cadastrado com sucesso![/{verde}]")

def login():
#faltam tratamentos de erro obviamente
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    cpf = input("Digite seu CPF: ")
    cursor.execute('''SELECT * FROM usuarios_ruranimais WHERE email = ? AND cpf = ? AND senha = ?''', (email, cpf, senha))
    dados_usuario = cursor.fetchone()
    os.system('cls')
    print(f"ID: {dados_usuario[0]}\nNome: {dados_usuario[1]}\nEmail: {dados_usuario[2]}\nSenha:{dados_usuario[3]}\nCPF: {dados_usuario[4]}")
    confirmacao = input("Esses são os seus dados? Se sim, digite 1, se não digite 2:")
    lista_dados_usuario = dados_usuario
    if confirmacao == "1":
        print("Login realizado com sucesso!")
        return lista_dados_usuario
    elif confirmacao == "2":
        print("Login não realizado, tente novamente.")
    else:
        print("Opção inválida, tente novamente.")





# def login():
#     os.system("clear")
#     rprint("\n[#d74013]================[/#d74013]")
#     rprint(":green_heart: :heart: [#719029][bold]LOGIN[/bold][/#719029] :heart: :green_heart:")
#     rprint("[#d74013]================[/#d74013]")

#     email = input("E-mail: ")
#     senha = input("Senha: ")

#     cursor.execute(
#         "SELECT nome, email, senha FROM contas_ruranimais WHERE email = ? AND senha = ?",
#         (email, senha)
#     )
#     usuario = cursor.fetchone()

#     if usuario:
#         nome, _, _ = usuario
#         print(f"\nBem-vindo(a), {nome}!")
#         return {"nome": nome, "email": email, "senha": senha}

#     print("\n❌ E-mail ou senha incorretos.")
#     return None

# def checar_dados():

# def atualizar_dados():