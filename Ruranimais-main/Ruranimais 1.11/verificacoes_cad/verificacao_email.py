import os
import secrets
import random
import string
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Carrega o que tem dentro do .env
load_dotenv()
if not os.environ.get("SENHA_APP") or not os.environ.get("EMAIL_REMETENTE"):
    raise EnvironmentError(
        "As variáveis de ambiente EMAIL_REMETENTE e SENHA_APP não estão definidas."
    )

# Função para gerar o código que vai ser enviado
def gerar_codigo_aleatorio(tamanho=6):
    caracteres = string.ascii_uppercase + string.digits
    codigo = "".join(secrets.choice(caracteres) for _ in range(tamanho))
    return codigo

# Função que envia o email + o conteúdo dele
def enviar_email_con(email, codigo):
    mensagem = MIMEText(
        f"<p>Olá,</p>"
        f"<p>Obrigado por se cadastrar no Ruranimais!</p>"
        f"<p>Seu código de confirmação é: <strong style=\"font-size: 20px; letter-spacing: 4px;\">{codigo}</strong></p>"
        f"<p>Por favor, insira esse código (válido por 10 minutos) "
        f"na aplicação para concluir seu cadastro.</p>"
        f"<p>Atenciosamente,<br>Equipe Ruranimais</p>",
        _subtype="html",
    )

    mensagem["Subject"] = "Confirmação de Cadastro - Ruranimais"
    mensagem["From"] = os.environ.get("EMAIL_REMETENTE")
    mensagem["To"] = email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(os.environ.get("EMAIL_REMETENTE"), os.environ.get("SENHA_APP"))
        servidor.send_message(mensagem)

