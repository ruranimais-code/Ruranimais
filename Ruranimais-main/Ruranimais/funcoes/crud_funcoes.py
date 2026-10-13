# Imports
from funcoes.verificacao_email import gerar_codigo_aleatorio, enviar_email_senha
from dotenv import load_dotenv
from smtplib import SMTPException
from datetime import datetime, timedelta
from rich import print as rprint
import re
import requests
import time
import os
import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

amarelo = "#EEA103"
vermelho = "#D74013"
azul = "#2B283B"
verde = "#719029"
bege = "#F8E8CF"

#CAD
# Confirmar se a senha é válida
def verificar_senha(senha):
    if len(senha) < 8:
        return False, "Senha inválida. A senha deve ter pelo menos 8 caracteres"
    elif not re.search(r"[A-Z]", senha):
        return False, "Senha inválida. A senha deve conter pelo menos uma letra maiúscula"
    elif not re.search(r"[a-z]", senha):
        return False, "Senha inválida. A senha deve conter pelo menos uma letra minúscula"
    elif not re.search(r"\d", senha):
        return False, "Senha inválida. A senha deve conter pelo menos um número"
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False, "Senha inválida. A senha deve conter pelo menos um caractere especial"
    else:
        return True, "Senha válida"

# Carrega o que tem dentro do .env
load_dotenv()
if not os.environ.get("API_KEY_CPF"):
    raise EnvironmentError(
        "A variável de ambiente API_KEY_CPF não está definida"
    )

# Tira os caracteres nâo numéricos do cpf
def limpar_cpf(cpf):
    return re.sub(r'\D', '', cpf)

# Verifica se o cpf tem 11 >números<
def validar_cpf(cpf):
    cpf = limpar_cpf(cpf)
    if len(cpf) != 11 or not cpf.isascii() or not cpf.isdigit():
        return False, "CPF deve conter 11 dígitos numéricos"
    # Verifica se todos os digitos são iguais
    if cpf == cpf[0] * 11:
        return False, "Formato inválido"
    else:
        return True, "Formato válido!"

# Verifica se cpf existe mesmo
def verificar_cpf(cpf):
    cpf_valido, mensagem_cpf = validar_cpf(cpf)
    if not cpf_valido:
        return False, mensagem_cpf

    cpf = limpar_cpf(cpf)
    url = f"https://api.cpfhub.io/cpf/{cpf}"
    headers = {
        "x-api-key": os.environ.get("API_KEY_CPF"),
        "Accept": "application/json"
    }

    # Vários tratamentos de acordo com resposta da api
    try:
        resposta = requests.get(url, headers=headers, timeout=30)
        if resposta.status_code == 200:
            data = resposta.json()
            if not isinstance(data, dict) or not isinstance(data.get("success"), bool):
                return False, "API retornou resposta inválida."
            if data["success"]:
                return True, "CPF válido"
            else:
                return False, "CPF inválido"
        elif resposta.status_code == 404:
            return False, "CPF não encontrado"
        return False, f"Erro na API: HTTP {resposta.status_code}."
    except requests.exceptions.RequestException as erro:
        return False, f"Erro de conexão: {erro}"
    except ValueError as erro:
        return False, f"API retornou JSON inválido: {erro}"

#LOG
# Função pra verificar o codigo do email pra facilitar minha vida
def verificar_codigo_email(email, enviar_email, finalidade):
    codigo = gerar_codigo_aleatorio()
    expira = datetime.now() + timedelta(minutes=10)

    rprint(f"\n[{amarelo}]Enviando código para {email}... [/{amarelo}]")
    try:
        enviar_email(email, codigo)
    except (OSError, SMTPException) as erro:
        rprint(f"\n❌[{vermelho}]Falha ao enviar o código[/{vermelho}]")
        print(f"Erro: {erro}")
        return False

    rprint(
        f"\n[{verde}]Código enviado com sucesso!"
        f"Verifique sua caixa de entrada e spam[/{verde}]"
    )
    for tentativa in range(1, 4):
        codigo_digitado = input(
            "Digite o código de verificação enviado para seu email: "
        ).strip().upper()
        if datetime.now() > expira:
            rprint(
                f"\n❌[{vermelho}]Código expirado"
                f"Solicite um novo código[/{vermelho}]"
            )
            return False
        if codigo_digitado == codigo:
            rprint(f"\n[{verde}]{finalidade} verificado com sucesso![/{verde}]")
            return True

        rprint(f"\n❌[{vermelho}]Código incorreto\nTentativas restantes: {3 - tentativa}[/{vermelho}]")

    rprint(f"\n❌[{vermelho}]Número máximo de tentativas atingido\nSolicite um novo código[/{vermelho}]")
    return False

