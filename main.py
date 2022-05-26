#Consumindo uma API com Python
import requests 

def apresentacao():
	print("===================")
	print("===CUNSULTA CEP ===")
	print("===================")

	cep = input("Digite o CEP: ")

	if len(cep) != 8:
		print("Quantidade de Dígitos Inválido!")
		print()
		apresentacao()
#Criando requsição
	r = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))

	endereco = r.json()
	if 'erro' not in endereco:
		print("CEP Encontrado:")
		print()
		print("CEP: {}".format(endereco["cep"]))
		print("Logradouro: {}".format(endereco["logradouro"]))
		print("Complemento: {}".format(endereco["complemento"]))
		print("Bairro: {}".format(endereco["bairro"]))
		print("Cidade: {}".format(endereco["localidade"]))
		print("Estado: {}".format(endereco["uf"]))
		print()
		apresentacao()
	else:
		print("CEP Inválido!")
		print()
		apresentacao()

apresentacao()
