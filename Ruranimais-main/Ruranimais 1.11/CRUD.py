from datetime import datetime, timedelta
import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
from rich import print as rprint
import os
import re
from verificacoes_cad.verificacao_email import enviar_email_con, gerar_codigo_aleatorio
from verificacoes_cad.cad_funcoes import *

# Cores Utilizadas Frequentemente
amarelo = "#EEA103"
vermelho = "#D74013"
azul = "#2B283B"
verde = "#719029"
bege = "#F8E8CF"

def cadastrar_usuario():
    rprint(f"\n[{vermelho}]=============================[/{vermelho}]")
    rprint(f":green_heart: :heart: [bold]CADASTRO DE USUÁRIO[/bold] :heart: :green_heart:")
    rprint(f"[{vermelho}]=============================[/{vermelho}]\n")

    while True:
        nome_usuario = input("Nome de usuário:")
        if len(nome_usuario) > 12: 
            rprint(f"\n❌[{vermelho}]Nome inválido. Digite um nome com no máximo 12 caracteres[/{vermelho}]")
            continue
        if len(nome_usuario) < 3:
            rprint(f"\n❌[{vermelho}]Nome inválido. Digite um nome com pelo menos 3 caracteres[/{vermelho}]")
            continue
        if " " in nome_usuario:
            rprint(f"\n❌[{vermelho}]Nome inválido. O nome não pode conter espaços[/{vermelho}]")
            continue
        if not re.fullmatch(r"[a-zA-Z0-9_]+", nome_usuario):
            rprint(f"\n❌[{vermelho}]Nome inválido. O nome só pode conter letras, números e underscores[/{vermelho}]")
            continue
        break

    while True:
        email = input("E-mail: ")
        if "@" not in email or "." not in email:
            rprint(f"\n❌[{vermelho}]E-mail inválido. Email não contém @ ou endereço válido[/{vermelho}]")
            continue
        elif email.endswith ("@ufrpe.br") == False:
            rprint(f"\n❌[{vermelho}]E-mail inválido. Digite um e-mail institucional da UFRPE[/{vermelho}]")
            continue
        else:
            codigo = gerar_codigo_aleatorio()
            expira = datetime.now() + timedelta(minutes=10)
            rprint(f"\n[{amarelo}]Enviando código para {email}... [/{amarelo}]")
            try:
                enviar_email_con(email, codigo)
            except Exception as erro:
                rprint(f"\n❌[{vermelho}]Falha ao enviar o código.[/{vermelho}]")
                print(f"Detalhe do erro: {erro}")
                return

            rprint(f"\n[{verde}]Código enviado com sucesso! Verifique sua caixa de entrada e spam.[/{verde}]")

            tentativas = 0
            while tentativas <= 3:
                codigo_digitado = input("Digite o código de verificação enviado para seu email:")
                codigo_tratado = codigo_digitado.strip().upper()
                if datetime.now() > expira:
                    rprint(f"\n❌[{vermelho}]Código expirado. Por favor, solicite um novo código.[/{vermelho}]")
                    break

                if codigo_tratado == codigo:
                    rprint(f"\n[{verde}]Email verificado com sucesso! [/{verde}]")
                    break

                tentativas += 1
                rprint(f"\n❌[{vermelho}]Código incorreto. Tentativas restantes: {3 - tentativas} [/{vermelho}]")
            else:
                rprint(f"\n❌[{vermelho}]Número máximo de tentativas atingido. Por favor, solicite um novo código.[/{vermelho}]")
                return

            break

    while True:
        cpf = input("Cpf: ")
        break

    while True:
        rprint (f"\nSenha precisa conter:\n- Pelo menos 8 caracteres\n- Uma letra maiúscula\n- Uma letra minúscula\n- Um número\n- Um caractere especial")
        senha = input("Senha: ")
        senha_valida, mensagem_senha = verificar_senha(senha)
        if not senha_valida:
            rprint(f"\n❌[{vermelho}]{mensagem_senha}[/{vermelho}]")
            continue
        confirmacao_senha = input("Confirme sua senha:")
        while confirmacao_senha != senha:
            rprint(f"\n❌[{vermelho}]As senhas não coincidem[/{vermelho}]")
            confirmacao_senha = input("Por favor, tente novamente: ")
        rprint(f"\n[{verde}]Senha criada com sucesso![/{verde}]")
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