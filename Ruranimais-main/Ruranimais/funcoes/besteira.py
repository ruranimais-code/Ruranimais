import time
from pathlib import Path


def mostrar_logo(caminho_logo=None):
    arquivo_logo = (
        Path(caminho_logo)
        if caminho_logo is not None
        else Path(__file__).with_name("ruranimaislogo.txt")
    )
    with arquivo_logo.open("r", encoding="utf-8") as f:
        logo= f.read()
    print(logo)
    time.sleep(4)