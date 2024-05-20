print('Digite 1 para converter de Quilômetros para Milhas ou 2 para converter de Milhas para Quilômetros: ')

option = int(input())

if option == 1:
    km = float(input('Quantos Quilômetros deseja converter? '))
    mile = km / 1.61
    print('Total em Milhas:', mile)

elif option == 2:
    mile = float(input('Quantas Milhas deseja converter? '))
    km = mile * 1.61
    print('Total em Quilômetros:', km)

else:
    print('Escolha uma opção válida (1 ou 2)')
