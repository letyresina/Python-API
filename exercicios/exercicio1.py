'''
    Exercício 1:
    Procurar o CEP através dos dados informados do usuário (endereço)
'''

# Importações

import requests

# armazenamento de UF para facilitar para o usuário

ufExistente = {
    'RO': 'Rondônia',
    'AC': 'Acre',
    'AM': 'Amazonas',
    'RR': 'Roraima',
    'PA': 'Pará',
    'AP': 'Amapá',
    'TO': 'Tocantins',
    'MA': 'Maranhão',
    'PI': 'Piauí',
    'CE': 'Ceará',
    'RN': 'Rio Grande do Norte',
    'PB': 'Paraíba',
    'PE': 'Pernambuco',
    'AL': 'Alagoas',
    'SE': 'Sergipe',
    'BA': 'Bahia',
    'MG': 'Minas Gerais',
    'ES': 'Espirito Santo',
    'RJ': 'Rio de Janeiro',
    'SP': 'São Paulo',
    'PR': 'Paraná',
    'SC': 'Santa Catarina',
    'RS': 'Rio Grande do Sul',
    'MS': 'Mato Grosso do Sul',
    'MT': 'Mato Grosso',
    'GO': 'Goiás',
    'DF': 'Distrito Federal'
}

# Acesso à API
try:

    print("UFs existentes")
    for ufSigla, ufNome in ufExistente.items():
        print(f"{ufSigla} - {ufNome}")

    ufValida = False

    while ufValida == False:
        uf = input("Informe a sigla da sua UF: ")
        if uf in ufExistente:
            ufValida = True
        else:
            print("UF inválida. Por favor, tente novamente")

    cidade = input("Informe qual a sua cidade: ")

    logradouro = input("Informe o nome da sua rua: ")

    url = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'

    resposta = requests.get(url)

    if resposta.status_code == 200: # ou requests.codes.ok
        dicionario = resposta.json()
        #print(dicionario)
        for item in dicionario:
            print(f"O CEP do endereço solicitado é: {item['cep']}")

    elif resposta.status_code == 400: # Bad Request
        print("ERRO: Os dados inseridos são inválidos! Tente novamente")


except ConnectionError:
    print("ERRO: Não foi possível acessar à API!")

except Exception as mensagem:
    print(f"ERRO: {mensagem}")