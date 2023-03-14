import requests
import json


def consulta_cnpj(cnpj) -> object:
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
    querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"}
    response = requests.request('GET', url,params=querystring)

    resp = json.loads(response.text)

    print(resp['nome'], resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro']), resp['municipio'], \
        resp['uf'], resp['cep'], resp['telefone'], resp['email']

    return resp['nome'], resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro'], resp['municipio'], \
        resp['uf'], resp['cep'], resp['telefone'], resp['email']

print('####################')
print('### Consulta CNPJ ###')
print('####################')
print()

cnpj = input('Digite o CNPJ para a consulta: ')

string = "" + cnpj + ""
characters = ".-/"

string = ''.join(x for x in string if x not in characters)

if len(string) != 14:
    print('Quantidade de dígitos inválida!')
    exit()
try:
    print('==> CNPJ ENCONTRADO <==')
    consulta_cnpj('' +string+ '')
except:
  print('{}: CNPJ inválido.'.format(cnpj))
print('---------------------------------')
print('Essas são as informações encontradas no seu cnpj!')

print('---------------------------------')
print('saindo...')