# Cria nova senha
def recuperar_senha(dados_usuario):
    cpf_digitado = input("Digite seu CPF para confirmar sua identidade: ").strip()
    if limpar_cpf(cpf_digitado) != limpar_cpf(dados_usuario[4]):
        rprint(f"\n❌[{vermelho}]CPF incorreto[/{vermelho}]\nVoltando para o menu...")
        time.sleep(2)
        return None

    if not verificar_codigo_email(dados_usuario[2], enviar_email_senha, "Recuperação de senha"):
        return None

    while True:
        rprint (f"\nSenha precisa conter:\n- Pelo menos 8 caracteres\n- Uma letra maiúscula\n- Uma letra minúscula\n- Um número\n- Um caractere especial")
        nova_senha = input("Digite sua nova senha: ").strip()
        senha_valida, mensagem = verificar_senha(nova_senha)
        if not senha_valida:
            rprint(f"\n❌[{vermelho}]{mensagem}[/{vermelho}]")
            continue

        confirmacao = input("Confirme sua nova senha: ").strip()
        if confirmacao != nova_senha:
            rprint(f"\n❌[{vermelho}]As senhas não coincidem[/{vermelho}]")
            continue
        break

    cursor.execute(
        "UPDATE usuarios_ruranimais SET senha = ? WHERE id = ?",
        (nova_senha, dados_usuario[0]),
    )
    conexao.commit()
    rprint(f"\n[{verde}]Senha redefinida com sucesso![/{verde}]")
    cursor.execute(
        "SELECT * FROM usuarios_ruranimais WHERE id = ?",
        (dados_usuario[0],),
    )
    return cursor.fetchone()

# Pra não poder usar dados que já foram cadastrados
def _campo_duplicado(nome_usuario=None, email=None, cpf=None):
    cursor.execute(
        "SELECT nome_usuario, email, cpf FROM usuarios_ruranimais"
    )
    for nome_cadastrado, email_cadastrado, cpf_cadastrado in cursor.fetchall():
        if nome_usuario is not None and nome_usuario == nome_cadastrado:
            return "Nome de usuário"
        if email is not None and email.casefold() == email_cadastrado.casefold():
            return "E-mail"
        if cpf is not None and limpar_cpf(cpf) == limpar_cpf(cpf_cadastrado):
            return "CPF"
    return None

# ATUALIZAR
# Por enquanto só tem pra deletar conta
def deletar_usuario(email, nome_usuario, cpf, senha):
    rprint(f"\n[{vermelho}]Deseja deletar sua conta?[/{vermelho}]")
    deseja_deletar = input(
        f"OBS.: Essa ação não pode ser desfeita!\n(s/n): "
    ).strip().lower()
    if deseja_deletar != "s":
        print("Até a próxima :(")
        return None

    # Pede informações usadas no login pra confirmar que usuário quer deletar conta
    email_digitado = input("Informe seu email para confirmar: ").strip()
    senha_digitada = input("Informe sua senha para confirmar: ").strip()
    if email_digitado != email or senha_digitada != senha:
        rprint(f"\n❌[{vermelho}]Email e/ou senha incorretos[/{vermelho}]\n\nNão foi possível deletar conta.")
        time.sleep(1)
        return None

   # Vai atrás de deletar as informações do usuário
    cursor.execute(
        """SELECT id FROM usuarios_ruranimais
           WHERE email = ? AND nome_usuario = ? AND cpf = ? AND senha = ?""",
        (email, nome_usuario, cpf, senha),
    )
    usuario = cursor.fetchone()
    if usuario is None:
        rprint(f"\n❌[{vermelho}]Não foi possível encontrar a conta[/{vermelho}]")
        return None

    cursor.execute(
        "DELETE FROM usuarios_ruranimais WHERE id = ?",
        (usuario[0],),
    )
    conexao.commit()
    rprint("\nConta deletada com sucesso...\nFoi um prazer ter você conosco!")
    return True
        