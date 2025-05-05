import os
#lista de dados 
restaurantes =['pizza','tomate','bolo','laranja','caramelo']

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
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes:
        print(f'{restaurante}')
    voltar_ao_menu_principal()
def escolher_opcao():
    try:
        opcao_escolhida = int(input('escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida ==  2:
            listar_restaurantes()
            
        elif opcao_escolhida ==  3:
            print('Ativar restaurante')
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