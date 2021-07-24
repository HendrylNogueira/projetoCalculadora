#A ideia é criar uma calculadora que faça de tudo um pouco
#\033[31m
from math import sqrt

cont = 0
total = 0
print('')

print(f'\033[33m{"":=^60}\033[m')
print('\033[33m{:^73}'.format(" \033[31mBem vindo a empresa de softwares \033[m \033[33m"))
print('\033[31m{:^60}'.format('H.N.Q BLACK'))
print(f'\033[33m{"":=^60}\033[m')

print('')

print('''Esse é um programa que faz calculos.
[ 1 ] Soma          \033[32m(ativado)\033[m
[ 2 ] Subtração     \033[32m(ativado)\033[m
[ 3 ] Multiplicação \033[32m(ativado)\033[m
[ 4 ] Divisão       \033[31m(desativado por enquanto)\033[m
[ 5 ] Potência      \033[32m(ativado)\033[m
[ 6 ] Raiz Quadrada \033[32m(ativado)\033[m

\033[31m[ 0 ] Sair\033[m''')

tipo_de_calculo = int(input('Digite o que deseja: '))
if tipo_de_calculo == 0:
    print('')
    #print('\033[31mSistema finalizado. Obrigado pela preferência!\033[m')
    print('')
    print('\033[33m{:=^60}'.format(''))
    print('\033[31m{:^60}\033[m'.format('Sistema finalizado. Obrigado pela preferência!'))
    print('{:^65}'.format('\033[31mDesenvolvido por Hendryl'))
    print('\033[33m{:=^60}'.format(''))
    exit()

if tipo_de_calculo == 1:                                                 #Para a soma
    print('Você entrou na aba de soma')
    while True:
        cont += 1
        valor = float(input(f'Para sair prescione "0000" \nDigite o {cont}º valor a ser somado: '))
        total += valor
        print(f'Igual a {total}')
        if valor == 0000:
            break
    print(f'O valor total é: {total}')


elif tipo_de_calculo == 2:                                               #Para a subtração
    print('Você entrou na aba de subtração, para sair prescione "0000"')
    cont += 1
    valor1 = float(input(f'Digite o {cont}º valor a ser subtraído: '))
    cont += 1
    valor2 = float(input(f'Digite o {cont}º valor a ser subtraído: '))
    subtotal = valor1 - valor2
    print(f'Igual a: {subtotal}')
    while True:
        cont += 1
        valor = float(input(f'Digite o {cont}º valor a ser subtraído: '))
        #if valor == 0000:
            #break
        total = subtotal - valor
        subtotal = total
        print(total)
        if valor == 0000:
            break
    print(f'O valor final é: {total}')


elif tipo_de_calculo == 3:
    print('Você entrou na aba de multiplicação')
    cont += 1
    valor1 = float(input(f'Para sair prescione "0000" \nDigite o {cont}º valor para ser multiplicado: '))
    cont += 1
    valor2 = float(input(f'Para sair prescione "0000" \nDigite o {cont}º valor para ser multiplicado: '))
    subtotal = valor1 * valor2
    print(f'Igual a {subtotal}')
    while True:
        cont += 1
        valor = float(input(f'Para sair prescione "0000" \nDigite o {cont}º valor para ser multiplicado:  '))
        if valor == 0000:
            break
        total = subtotal * valor
        subtotal = total
        print(subtotal)
    print(f'O valor final é: {subtotal}')


elif tipo_de_calculo == 4:
    print('Voce entrou na aba de divisão, para sair prescione "0000"')

elif tipo_de_calculo == 5:
    print('Você entrou na aba de potenciação.')
    while True:
        valor1 = float(input('Digite o valor da base: '))
        valor2 = float(input('Digite o valor do expoente: '))
        resposta = valor1 ** valor2
        print(' ')
        print(f'Igual a: {resposta}')
        continuar = int(input('''    [ 1 ] Sim 
    [ 2 ] Não
Deseja continuar: '''))
        if continuar == 2:
            break

elif tipo_de_calculo == 6:
    print('Você entrou na aba de Raiz Quadrada')
    while True:
        valor1 = float(input('Digite um valor: '))
        resposta = sqrt(valor1)
        print('')
        print(f'Igual a {resposta}')
        continuar = int(input('''    [ 1 ] Sim 
    [ 2 ] Não
Deseja continuar: '''))
        if continuar == 2:
            break
print('')
print('\033[31mSistema finalizado. Obrigado pela preferência!\033[m')
