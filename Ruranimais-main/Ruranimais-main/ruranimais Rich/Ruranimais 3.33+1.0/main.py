import time
from rich import print
from rich.console import Console
console = Console()
from cadastro import cadastrar_usuario

import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

def menu_inicial():

    while True:

        print("\n===================================")
        print("🐾 [green1]RURANIMAIS[/green1] :green_heart:")
        print("A rede social de quem cuida.")
        print("===================================\n")
        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("3 - Sair")

        opcao_inicial_menu = input("\nEscolha uma opção: ")

        if opcao_inicial_menu == "1":
            print("\nProsseguindo para o Cadastro de usuário.")
            cadastrar_usuario()
        
        elif opcao_inicial_menu == "2":
            print("")

        elif opcao_inicial_menu == "3":
            print("Fechando programa...")
            time.sleep(1)
            print("[white]...[/white]")
            print("[blue][strong]Você encerrou sua sessão no Ruranimais.[/strong][/blue]")
            exit()

        else:
            print("\nOpção inválida!")

menu_inicial()