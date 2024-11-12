# -*- coding: UTF-8 -*-
"""
Jogo de dados
Programa sob licença GNU V.3
Desenvolvido por: E. S. Pereira
Versão 0.0.01
"""

from random import randint

print('Jogo de dados')
print('Teste sua sorte')

while(True):
    try:
        numero = int(input('Escolha um número de 1 a 6: '))
    except:
        print('Erro ao ler o número digitado, digite apenas números de 1 a 6, letras não são aceitas.')
        break
    dado = randint(1, 6)
    if dado == numero:
        print('Parabéns, saiu o seu número no dado.')
    else:
        print('Não foi dessa vez')
        print(f'O número sorteado foi {dado}')
    print('Deseja tentar a sorte novamente?')
    continuar = input('Digite S para continuar ou N para sair: ')

    if continuar == 'N' or continuar == 'n':
        break