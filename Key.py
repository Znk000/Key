import time
import random
import string

banner = "\033[1;31m" + """
_  __
| |/ /___ _   _
| ' // _ \ | | |
| . \  __/ |_| |  _
|_|\_\___|\__, | (_)
          |___/
""" + "\033[1;33m"
print(banner)
print("\033[1;33m~By Vini Dev~\n\033[0m")

print("\033[1;31mOpções:\033[0m")

opcao = "\033[1;33m[1] Gerar senha\033[0m"
print(opcao)

escolha = input("\033[1;33mEscolha uma Opção:\033[0m ")

if escolha == "1":
    tamanho_senha = 12

    def gerar_senha(tamanho):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        return senha

    senha_gerada = gerar_senha(tamanho_senha)
    print("\033[1;31mSenha gerada:\033[0m", senha_gerada)
else:
    print("\033[1;31mNão tem essa opção, burro\033[0m")
