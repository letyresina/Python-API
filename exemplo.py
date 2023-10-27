# Para acessar api's, precisamos instalar o requests -> pip install requests
# Para reconhecer o código, em aula, como tem dois pythons instalados, pode utilizar py -3.11 -m pip install requests

import requests

try:

    cep = input("Informe o CEP (SOMENTE NÚMEROS!): ")
    url = f'https://viacep.com.br/ws/{cep}/json/'

    resposta = requests.get(url)

    if resposta.status_code == 200: # ou requests.codes.ok
        dicionario = resposta.json()
        print(f"Rua: {dicionario['logradouro']}")
        print(f"Complemento: {dicionario['complemento']}")
        print(f"Cidade: {dicionario['localidade']}")
        print(f"Estado: {dicionario['uf']}")

    elif resposta.status_code == 400: # Bad Request
        print("ERRO: O CEP deve ter 8 caracteres")

except ConnectionError:
    print("ERRO: Não foi possível acessar à API!")

except Exception as mensagem:
    print(f"ERRO: {mensagem}")