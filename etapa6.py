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