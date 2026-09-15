import time
import sqlite3
from rich import print
from rich.console import Console
console = Console()
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

#ctrl + ;
def cadastro():
    cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                saldo FLOAT NOT NULL,
                cpf TEXT NOT NULL UNIQUE
                )""")

    meunome = input("Oi oi oi oi, fala algo, tipo, seu nome sei lá porra: ")
    meusaldo = int(input("Me fala um número: "))
    meucpf = input("Me diz teu cpf pfv: ")

    cursor.execute("""INSERT INTO contas_bancarias
               (nome, sald mudar nome do banco de dados e as categorias de dados dentro dele tbm
# do, cpf) VALUES
               (?,?,?)""", (meunome, meusaldo, meucpf))
    cursor.execute("""SELECT * FROM contas_bancarias""")

    contas = cursor.fetchall()
    print(contas)
    for conta in contas:
       id, nome, saldo, cpf = conta
       print(f"id:{id}")
       print(f"nome:{nome}")
       print(f"saldo:{saldo}")
       print(f"cpf:{cpf}")
    conexao.commit()

menu_pre_perfil= True
menu_pos_perfil = False
while menu_pre_perfil == True:
    opcao_menu = console.input(f"\n[green]Menu Bonitinho Dos Ruranimais[/green]\n1 - Cadastro\n2 - Login\n3 - Ajuda\n4 - Sair\n")
    if opcao_menu == "1":
        print("Direcionando ao cadastro...")
        cadastro()
        menu_pre_perfil = False
        menu_pos_perfil = True
    elif opcao_menu == "2":
        print("placeholder")
    elif opcao_menu == "3":
        print("Tabela de Ajuda")
    elif opcao_menu == "4":
        print("Fechando programa...")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2..")
        time.sleep(1)
        print("1.")
        time.sleep(1)
        print("[blue]Você encerrou sua sessão no Ruranimais.[/blue]")
        exit()
    else:
        print("Opção inválida, tente novamente")
        opcao_menu = console.input(f"[green]Menu Bonitinho Dos Ruranimais[/green]\n1 - Cadastro\n2 - Login\n3 - Ajuda\n4 - Sair\n")

while menu_pos_perfil == True:
    opcao_menu = console.input(f"[green]Menu Bonitinho Dos Ruranimais[/green]\n1 - Visualizar Perfil\n2 - Ver Publicações\n3 - Ver Enquetes\n")




# É interessante, pois dá um senso de continuidade, pode ser um menu inicial apenas de cadastro e login e ajuda
# é, faria sentido, aí iria pro MENU principal de verdade
# checar o que fazer quando o input for um caractere especial
# e se o input for na verdade uma linha de código?
#escobrir como se deleta os dados de um .db
# int não é float porra