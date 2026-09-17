mensagens = []


def enviar_mensagem(usuario, usuarios):

    print("\n===================================")
    print("💬 ENVIAR MENSAGEM")
    print("===================================")

    print("\nUsuários disponíveis:")

    for email, dados in usuarios.items():

        if email != usuario["email"]:

            print(
                f"- {dados['nome']} "
                f"({email})"
            )

    destinatario = input(
        "\nE-mail do destinatário: "
    )

    if destinatario not in usuarios:

        print("\n❌ Usuário não encontrado.")

        return

    texto = input("Mensagem: ")

    if texto == "":

        print("\n❌ Mensagem vazia.")

        return

    mensagens.append({

        "remetente": usuario["email"],
        "destinatario": destinatario,
        "texto": texto

    })

    print("\n✅ Mensagem enviada!")


def visualizar_mensagens(usuario):

    print("\n===================================")
    print("💬 MINHAS MENSAGENS")
    print("===================================")

    encontrou = False

    for mensagem in mensagens:

        if (
            mensagem["destinatario"]
            == usuario["email"]
            or
            mensagem["remetente"]
            == usuario["email"]
        ):

            encontrou = True

            print("\n-----------------------------------")

            print(
                f"De: "
                f"{mensagem['remetente']}"
            )

            print(
                f"Para: "
                f"{mensagem['destinatario']}"
            )

            print(
                f"Mensagem: "
                f"{mensagem['texto']}"
            )

    if not encontrou:

        print(
            "Nenhuma mensagem encontrada."
        )