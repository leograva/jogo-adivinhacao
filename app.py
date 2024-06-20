import random

chances = 5
numero_aleatorio = random.randint(1, 100)

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

while(chances > 0):
    entrou = True
    escolhido = int(input('Escolha um número'))
    if(escolhido == numero_aleatorio):
        print('Parabéns, voce acertou!!!')
        break
    else:
        if(escolhido > numero_aleatorio):
            print('O número digitado é maior que o número misterioso')
        elif(escolhido < numero_aleatorio):
            print('O número digitado é menor que o número misterioso')
        chances-=1
print(f'Fim de jogo!!!, o número correto é: {numero_aleatorio}')

