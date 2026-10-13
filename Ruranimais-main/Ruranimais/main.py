# Bibliotecas
from rich import print as rprint
from rich.console import Console
console = Console()
# Imports
import time
import os
import platform
from CRUD import *
from funcoes.besteira import mostrar_logo


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

# Mostra a logo do Ruranimais ao iniciar
mostrar_logo()
# Início do Programa - Menu Ruranimais :)
def menu_inicial():
    os.system(comando_de_limpeza)
    while True:
        rprint(f"\n[{vermelho}]===============================[/{vermelho}]")
        rprint(f":heart:  𖹭  [{verde}][bold]R U R A N I M A I S[/bold][/{verde}] 𖹭 :heart:")
        rprint(f"[{vermelho}]===============================\n[/{vermelho}]")
        rprint(f"[{verde}][bold]Digite o comando destacado ou o número associado para prosseguir.[/bold][/{verde}]")
        rprint(f"1 - [{amarelo}]Cadastrar[/{amarelo}] usuário\n"
               f"2 - [{amarelo}]Login[/{amarelo}] de usuário\n"
               f"3 - [{amarelo}]Checar[/{amarelo}] Dados\n"
               f"4 - [{amarelo}]Atualizar[/{amarelo}] Dados\n"
               f"5 - [{amarelo}]Sair[/{amarelo}] do programa\n"
               f"\n[{amarelo}][bold]Escolha uma opção: [/bold][/{amarelo}]\n"
               )

        opcao = input("")

        if opcao.lower() == "cadastro" or opcao == "1":
            os.system(comando_de_limpeza)
            cadastrar_usuario()
            print("Após o cadastro, é necessário realizar o login para acessar o sistema.")

        elif opcao.lower() == "login" or opcao == "2":
            lista_dados_usuario = login()
            if lista_dados_usuario is not None:
                confirmacao_log.append("1")
            else:
                confirmacao_log.clear()

        elif opcao.lower() == "checar" or opcao == "3":
            if len(confirmacao_log) == 0:
                os.system(comando_de_limpeza)
                print("\nVocê não está logado. Faça o login primeiro.")
                time.sleep(2)
            else:
                ordem_dados = ["ID: ", "Nome: ", "Email: ", "CPF: "]
                dados_visiveis = (
                    lista_dados_usuario[0],
                    lista_dados_usuario[1],
                    lista_dados_usuario[2],
                    lista_dados_usuario[4],
                )
                for a, b in zip(ordem_dados, dados_visiveis):
                    print(a)
                    print(b)

                    
        elif opcao.lower() == "atualizar" or opcao == "4":
            if len(confirmacao_log) == 0:
                os.system(comando_de_limpeza)
                print("\nVocê não está logado. Faça o login primeiro.")
                time.sleep(2)
            else:
                os.system(comando_de_limpeza)
                if atualizar_dados(lista_dados_usuario):
                    confirmacao_log.clear()
                    lista_dados_usuario = None
            

        elif opcao.lower() == "sair" or opcao == "5":
            os.system(comando_de_limpeza)
            rprint("\n\n\n[#eea103][bold]Até logo![/bold][/#eea103]\n\n\n")
            exit()
        
        else:
            os.system(comando_de_limpeza)
            rprint(
                   f"[{vermelho}]=====================[/{vermelho}]\n\n"
                   f"[bold][{vermelho}]Opção inválida! Tente novamente :)[/{vermelho}][/bold]\n\n"
                   f"[{vermelho}]=====================[/{vermelho}]\n\n"
                  )
            time.sleep(3)
            os.system(comando_de_limpeza)

menu_inicial()