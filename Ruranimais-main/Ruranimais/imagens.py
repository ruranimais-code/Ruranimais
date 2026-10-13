from rich import print as rprint
import os
import time
from PIL import Image

avatar = Image.open("C:\\Users\\Ryan\\Desktop\\testesry\\Ruranimais 1.11\\imagens_repositorio\\png balhaçad.png")
#exibir imagem
# cuzy.show()

avatar_rgb = avatar.convert("RGB")
avatar_rgb.save("C:\\Users\\Ryan\\Desktop\\testesry\\Ruranimais 1.11\\imagens_repositorio\\png balhaçad.jpg")

# MEIO QUE NADA AQUI AINDA  
# def enviar_imagem():
#     while True:
#         print("\n===================================")
#         print("🖼️ ENVIO DE IMAGEM")
#         print("===================================")

#         imagem = input("Digite o nome ou caminho da imagem: ")
#         if imagem.strip() == "":
#             print("\nImagem inválida.\n")


#         print("\nImagem enviada com sucesso!")