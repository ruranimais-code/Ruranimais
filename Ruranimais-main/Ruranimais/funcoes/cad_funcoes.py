# Imports
import re
import requests
import os
from dotenv import load_dotenv

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

# Tira os caracteres nâo numéricos do cpf, tipo "." e "-"
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