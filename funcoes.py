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

def posiciona_frota(frota):
    resultado = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    for navio in frota:
        pos = frota[navio]
        for lista in pos:
            for i in range(len(lista)):
                linha = lista[i][0]
                coluna = lista[i][1]
                resultado[linha][coluna] = 1
    return resultado

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def afundados(frota, tabuleiro):
    afundado = 0
    for navio in frota:
        pos = frota[navio]
        for lista in pos:
            soma = 0
            for i in range(len(lista)):
                linha = lista[i][0]
                coluna = lista[i][1]
                if tabuleiro[linha][coluna] == 'X':
                    soma +=1
            if soma == len(lista):
                afundado +=1
    return afundado
