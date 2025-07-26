import json

def mostrar_menu_principal():
    try:
        # Mostrando menu principal
        print('SEJA BEM-VINDO AO MENU INICIAL')
        print('1_ Estudantes')
        print('2_ Professores')
        print('3_ Disciplinas')
        print('4_ Turmas')
        print('5_ Matriculas')
        print('0_ Sair')
        # Pegando opção do usuario
        opcao = int(input('Infome uma ação que deseja: '))
        if opcao in [0, 1, 2, 3, 4, 5]:
            return opcao
        else:
            print('Erro: Opção inválida! Escolha uma das opções listadas.')
    except ValueError:
            print('Erro: Entrada inválida! Informe um número.')


def mostrar_menu_secundario():
    try:
        print(f'MENU DE OPERAÇÕES ***** [{opcao_string}] *****')
        print('1_ Listar')
        print('2_ criar')
        print('3_ Atualizar')
        print('4_ Excluir')
        print('5_ Voltar ao menu anterior')
        opcao_secundaria = int(input('Informe uma ação que deseja: '))
        if opcao_secundaria in [1, 2, 3, 4, 5]:
            return opcao_secundaria
        else:
            print('Erro: Opção inválida! Escolha uma das opções listadas.')
    except ValueError:
            print('Erro: Entrada inválida! Informe um número.')


def processos_menu_secundario(arq):
        while True:
            #Mostrando menu secundário      
            opcao_secundaria = mostrar_menu_secundario()
            if opcao_secundaria == 1:
                mostrar_dados(arq)
            elif opcao_secundaria == 2:
                print('==========[Inclusão]==========')
                cadastrar_dados(arq)     
            elif opcao_secundaria == 3:
                print(f'*****EDITAR {opcao_string}*****')
                codigo_para_editar = input(f"Informe o codigo que deseja para editar: ")
                atualizar_dados(codigo_para_editar, arq)       
            elif opcao_secundaria == 4:
                print(f'*****REMOVER {opcao_string}*****')
                codigo_para_excluir = input("Informe o codigo que deseja para excluir: ")
                excluir_dados(codigo_para_excluir, arq)    
            elif opcao_secundaria == 5:
                break


def vericar_codigo_existe(codigo, nome_arquivo):    
    lista_variada = ler_arquivo(nome_arquivo)
    chave_codigo = pegar_codigo(nome_arquivo)
    for item in lista_variada:
        if item[chave_codigo] == codigo:
            return True
    return False


def pegar_codigo(nome_arquivo):
    if nome_arquivo == estudantes_arquivo:
        chave_codigo = "codigo_estudante"
    elif nome_arquivo == professores_arquivo:
        chave_codigo = "codigo_professor"
    elif nome_arquivo == disciplinas_arquivo:
        chave_codigo = "codigo_disciplina"
    elif nome_arquivo == turmas_arquivo:
        chave_codigo = "codigo_turma"
    elif nome_arquivo == matriculas_arquivo:
        chave_codigo = "codigo_turma"
    return chave_codigo


