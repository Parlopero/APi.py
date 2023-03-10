import requests
import json



def consulta_cnpj(cnpj):

     url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
     querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"}
     response = requests.request('GET', url, params=querystring)

     resp = json.loads(response.text)

     print(resp['nome'] ,resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro'])

     return resp['nome'] ,resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro']


print('####################')
print('### Consulta CEP ###')
print('####################')
print()

cnpj = input('Digite o CNPJ para a consulta: ')


if len(cnpj) != 14:
		print('Quantidade de dígitos inválida!')
		exit()


print('==> CEP ENCONTRADO <==')
consulta_cnpj(''+cnpj+'')

print('---------------------------------')
option = int(input('Deseja realizar uma nova consulta ?\n 1. Sim\n 2. Sair\n'))
