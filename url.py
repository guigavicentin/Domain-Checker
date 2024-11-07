import requests
import argparse
from collections import defaultdict
import random

# Banners aleatórios para exibir no início
banners = [
    "===== Domínio Checker =====",
    "### Analisador de Domínios ###",
    "--- Verificação de Domínios ---",

"""
@@@@@%+..........................................................................+%@@@@@@
@@@@#-...............................:-=+*##*+==:.................................-#@@@@@
@@%=................................+@@@@@@@@@@@@#..................................+%@@@
@#:................................-%@@@@@@@@@@@@@=..................................-#@@
*..................................%@@@@@@@@@@@@@@%....................................#@
..................................=%@@@@@@@@@@@@@@@+....................................#
..........................:-==+**+=---=+*#%%#*+=---=+**+==--.............................
...........................:=*#%@@@@@%%#*+=-+*#%@@@@@@@%*=-..............................
................................-+%@@@@@@@@@@@@@@@@%+-:..................................
..................................:%@@@@@@@@@@@@@@@-.....................................
...................................=@@@@@@@@@@@@@@*......................................
....................................*@@@@@@@@@@@@%.......................................
:-=++=-..............................+%@@@@@@@@%+:...............................-=++=-:.
@@@@@@@%*-.............................-+%@@%*-...............................-*%@@@@@@@#
.......=@@*...............................==................................:#@@@:....%@@
..@@@..=@@@+........................:-...-@@*...--:.........................*@@@@*+:..%@@
..@@@..=@@@#..................:-+*%@@@*...*%...+@@@%#+=-....................%@@@@@@-..%@@
..@@@..=@@@*..............=*#%@@@@@@@@@=..+%..:%@@@@@@@@@%#*=:..............*@@@@@@-..%@@
.......=@@#..............*@@@@@@@@@@@@@%:.#@-.%@@@@@@@@@@@@@@%:.............:%@@@@@-..%@@
%%%%%%%%#=..............*@@@@@@@@@@@@@@@#:%@+#@@@@@@@@@@@@@@@@%:..............=#@@@%%%@@%
-=+**+=:...............=@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@*................:=+**+=-.
....:-................:%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.................-......
.+-.:%+..............:%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=..............=%+.:+:..
.#@%#%@%-............#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-...........:#@@#%@@:..
.+%@@@@@@#+=-:......*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.......-=+*%@@@@@%*...
...:=#%@@@@@@@@%#*+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+*##%@@@@@@@@%+-.....
.......=@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@*:........
.......-@@@@@@@@@@@@@@@@@%+.-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.=%@@@@@@@@@@@@@@@@@+.........
........:-+*#%@@@@@@@@@@%-...%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%..:*@@@@@@@@@@%%*+=-.........:
..............:-=+*#%%@+.....#@@@@@@@@@@@@@@@@@@@@@@@@@@@@*....=%@%#*+=-:..............:%
%-....................:......+%%%%%%%%%%%%%%%%%%%%%%%%%%%%=...........................-%@
@%+..................................................................................*%@@
"""

]
print(random.choice(banners))

# Parser para aceitar argumentos de linha de comando
parser = argparse.ArgumentParser(description="Verificador de domínios HTTP/HTTPS.")
parser.add_argument("-d", "--dominios", required=True, help="Arquivo contendo a lista de domínios")
args = parser.parse_args()

# Dicionários para armazenar contagens e URLs por status
status_count = defaultdict(int)
status_urls = defaultdict(list)

# Função para garantir que a URL tenha esquema HTTPS
def formatar_url(url):
    if not url.startswith(('http://', 'https://')):
        return 'https://' + url
    return url

# Função para realizar as requisições
def testar_dominio(url):
    try:
        # Formata a URL para garantir que tenha https:// no início
        url_formatada = formatar_url(url)

        # Envia uma requisição GET
        response_get = requests.get(url_formatada, timeout=5)
        status_count[response_get.status_code] += 1
        status_urls[response_get.status_code].append(f"{url_formatada} (GET)")

        # Envia uma requisição POST
        response_post = requests.post(url_formatada, timeout=5)
        status_count[response_post.status_code] += 1
        status_urls[response_post.status_code].append(f"{url_formatada} (POST)")

    except requests.exceptions.ConnectTimeout:
        print(f"Erro: Conexão com {url} expirou. Tempo limite atingido.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")

# Lê os domínios do arquivo especificado na linha de comando
try:
    with open(args.dominios, 'r') as file:
        dominios = [line.strip() for line in file if line.strip()]

    # Executa o teste em cada domínio
    for dominio in dominios:
        testar_dominio(dominio)

    # Exibe o resultado
    print("\nResultados por código de status:")
    for status, count in status_count.items():
        print(f"Código {status}: {count} ocorrências")
        print("URLs:")
        for url in status_urls[status]:
            print(f" - {url}")
        print()  # linha em branco para separar os status

except FileNotFoundError:
    print(f"Erro: Arquivo '{args.dominios}' não encontrado.")
