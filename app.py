import os
#lista de dados 
restaurantes =['pizza','tomate','bolo','laranja','caramelo']

#Funções do app
def exibir_nome_programa():
    print('Sabor Express\n')
def exibir_opcao():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')
def finalizar_app():
    os.system('cls')
    print('finalizando o App\n')
def opcao_invalida():
    print('Opção invalida!\n')
    input('Digite uma tecla para voltar ao menu principal.')
    main()
def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('Digite uma tecla para voltar ao menu principal.')
    main()
def listar_restaurantes():
    os.system('cls')
    print('Listando restaurantes\n')
    for restaurante in restaurantes:
        print(f'{restaurante}')

    input('\nDigite uma tecla para voltar ao menu principal.')
    main()
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