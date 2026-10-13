# Imports
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
        "As variáveis de ambiente EMAIL_REMETENTE e SENHA_APP não estão definidas"
    )

# Função para gerar o código que vai ser enviado
def gerar_codigo_aleatorio(tamanho=6):
    caracteres = string.ascii_uppercase + string.digits
    codigo = "".join(secrets.choice(caracteres) for _ in range(tamanho))
    return codigo

# Função que envia o email pra confirmação do cadastro + o conteúdo dele
def enviar_email_con(email, codigo):
    mensagem = MIMEText(
        f"<p>Olá,"
        f"<p>Obrigado por se cadastrar no Ruranimais!</p>"
        f"<p><br><br>Seu código de confirmação é: <strong style=\"font-size: 20px; letter-spacing: 4px;\">{codigo}</strong></p>"
        f"<p><br><br>Por favor, insira esse código (válido por 10 minutos) na aplicação para concluir seu cadastro.</p>"
        f"<p>Atenciosamente,<br>Equipe Ruranimais</p>",
        _subtype="html",
    )

    mensagem["Subject"] = "Confirmação de Cadastro - Ruranimais"
    mensagem["From"] = os.environ.get("EMAIL_REMETENTE")
    mensagem["To"] = email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(os.environ.get("EMAIL_REMETENTE"), os.environ.get("SENHA_APP"))
        servidor.send_message(mensagem)

# Função que envia o email pra confirmação do log + o conteúdo dele
def enviar_email_log(email, codigo):
    mensagem = MIMEText(
        f"<p>Olá,"
        f"<p>Bem vindo de volta ao Ruranimais!</p>"
        f"<p><br><br>Seu código de confirmação é: <strong style=\"font-size: 20px; letter-spacing: 4px;\">{codigo}</strong></p>"
        f"<p><br><br>Por favor, insira esse código (válido por 10 minutos) na aplicação para concluir seu login.</p>"
        f"<p>Atenciosamente,<br>Equipe Ruranimais</p>",
        _subtype="html",
    )

    mensagem["Subject"] = "Confirmação de Login - Ruranimais"
    mensagem["From"] = os.environ.get("EMAIL_REMETENTE")
    mensagem["To"] = email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(os.environ.get("EMAIL_REMETENTE"), os.environ.get("SENHA_APP"))
        servidor.send_message(mensagem)

# Função recuperar senha
def enviar_email_senha(email, codigo):
    mensagem = MIMEText(
        f"<p>Olá,"
        f"<p>Por favor, insira este código:"
        f"<p><br><br><strong style=\"font-size: 20px; letter-spacing: 4px;\">{codigo}</strong></p>"
        f"<p><br><br>Na aplicação para recuperar sua senha.</p>"
        f"<p>Atenciosamente,<br>Equipe Ruranimais</p>",
        _subtype="html",
        )
    
    mensagem["Subject"] = "Recuperação de Senha - Ruranimais"
    mensagem["From"] = os.environ.get("EMAIL_REMETENTE")
    mensagem["To"] = email
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(os.environ.get("EMAIL_REMETENTE"), os.environ.get("SENHA_APP"))
        servidor.send_message(mensagem)