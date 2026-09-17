def enviar_imagem(usuario):

    print("\n===================================")
    print("🖼️ ENVIO DE IMAGEM")
    print("===================================")

    imagem = input(
        "Digite o nome ou caminho da imagem: "
    )

    if imagem == "":

        print("\n❌ Imagem inválida.")

        return

    if "imagens" not in usuario:

        usuario["imagens"] = []

    usuario["imagens"].append(imagem)

    print("\n✅ Imagem enviada com sucesso!")


def visualizar_imagens(usuario):

    print("\n===================================")
    print("🖼️ MINHAS IMAGENS")
    print("===================================")

    if "imagens" not in usuario:

        print("Nenhuma imagem encontrada.")

        return

    if len(usuario["imagens"]) == 0:

        print("Nenhuma imagem encontrada.")

        return

    for i, imagem in enumerate(
        usuario["imagens"]
    ):

        print(
            f"{i + 1} - {imagem}"
        )