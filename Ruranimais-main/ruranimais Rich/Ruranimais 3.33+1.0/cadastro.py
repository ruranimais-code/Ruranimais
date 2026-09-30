usuarios = {}
import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

def cadastrar_usuario():
    cursor.execute("""CREATE TABLE IF NOT EXISTS contas_ruranimais (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL UNIQUE
                    )""")


    print("\n===================================")
    print("🐾 CADASTRO DE USUÁRIO")
    print("===================================")

    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    cursor.execute("""INSERT INTO contas_ruranimais
                   (nome, email, senha)VALUES
                   (?,?,?)""", (nome, email, senha))
    cursor.execute("""SELECT * FROM contas_ruranimais""")
    
    contas = cursor.fetchall()
    print(contas)
    for conta in contas:
           id, nome, email, senha = conta
           print(f"id:{id}")
           print(f"nome:{nome}")
           print(f"email:{email}")
           print(f"senha:{senha}")
    conexao.commit()
    print("\n✅ Usuário cadastrado com sucesso!")


def login():

    print("\n===================================")
    print("🔐 LOGIN")
    print("===================================")

    email = input("E-mail: ")
    senha = input("Senha: ")

    cursor.execute(
        "SELECT nome, email, senha FROM contas_ruranimais WHERE email = ? AND senha = ?",
        (email, senha)
    )
    usuario = cursor.fetchone()

    if usuario:
        nome, _, _ = usuario
        print(f"\n✅ Bem-vindo(a), {nome}!")
        return {"nome": nome, "email": email, "senha": senha}

    print("\n❌ E-mail ou senha incorretos.")
    return None


def menu_inicial():

    while True:

        print("\n===================================")
        print("🐾 RURANIMAIS")
        print("===================================")

        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            cadastrar_usuario()

        elif opcao == "2":

            login()

        elif opcao == "3":

            print("\n👋 Até logo!")
            exit()

        else:

            print("\n❌ Opção inválida!")
menu_inicial()