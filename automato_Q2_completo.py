import sys
import colorama
import csv

entrada = 'O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico'

prod = {
    '(X, )': 'S',
    '(S,c)': 'C',
    '(C,o)': 'O',
    '(O,m)': 'M',
    '(M,p)': 'P',
    '(P,u)': 'U',
    '(U,t)': 'T',
    '(T,a)': 'A',
    '(A,d)': 'D',
    '(D,o)': 'O',
    '(O,r)': 'R',
    '(R, )': 'Z'
}
estado_inicial = 'X'
estado_final = 'Z'

def rodar_automato(entrada, prod, estado_inicial, estado_final):
    estado_atual = estado_inicial
    posicao = -1
    tentativa = True
    inicioComputador = 0
    ocorrencias = []

    for simbolo in entrada:
        posicao = posicao + 1
        try:
            if tentativa:
                inicioComputador = posicao
                tentativa = False
            estado_seguinte = prod[f'({estado_atual},{simbolo})']
            estado_atual = estado_seguinte
        except KeyError:
            tentativa = True
            estado_atual = estado_inicial

        if estado_atual == estado_final:
            estado_atual = estado_inicial
            tentativa = True
            ocorrencias.append(inicioComputador+1)

    return ocorrencias

        
ocorrencias = rodar_automato(entrada, prod, estado_inicial, estado_final)                                
print(f"Computador apareceu nas posições: {ocorrencias}")