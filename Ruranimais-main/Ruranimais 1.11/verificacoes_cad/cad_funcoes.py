import re
import requests
import os
from dotenv import load_dotenv

# Confirmar se a senha é válida
def verificar_senha(senha):
    if len(senha) < 8:
        return False, "Senha inválida. A senha deve ter pelo menos 8 caracteres."
    elif not re.search(r"[A-Z]", senha):
        return False, "Senha inválida. A senha deve conter pelo menos uma letra maiúscula."
    elif not re.search(r"[a-z]", senha):
        return False, "Senha inválida. A senha deve conter pelo menos uma letra minúscula."
    elif not re.search(r"\d", senha):
        return False, "Senha inválida. A senha deve conter pelo menos um número."
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False, "Senha inválida. A senha deve conter pelo menos um caractere especial."
    else:
        return True, "Senha válida."


# Confirmar se cpf existe
load_dotenv()
if not os.environ.get("headers"):
    raise EnvironmentError(
        "As variáveis de ambiente headers não estão definidas."
    )
res = requests.get(
    "https://api.cpfhub.io/cpf/12345678909",
    headers=os.environ.get("headers"),
    timeout=30,
)

def limpar_cpf(cpf):
    return re.sub(r'\D', '', cpf)
    #remove pontos e traços



