import sys
import colorama
import csv

estado_inicial = '0'
transicoes = {
    '(0,25)': '25',
    '(0,50)': '50',
    '(0,100)': '100',
    '(25,25)': '50',
    '(25,50)': '75',
    '(25,100)': '25',
    '(50,25)': '75',
    '(50,50)': '100',
    '(50,100)': '50',
    '(75,25)': '100',
    '(75,50)': '25',
    '(75,100)': '75',
    '(100,25)': '25',
    '(100,50)': '50',
    '(100,100)': '100',
}

transducoes = {
    '(0,25)': '0',
    '(0,50)': '0',
    '(0,100)': '1',
    '(25,25)': '0',
    '(25,50)': '0',
    '(25,100)': '1',
    '(50,25)': '0',
    '(50,50)': '1',
    '(50,100)': '1',
    '(75,25)': '1',
    '(75,50)': '1',
    '(75,100)': '1',
    '(100,25)': '0',
    '(100,50)': '0',
    '(100,100)': '1',
}

entrada = ["100", "25", "25", "25", "25", "100", "50", "50", "100", "100", "25", "50", "25", "50", "25", "25", "100"]

def transdutor(entrada, estado_inicial, transicoes, transducoes):
    estado_atual = estado_inicial
    saida = []

    for simbolo in entrada:
        try:
            estado_seguinte = transicoes[f'({estado_atual},{simbolo})']
            saida.append(transducoes[f'({estado_atual},{simbolo})'])
            estado_atual = estado_seguinte
        except KeyError:
            break;
    return saida

saida = transdutor(entrada, estado_inicial, transicoes, transducoes)

print(saida)

