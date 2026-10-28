def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = []
    if orientacao == 'vertical':
        for i in range(linha, linha+tamanho):
            posicao.append([i,coluna])
    elif orientacao == 'horizontal':
        for i in range(coluna, coluna+tamanho):
            posicao.append([linha,i])
    return posicao