def cadastrar_colaborador(id):
	global lista_colaboradores
	global id_global
	print('*'*70)
	print('-'*21, 'MENU CADASTRAR COLABORADOR', '-'*21)
	print('id do colaborador: {}'.format(id))
	nome = input('Por favor informe o nome do colaborador ou colaboradora: ')
	setor = input('Por favor informe o setor do colaborador ou colaboradora: ')
	pagamento = input('Por favor informe o pagamento do colaborador ou colaboradora: ')
	colaborador = {'id': id_global, 'nome': nome, 'setor': setor, 'salário': pagamento} #formando o dicionário
	return lista_colaboradores.append(colaborador) #formando a lista de dicionários.
# fim da função cadastrar colaborador

# função consultar colaborador:
def consultar_colaborador():
	while True:
		global lista_colaboradores
		print('*'*70)
		print('-'*21, 'MENU CONSULTAR COLABORADOR', '-'*21)
		opcao = int(input('\nEscolha o número da opção desejada:\n1-Consultar todos os colaboradores\n2-Consultar colaborador por id\n3-Consultar colaboradores por setor\n4-Retornar ao menu principal\n'))
		if opcao == 4:
			break
		elif opcao == 1: #printar todos os colaboradores
			if len(lista_colaboradores) > 0: #verifica se a lista tem pelo menos um item. Se não tiver, cai no else falando que a lista está vazia.
				for colaborador in lista_colaboradores:
					print('id: {}\nnome: {}\nsetor: {}\nsalário: {}\n'.format(colaborador.get('id'), colaborador.get('nome'), colaborador.get('setor'), colaborador.get('salário')))
				break
			else:
				print ('Não há colaboradores cadastrados. Lista vazia.')
		elif opcao == 2: #printar apenas o colaborador do id específico
			try:
				id = int(input('Qual o id do colaborador que deseja consultar? '))
				if not any(colaborador['id'] == id for colaborador in lista_colaboradores): #verifica se existe aquele id na lista
					print('Id não encontrado, tente novamente.')
				else:
					for colaborador in lista_colaboradores:
						if id == colaborador['id']:
							print('\nid: {}\nnome: {}\nsetor: {}\nsalário: {}\n'.format(colaborador.get('id'), colaborador.get('nome'), colaborador.get('setor'), colaborador.get('salário')))
						break
			except ValueError: #erro caso o usuário digite algo que não seja um número
				print ('\nDigite apenas números\n')
		elif opcao == 3: #printar todos os colaboradores daquele setor
			setor = input('Qual o setor que deseja consultar? ')
			if not any(colaborador['setor'] == setor for colaborador in lista_colaboradores):#verifica se o setor existe dentro da lista
				print('Setor não cadastrado, tente novamente.')
			else:
				for colaborador in lista_colaboradores:
					if setor.lower() == colaborador['setor'].lower():
						print('\nid: {}\nnome: {}\nsetor: {}\nsalário: {}\n'.format(colaborador.get('id'), colaborador.get('nome'), colaborador.get('setor'), colaborador.get('salário')))
# fim da função consultar colaborador

# função remover colaborador:
def remover_colaborador():
	global lista_colaboradores
	print('*'*70)
	print('-'*21, 'MENU REMOVER COLABORADOR', '-'*21)
	remover = int(input('Digite o id do colaborador a ser removido: '))
	if not any(colaborador['id'] == remover for colaborador in lista_colaboradores): #veirifica se o id existe 
		print('Id não encontrado, tente novamente.')
	else:
		for colaborador in lista_colaboradores:
			if remover == colaborador['id']:
				confirma = input('\nColaborador:\nid: {}\nnome: {}\nsetor: {}\nsalário: {}\nTem certeza que deseja excluir? [S/N] '.format(colaborador.get('id'), colaborador.get('nome'), colaborador.get('setor'), colaborador.get('salário'))) #imprime o colaborador com o id correspondente na tela e pede uma confirmação antes de excluir.
				if confirma.lower() == 's':
					lista_colaboradores.remove(colaborador)
				else:
					break
# fim da função remover colaborador


# programa principal
lista_colaboradores = [] #lista de dicionários com os colaboradores 
id_global = 0 

print('Controle de Colaboradores') #exigência print com o meu nome
while True:
	try:
		print('\n'+'*'*70)
		print('-'*27, 'MENU PRINCIPAL', '-'*27)
		opcao = int(input('\nEscolha o número da opção desejada:\n1-Cadastrar colaborador\n2-Consultar colaborador(es)\n3-Remover colaborador\n4-Sair\n'))
		if opcao == 4:
			break 
		elif opcao == 1:
			id_global += 1
			cadastrar_colaborador(id_global)
			continue
		elif opcao == 2:
			consultar_colaborador()
			continue
		elif opcao == 3:
			remover_colaborador()
			continue
		else:
			print('Você digitou uma opção inválida.')
			continue
	except ValueError:
		print('Digite apenas números por favor.')
		continue