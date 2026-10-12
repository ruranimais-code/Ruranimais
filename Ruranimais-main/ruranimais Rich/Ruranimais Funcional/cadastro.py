usuarios = {}
def cadastrar_usuario():

    print("\n===================================")
    print("🐾 CADASTRO DE USUÁRIO")
    print("===================================")

    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    if email in usuarios:

        print("\n❌ Este e-mail já está cadastrado!")

        return

    usuarios[email] = {

        "nome": nome,
        "email": email,
        "senha": senha

    }

    print("\n✅ Usuário cadastrado com sucesso!")


def login():

    print("\n===================================")
    print("🔐 LOGIN")
    print("===================================")

    email = input("E-mail: ")
    senha = input("Senha: ")

    if email in usuarios:

        if usuarios[email]["senha"] == senha:

            print(
                f"\n✅ Bem-vindo(a), "
                f"{usuarios[email]['nome']}!"
            )

            return usuarios[email]

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
            break

        else:

            print("\n❌ Opção inválida!")


menu_inicial()