def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = []
    if orientacao == 'vertical':
        for i in range(linha, linha+tamanho):
            posicao.append([i,coluna])
    elif orientacao == 'horizontal':
        for i in range(coluna, coluna+tamanho):
            posicao.append([linha,i])
    return posicao

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    for j in range(len(posicao)):
        if posicao[j][0] > 9 or posicao[j][1] > 9:
            return False
        if 9<linha<0 or 9<coluna<0:
            return False
        for navio in frota:
            pos = frota[navio]
            for lista in pos:
                for i in range(len(lista)):
                    linhas = lista[i][0]
                    colunas = lista[i][1]
                    if posicao[j][0] == linhas and posicao[j][1] == colunas:
                        return False
    return True

frota = {}   
nome = ['porta-aviões', 'navio-tanque', 'navio-tanque', 'contratorpedeiro', 'contratorpedeiro', 'contratorpedeiro', 'submarino', 'submarino', 'submarino', 'submarino' ]
tamanho = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
for i in range(9):
    verificacao = False
    while verificacao == False:
        print(f'Insira as informações referentes ao navio {nome[i]} que possui tamanho {tamanho[i]}')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if nome[i] != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal >'))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
        else:
            orientacao = 'vertical'
        verificacao = posicao_valida(frota, linha, coluna, orientacao, tamanho[i])
        if verificacao == False:
            print('Esta posição não está válida!')
    posicao = define_posicoes(linha, coluna, orientacao, tamanho[i])
    if nome[i] not in frota:
        frota[nome[i]] = []
    frota[nome[i]].append(posicao)
    print(frota)
    

