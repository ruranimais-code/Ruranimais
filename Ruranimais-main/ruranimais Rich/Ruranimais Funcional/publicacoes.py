publicacoes = []


def criar_publicacao(usuario):

    print("\n===================================")
    print("📝 NOVA PUBLICAÇÃO")
    print("===================================")

    texto = input("Digite sua publicação: ")

    if texto == "":
        print("\n❌ A publicação não pode estar vazia.")
        return

    publicacao = {

        "autor": usuario["nome"],
        "email": usuario["email"],
        "texto": texto,
        "curtidas": [],
        "comentarios": []

    }

    publicacoes.append(publicacao)

    print("\n✅ Publicação criada!")


def listar_publicacoes():

    print("\n===================================")
    print("📰 PUBLICAÇÕES")
    print("===================================")

    if len(publicacoes) == 0:

        print("Nenhuma publicação encontrada.")

        return

    for i, publicacao in enumerate(publicacoes):

        print("\n-----------------------------------")

        print(f"ID: {i + 1}")
        print(f"Autor: {publicacao['autor']}")
        print(f"Publicação: {publicacao['texto']}")
        print(
            f"Curtidas: "
            f"{len(publicacao['curtidas'])}"
        )


def curtir_publicacao(usuario):

    listar_publicacoes()

    if len(publicacoes) == 0:
        return

    try:

        numero = int(
            input("\nDigite o ID da publicação: ")
        )

        indice = numero - 1

        publicacao = publicacoes[indice]

    except (ValueError, IndexError):

        print("\n❌ Publicação inválida.")

        return

    if usuario["email"] in publicacao["curtidas"]:

        print("\n❌ Você já curtiu essa publicação.")

    else:

        publicacao["curtidas"].append(
            usuario["email"]
        )

        print("\n❤️ Publicação curtida!")