def salvar_arquivo(data, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(data, arquivo, ensure_ascii=False)


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            data_arquivo = json.load(arquivo)
            return data_arquivo
    except:
        return []
    

def mostrar_dados(nome_arquivo):
    lista_variada = ler_arquivo(nome_arquivo)
    print('==========[Listagem]==========')
    if len(lista_variada) == 0:
        print('Ninguém cadastrado!')
    else:
        for data in lista_variada:
            print(f'Dados: {data}')


def cadastrar_dados(nome_arquivo):
    lista_variada = ler_arquivo(nome_arquivo)
    dados = {}
    try:
        # Cria um dicionário com os dados do novo estudante
        if nome_arquivo == estudantes_arquivo:
            codigo = int(input("Informe o codigo do estudante: "))
            nome = input('Informe o nome do estudante: ')
            cpf = input("Informe o cpf do estudante: ")
            dados = {
                "codigo_estudante": codigo,
                "nome_estudante": nome,
                "cpf_estudante": cpf
            }
        elif nome_arquivo == professores_arquivo:
            codigo = int(input("Informe o codigo do professor: "))
            nome = input('Informe o nome do professor: ')
            cpf = input("Informe o cpf do professor: ")
            dados = {
                "codigo_professor": codigo,
                "nome_professor": nome,
                "cpf_professor": cpf
            }
        elif nome_arquivo == disciplinas_arquivo:
            codigo = int(input("Informe o codigo da disciplina: "))
            nome = input('Informe o nome da disciplina: ')
            dados = {
                "codigo_disciplina": codigo,
                "nome_disciplina": nome,
            }
        elif nome_arquivo == turmas_arquivo:
            codigo = int(input("Informe o codigo da turma: "))
            codigo_professor = int(input('Informe o codigo do professor: '))
            codigo_disciplina = int(input('Informe o codigo da disciplina: '))
            dados = {
                "codigo_turma": codigo,
                "codigo_professor": codigo_professor,
                "codigo_disciplina": codigo_disciplina
            }
        elif nome_arquivo == matriculas_arquivo:
            codigo = int(input("Informe o codigo da turma: "))
            codigo_estudante = int(input('Informe o codigo do estudante: '))
            dados = {
                "codigo_turma": codigo,
                "codigo_estudante": codigo_estudante,
            }
        if vericar_codigo_existe(codigo, nome_arquivo):
            print(f"Erro: O código {codigo} já está cadastrado.")
            return
        else:
            lista_variada.append(dados)
            salvar_arquivo(lista_variada, nome_arquivo)
            print(f'Incluido com sucesso.')
    except ValueError:
        print("Erro: entrada invalida! Certifique-se de inserir números corretamente.")
        return -1


def atualizar_dados(codigo_para_editar, nome_arquivo):
    lista_variada = ler_arquivo(nome_arquivo)
    try:
        chave_codigo = pegar_codigo(nome_arquivo)
        codigo_para_editar = int(codigo_para_editar)
        
        # Verifica se o estudante foi encontrado
        for data in lista_variada:
            if data[chave_codigo] == codigo_para_editar:
                novo_codigo = int(input(f"Informe o novo codigo para {opcao_string}: "))
                
                # Verifica se o novo código já existe
                if novo_codigo != codigo_para_editar and vericar_codigo_existe(novo_codigo, nome_arquivo):
                    print(f"Erro: O código {novo_codigo} já está cadastrado.")
                    return  # Retorna se o código já existir
                
                # Atualiza os dados de acordo com o tipo de arquivo
                if nome_arquivo == estudantes_arquivo:
                    data['nome_estudante'] = input('Informe o nome do estudante atualizado: ')
                    data['cpf_estudante'] = input("Informe o cpf do estudante atualizado: ")
                    data['codigo_estudante'] = novo_codigo  # Atualiza o código do estudante
                
                elif nome_arquivo == professores_arquivo:
                    data['nome_professor'] = input('Informe o nome do professor atualizado: ')
                    data['cpf_professor'] = input("Informe o cpf do professor atualizado: ")
                    data['codigo_professor'] = novo_codigo  # Atualiza o código do professor
                
                elif nome_arquivo == disciplinas_arquivo:
                    data['nome_disciplina'] = input('Informe o nome da disciplina atualizado: ')
                    data['codigo_disciplina'] = novo_codigo
                
                elif nome_arquivo == turmas_arquivo:
                    data['codigo_professor'] = int(input('Informe o codigo do professor atualizado: '))
                    data['codigo_disciplina'] = int(input('Informe o codigo da disciplina atualizado: '))
                    data['codigo_turma'] = novo_codigo
                
                elif nome_arquivo == matriculas_arquivo:
                    data['codigo_turma'] = novo_codigo  # Atualiza o código da turma
                    data['codigo_estudante'] = int(input('Informe o codigo do estudante atualizado: '))
                    data['codigo_turma'] = novo_codigo
                
                salvar_arquivo(lista_variada, nome_arquivo)  # Salva as alterações
                print(f"{opcao_string} editado com sucesso!")  # Mensagem de sucesso
                return
        
        print('Código não encontrado!')  # Mensagem caso o código não exista
    except ValueError:
        print("Erro: Código inválido! Certifique-se de inserir números corretamente.")


def excluir_dados(codigo_para_excluir, nome_arquivo):
    lista_variada = ler_arquivo(nome_arquivo)
    dados_para_remover = None
    try:
        chave_codigo = pegar_codigo(nome_arquivo)
        codigo_para_excluir = int(codigo_para_excluir)
        # Percorre a lista para verificar se há um codigo igual a digitada pelo usúario
        for data in lista_variada:
            if data[chave_codigo] == codigo_para_excluir:
                dados_para_remover = data
                break
        if dados_para_remover is not None:
            lista_variada.remove(dados_para_remover)
            salvar_arquivo(lista_variada, nome_arquivo)
            print("Removido com sucesso!")
        else:
            print("Codigo informado não encontrado!")
    except ValueError:
         print("Erro: Código inválido! Certifique-se de inserir números corretamente.")
    

estudantes_arquivo = 'estudantes.json'
professores_arquivo = 'professores.json'
disciplinas_arquivo = 'disciplinas.json'
turmas_arquivo = 'turmas.json'
matriculas_arquivo = 'matriculas.json'


while True:
    # Mostrando menu principal
    opcao = mostrar_menu_principal()
    opcao_string = ''
    match opcao:
        case 1:
            opcao_string = 'ESTUDANTES'
        case 2:
            opcao_string = 'PROFESSORES'
        case 3:
            opcao_string = 'DISCIPLINAS'
        case 4:
            opcao_string = 'TURMAS'
        case 5:
            opcao_string = 'MATRICULAS'
        case 0:
            opcao_string = 'SAIR' 
    if opcao == 1:
       processos_menu_secundario(estudantes_arquivo)
    elif opcao == 2:
        processos_menu_secundario(professores_arquivo)
    elif opcao == 3:
        processos_menu_secundario(disciplinas_arquivo)
    elif opcao == 4:
        processos_menu_secundario(turmas_arquivo)
    elif opcao == 5:
        processos_menu_secundario(matriculas_arquivo)
    # Se o usuário escolher a opção de sair do sistema
    elif opcao == 0:
        print('Você pediu para sair.')
        break





