import random

def jogar():
    print('**********************************')
    print('Bem Vindo ao Jogo da Adivinhação !')
    print('**********************************')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual o nivel de dificuldade ?')
    print('(1) Facil (2) Dificil (3) Dificil')

    nivel = int(input('Defina um Nivel:'))

    if (nivel == 1) :
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for tentativa in range (1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(tentativa, total_de_tentativas))

        chute_str = input('Digite um número entre 1 e 100!')
        print('Você Digitou ', chute_str)
        chute = int(chute_str)

        if ( chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue
         #Acertou
        if( chute == numero_secreto):
            print('Você acertou e fez {} pontos !'.format(pontos))
            break
         #Errou


        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            if (chute > numero_secreto):
                print('Errou! Seu chute foi maior que o número secreto.')

            else:
                print('Errou! Seu chute foi menor que o número secreto. ')


    print('Fim de jogo')
    print(f'O númeuro secreto era {numero_secreto}.você fez {pontos}')



    #permite executar automaticamente via linha comando
if(__name__ == '__main__'):
        jogar()

