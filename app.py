import os
#lista de dados 
restaurantes =[{'nome':'praça', 'categoria':'japonesa', 'ativo':False},
               {'nome':'pizza suprema', 'categoria':'italina', 'ativo':True},
               {'nome':'sushi', 'categoria':'coreano', 'ativo':False}]

#Funções do app
def exibir_nome_programa():
    print('Sabor Express\n')
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
def exibir_opcao():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')
def finalizar_app():
    exibir_subtitulo('finalizando o App')
def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal. ')
    main()
def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu_principal()
def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    restaurantes.append(dados_do_restaurante)
    voltar_ao_menu_principal()
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria_restaurante} | {ativo_restaurante}')
    voltar_ao_menu_principal()
def alternar_estado_restaurante():
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
    os.system('cls')
    exibir_nome_programa()
    exibir_opcao()
    escolher_opcao()


if __name__ == '__main__':
    main()