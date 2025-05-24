"""
1. [1.0 pt] Implemente AFDs, em uma linguagem de programação à sua escolha, que aceitem as seguintes cadeias:
    b) Todas as cadeias em {a,b}* de modo que o último símbolo seja b e o número de símbolos a seja par.
"""

entradas = [ "b", "babab", "baab", "aab", "a", "ab", "bab", "aba"]

transicoes = {
    '(S,a)': 'IaFa',
    '(S,b)': 'PaFb',
    '(IaFa,a)': 'PaFa',
    '(IaFa,b)': 'IaFb',
    '(PaFb,a)': 'IaFa',
    '(PaFb,b)': 'PaFb',
    '(IaFb,a)': 'PaFa',
    '(IaFb,b)': 'IaFb',
    '(PaFa,a)': 'IaFa',
    '(PaFa,b)': 'PaFb',
}
estado_inicial = 'S'
estado_final = 'PaFb'

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
            print(f"{cadeia}: Rejeitada")
            estado_atual = estado_inicial
        else:
            estado_atual = estado_inicial
            print(f"{cadeia}: Aceita")

        
rodar_automato(entradas, transicoes, estado_inicial, estado_final)                                
        
