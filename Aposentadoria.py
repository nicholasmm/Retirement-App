nome = input('Digite seu nome: ')
sexo = int(input('Digite seu sexo, 1 para HOMEM e 2 para MULHER: '))
idade = int(input('Digite seu idade: '))
anos_servico = int(input('Digite seus anos de serviço: '))

idade_homem = 65
idade_mulher = 62
servico_H = 20
servico_M = 15

while True:
    sexo = int(input('Digite seu sexo, 1 para HOMEM e 2 para MULHER: '))

    if sexo < 1 or sexo > 2:
        print("Tente novamente. Leia a instrução com atenção")
    else:
        break

if sexo == 1: 
    if idade >= idade_homem and anos_servico >= servico_H:
        print ('Parabéns',nome,'você pode se aposentar')
    else : 
        print (nome,'infelizmente você não pode se aposentar')

if sexo == 2: 
    if idade >= idade_mulher and anos_servico >= servico_M:
        print ('Parabéns',nome,'você pode se aposentar.')
    else : 
        print (nome,'infelizmente você não pode se aposentar.')
