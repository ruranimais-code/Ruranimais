# Bibliotecas / Imports
from rich import print as rprint
from CRUD import *
import time
import os
import platform
from rich.console import Console
console = Console()

# Criação e Conexão do Banco de Dados - SQlite
import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
# Preciso achar um jeito de usar o atributo UNIQUE sem que o programa bugue por completo.
cursor.execute(''' CREATE TABLE IF NOT EXISTS usuarios_ruranimais (
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               nome_usuario TEXT NOT NULL,
               email TEXT NOT NULL,
               senha TEXT NOT NULL,
               cpf TEXT NOT NULL)
''')
conexao.commit()

#Identificação de Sistema + Limpeza Inicial do Terminal
if platform.system() == "Linux" or platform.system() == "Darwin":
    comando_de_limpeza = "clear"
if platform.system() == "Windows":
    comando_de_limpeza = "cls"
os.system(comando_de_limpeza)

# Cores Utilizadas Frequentemente
amarelo = "#EEA103"
vermelho = "#D74013"
azul = "#2B283B"
verde = "#719029"
bege = "#F8E8CF"

confirmacao_log = []

# Início do Programa - Menu Ruranimais :)
def menu_inicial():
    while True:
        rprint(f"\n[{vermelho}]=====================[/{vermelho}]")
        rprint(f":green_heart: :heart: [#719029][bold]RURANIMAIS[/bold][/#719029] :heart: :green_heart:")
        rprint(f"[{vermelho}]=====================\n[/{vermelho}]")
        rprint(f"[{verde}][bold]Digite o comando destacado ou o número associado para prosseguir.[/bold][/{verde}]")
        rprint(f"1 - [{amarelo}]Cadastrar[/{amarelo}] usuário\n"
               f"2 - [{amarelo}]Login[/{amarelo}] de usuário\n"
               f"3 - [{amarelo}]Checar[/{amarelo}] Dados\n"
               f"4 - [{amarelo}]Atualizar[/{amarelo}] Dados\n"
               f"5 - [{amarelo}]Sair[/{amarelo}] do programa\n"
               f"\n[{amarelo}][bold]Escolha uma opção: [/bold][/{amarelo}]\n"
               )

        opcao = input("")

        if opcao.lower == "cadastro" or opcao == "1":
            os.system(comando_de_limpeza)
            cadastrar_usuario()
            print("Após o cadastro, é necessário realizar o login para acessar o sistema.")

        elif opcao.lower == "login" or opcao == "2":
            lista_dados_usuario = login()
            confirmacao_log.append("1")

        elif opcao.lower() == "checar" or opcao == "3":
            if len(confirmacao_log) == 0:
                os.system(comando_de_limpeza)
                print("\nVocê não está logado. Faça o login primeiro.")
                time.sleep(2)
            else:
                ordem_dados = ["ID: ", "Nome: ", "Email: ", "Senha: ", "CPF: "]
                for a, b in zip(ordem_dados, lista_dados_usuario):
                    print(a)
                    print(b)

                    
        elif opcao == "4":
            print("indisponível no momento, foi mal :p")
            time.sleep(3)
            #terminar isso aqui depois

        elif opcao.lower() == "sair" or opcao == "5":
            os.system(comando_de_limpeza)
            rprint("\n\n\n[#eea103][bold]Até logo![/bold][/#eea103]\n\n\n")
            exit()
        
        else:
            os.system(comando_de_limpeza)
            rprint(
                   "[#d74013]=====================[/#d74013]\n\n"
                   "[bold][#d74013]Opção inválida! Tente novamente :)[/#d74013][/bold]\n\n"
                   "[#d74013]=====================[/#d74013]\n\n"
                  )
            time.sleep(3)
            os.system(comando_de_limpeza)

menu_inicial()