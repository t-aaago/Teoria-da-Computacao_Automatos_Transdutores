import sys
import colorama
import csv

entradas = [
    '0', '0100', '100', '1', '1001','010', '0001'
]

transicoes = {
    '(S,0)': 'S',
    '(S,1)': 'A',
    '(A,0)': 'B',
    '(B,0)': 'S'
}
estado_inicial = 'S'
estado_final = 'S'



def rodar_automato(entradas, transicoes, estado_inicial, estado_final):
    estado_atual = estado_inicial

    for cadeia in entradas:
        for simbolo in cadeia:
            try:
                estado_seguinte = transicoes[f'({estado_atual},{simbolo})']
                estado_atual = estado_seguinte
            except KeyError:
                break;
        
        if estado_atual != estado_final:
            estado_atual = estado_inicial
            print(f"{cadeia}: Rejeitada")
        else:
            estado_atual = estado_inicial
            print(f"{cadeia}: Aceita")

        
rodar_automato(entradas, transicoes, estado_inicial, estado_final)                                
        
