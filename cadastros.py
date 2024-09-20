import csv

cadastros = []

def salvar_csv(nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=['nome', 'idade', 'email'])
        writer.writeheader()
        writer.writerows(cadastros)
    print('Cadastros salvos com sucesso!')

def carregar_csv(nome_arquivo):
    global cadastros
    cadastros = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            reader = csv.DictReader(arquivo)
            for linha in reader:
                cadastros.append(linha)
        print('Cadastros carregados com sucesso!')
    except FileNotFoundError:
        print('Arquivo não encontrado. Nenhum cadastro carregado.')

def menu():
    while True:
        print('Menu de Operações: ')
        print('1 - Cadastrar')
        print('2 - Listar')
        print('3 - Consultar')
        print('4 - Excluir')
        print('5 - Salvar em CSV')
        print('6 - Carregar de CSV')
        print('7 - Sair')

        escolha = int(input('O que deseja fazer: '))

        if escolha == 1:
            nome = input('Digite o seu nome: ')
            idade = input('Digite a sua idade: ')
            email = input('Digite o seu email: ')
            cadastros.append({'nome': nome, 'idade': idade, 'email': email})
            print(f'O cadastro de {nome} foi realizado com sucesso!')
        
        elif escolha == 2:
            print('Lista de cadastros:')
            for i, cadastro in enumerate(cadastros, 1):
                print(f'{i}. Nome: {cadastro["nome"]}, Idade: {cadastro["idade"]}, Email: {cadastro["email"]}')
        
        elif escolha == 3:
            consulta = input('Digite um nome para consultar: ')
            encontrado = False
            for cadastro in cadastros:
                if cadastro['nome'] == consulta:
                    print(f'Nome: {cadastro["nome"]}, Idade: {cadastro["idade"]}, Email: {cadastro["email"]}')
                    encontrado = True

            if not encontrado:
                print(f'{consulta} não encontrada!')
        
        elif escolha == 4:
            excluir = input('Digite o nome para excluir: ')
            encontrado = False
            for cadastro in cadastros:
                if cadastro['nome'] == excluir:
                    cadastros.remove(cadastro)
                    print('Cadastro excluído com sucesso!')
                    encontrado = True
                    break
            if not encontrado:
                print('Cadastro não encontrado.')
        
        elif escolha == 5:
            nome_arquivo = input('Digite o nome do arquivo para salvar (e.g., cadastros.csv): ')
            salvar_csv(nome_arquivo)
        
        elif escolha == 6:
            nome_arquivo = input('Digite o nome do arquivo para carregar (e.g., cadastros.csv): ')
            carregar_csv(nome_arquivo)
        
        elif escolha == 7:
            print('Programa finalizado.')
            break
        
        else:
            print('Digite uma opção válida.')

menu()