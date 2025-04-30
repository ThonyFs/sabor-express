import os

num = int(input('Insira um numero: '))

if num % 2 == 0:
    os.system('cls')
    print(f'{num} é um numero par!')
else:
    os.system('cls')
    print(f'{num} é um numro impar!')

end = input('aperte qualquer tecla para seguir para o proximo exercicio.')
os.system('cls')

def classifica_idade(idade):
    if idade >= 0 and idade <= 12:
        os.system('cls')
        print(f"Com {idade} você é uma criança.")
    elif idade > 12 and idade <= 18:
        os.system('cls')
        print(f'Com {idade} você é um adolescente.')
    else:
        os.system('cls')
        print(f'Com {idade} você é um adulto.')

idade = int(input('Informe sua idade: '))
classifica_idade(idade)

end = input('aperte qualquer tecla para finalizar o programa.')
os.system('cls')

