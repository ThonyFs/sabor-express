import os
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
def escolher_opcao():
    opcao_escolhida = int(input('escolha uma opção: '))

    if opcao_escolhida == 1:
        print('cadastrar restaurante')
    elif opcao_escolhida ==  2:
        print('Listar restaurante')
        
    elif opcao_escolhida ==  3:
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome_programa()
    exibir_opcao()
    escolher_opcao()


if __name__ == '__main__':
    main()