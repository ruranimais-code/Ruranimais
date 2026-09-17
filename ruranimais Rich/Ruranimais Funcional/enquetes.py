enquetes = []


def criar_enquete(usuario):

    print("\n===================================")
    print("📊 CRIAR ENQUETE")
    print("===================================")

    pergunta = input("Pergunta: ")

    opcao1 = input("Opção 1: ")
    opcao2 = input("Opção 2: ")

    enquete = {

        "autor": usuario["nome"],
        "pergunta": pergunta,

        "opcoes": {

            opcao1: 0,
            opcao2: 0

        }

    }

    enquetes.append(enquete)

    print("\n✅ Enquete criada!")


def listar_enquetes():

    print("\n===================================")
    print("📊 ENQUETES")
    print("===================================")

    if len(enquetes) == 0:

        print("Nenhuma enquete encontrada.")

        return

    for i, enquete in enumerate(enquetes):

        print("\n-----------------------------------")

        print(f"ID: {i + 1}")
        print(f"Autor: {enquete['autor']}")
        print(
            f"Pergunta: "
            f"{enquete['pergunta']}"
        )

        for opcao, votos in enquete[
            "opcoes"
        ].items():

            print(
                f"- {opcao}: "
                f"{votos} voto(s)"
            )


def votar_enquete():

    listar_enquetes()

    if len(enquetes) == 0:
        return

    try:

        numero = int(
            input(
                "\nDigite o ID da enquete: "
            )
        )

        enquete = enquetes[numero - 1]

    except (ValueError, IndexError):

        print("\n❌ Enquete inválida.")

        return

    opcoes = list(
        enquete["opcoes"].keys()
    )

    for i, opcao in enumerate(opcoes):

        print(
            f"{i + 1} - {opcao}"
        )

    try:

        escolha = int(
            input("\nEscolha uma opção: ")
        )

        opcao_escolhida = opcoes[
            escolha - 1
        ]

    except (ValueError, IndexError):

        print("\n❌ Opção inválida.")

        return

    enquete["opcoes"][
        opcao_escolhida
    ] += 1

    print("\n✅ Voto registrado!")