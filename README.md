# Domain-Checker

Domain Checker 🔍

Este script Python realiza uma análise automática de domínios, verificando a disponibilidade de resposta HTTP/HTTPS por meio de requisições GET e POST. Além disso, o script trata erros de conexão e fornece um resumo detalhado dos códigos de status HTTP.

Funcionalidades

Entrada de Arquivo: Aceita um arquivo de domínios como argumento, tornando a análise de listas de domínios mais prática.
Tratamento de Erros: Identifica e trata erros de conexão e timeout, fornecendo mensagens claras.
Análise de Respostas HTTP: Registra e exibe a quantidade de respostas agrupadas por código de status.

Como Usar

Pré-requisitos: Instale a biblioteca requests:

pip install requests

Execução: Passe o arquivo de domínios como argumento ao rodar o script. Exemplo:

python url.py -d lista_de_dominios.txt
