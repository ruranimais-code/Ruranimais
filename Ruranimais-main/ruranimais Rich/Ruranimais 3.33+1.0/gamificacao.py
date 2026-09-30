def adicionar_pontos(usuario, pontos):

    if "pontos" not in usuario:

        usuario["pontos"] = 0

    usuario["pontos"] += pontos

    verificar_achievements(usuario)


def verificar_achievements(usuario):

    if "achievements" not in usuario:

        usuario["achievements"] = []

    if "colecao" not in usuario:

        usuario["colecao"] = []

    pontos = usuario["pontos"]

    if (
        pontos >= 10
        and
        "Primeiros Passos"
        not in usuario["achievements"]
    ):

        usuario["achievements"].append(
            "Primeiros Passos"
        )

        usuario["colecao"].append(
            "🏆 Medalha: Primeiros Passos"
        )

        print(
            "\n🏆 ACHIEVEMENT DESBLOQUEADO!"
        )


    if (
        pontos >= 30
        and
        "Amigo dos Animais"
        not in usuario["achievements"]
    ):

        usuario["achievements"].append(
            "Amigo dos Animais"
        )

        usuario["colecao"].append(
            "🐾 Medalha: Amigo dos Animais"
        )

        print(
            "\n🏆 ACHIEVEMENT DESBLOQUEADO!"
        )


    if (
        pontos >= 50
        and
        "Protetor Ruranimais"
        not in usuario["achievements"]
    ):

        usuario["achievements"].append(
            "Protetor Ruranimais"
        )

        usuario["colecao"].append(
            "🌟 Medalha: Protetor Ruranimais"
        )

        print(
            "\n🏆 ACHIEVEMENT DESBLOQUEADO!"
        )


def visualizar_gamificacao(usuario):

    print("\n===================================")
    print("🏆 GAMIFICAÇÃO")
    print("===================================")

    print(
        f"Pontuação: "
        f"{usuario.get('pontos', 0)}"
    )

    print("\nAchievements:")

    if usuario.get("achievements"):

        for achievement in usuario[
            "achievements"
        ]:

            print(
                f"🏆 {achievement}"
            )

    else:

        print(
            "Nenhum achievement desbloqueado."
        )

    print("\nColeção:")

    if usuario.get("colecao"):

        for item in usuario["colecao"]:

            print(
                f"- {item}"
            )

    else:

        print("Coleção vazia.")