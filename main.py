import requests
import PySimpleGUI as sg

#Criando o tema
sg.theme("DarkTeal12")
def index():	
	layout = [
		[sg.Text("Digite um CEP: ", font=" Helvetica 20")],
		[sg.Input(key = '-CEP-', size=20, font=" Any 16")],
		[sg.Button("Consultar", font="16"), sg.Button("Nova Consulta", font="16"), sg.Button("Sair", font="16")],
		[sg.Text("")],
		[sg.Text("Logradouro     ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT1-")],
		[sg.Text("")],
		[sg.Text("Complemento", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT2-")],
		[sg.Text("")],
		[sg.Text("Bairro             ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT3-")],
		[sg.Text("")],
		[sg.Text("Cidade           ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT4-")],
		[sg.Text("")],
		[sg.Text("Estado            ", font="16"), sg.Input(size=(50), font=" Any 16", key="-OUT5-")]
	
]
	window = sg.Window('Sistema de Consultar CEP', layout, size=(500,600), element_justification='center'  )

	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Sair':
			break
		elif event == 'Consultar':
			cep = values['-CEP-']
			r = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
			endereco = r.json()
			window['-OUT1-'].update(endereco["logradouro"])
			window['-OUT2-'].update(endereco["complemento"])
			window['-OUT3-'].update(endereco["bairro"])
			window['-OUT4-'].update(endereco["localidade"])
			window['-OUT5-'].update(endereco["uf"])
		elif event == "Nova Consulta":
			window['-CEP-'].update("")
			window['-OUT1-'].update("")
			window['-OUT2-'].update("")
			window['-OUT3-'].update("")
			window['-OUT4-'].update("")
			window['-OUT5-'].update("")
index()
