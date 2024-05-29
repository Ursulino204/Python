num1 = float(input('Digite sua nota 1: '))
num2 = float(input('Digite sua nota 2: '))
num3 = float(input('Digite sua nota 3: '))
num4 = float(input('Digite sua nota da prova: '))

media_atv = (num1 + num2 + num3)/2
media_final = (media_atv + num4)/2

if media_final > 10:
    print('Digite notas válidas!')
else:
    print(f'Sua média final é: {media_final:.2f}')
