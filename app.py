import os
#lista de dados 
restaurantes =[{'nome':'praça', 'categoria':'japonesa', 'ativo':False},
               {'nome':'pizza suprema', 'categoria':'italina', 'ativo':True},
               {'nome':'sushi', 'categoria':'coreano', 'ativo':False}]

#Funções do app
def exibir_nome_programa():
    '''Essa função é responsável por exibir o nome do restaurante'''
    print('Sabor Express\n')

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir subtitulos'''
    os.system('cls')
    linha ='*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def exibir_opcao():
    '''Essa função é responsável por exibir opções do programa'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função é responsável apresentar mensagem de finalização do programa'''
    exibir_subtitulo('finalizando o App')

def voltar_ao_menu_principal():
    '''Essa função é responsável por voltar ao inicio do programa'''
    input('Digite uma tecla para voltar ao menu principal. ')
    main()

def opcao_invalida():
    '''Essa função é responsável por Informar uma opção errada'''
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastar um novo restaurante'''
    exibir_subtitulo('Cadastro de restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    restaurantes.append(dados_do_restaurante)
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados'''
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por alterar o estado do restaurante'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsável por interagir com usuário para escolher uma opção'''
    try:
        opcao_escolhida = int(input('escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida ==  2:
            listar_restaurantes()
            
        elif opcao_escolhida ==  3:
            alternar_estado_restaurante()
        elif opcao_escolhida ==  4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é que defini o principal do programa'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcao()
    escolher_opcao()


if __name__ == '__main__':
    main()