import random

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

frota = {}   
nome = ['porta-aviões', 'navio-tanque', 'navio-tanque', 'contratorpedeiro', 'contratorpedeiro', 'contratorpedeiro', 'submarino', 'submarino', 'submarino', 'submarino' ]
tamanho = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
for i in range(len(nome)):
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


frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_player = posiciona_frota(frota)

jogando = True
posicoes_jogadas = []
posicoes_oponente = []

while jogando == True:
    print(monta_tabuleiros(tabuleiro_player, tabuleiro_oponente))
    posicao_repetida = True
    while posicao_repetida == True:
        linha = int(input('Jogador, qual linha deseja atacar? '))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))
        coluna = int(input('Jogador, qual coluna deseja atacar? '))
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))
        if [linha, coluna] in posicoes_jogadas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            posicao_repetida = False
    posicoes_jogadas.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:
        linha_oponente = random.randint(0,9)
        coluna_oponente = random.randint(0,9)
        while [linha_oponente, coluna_oponente] in posicoes_oponente:
            linha_oponente = random.randint(0,9)
            coluna_oponente = random.randint(0,9)
        posicoes_oponente.append([linha_oponente, coluna_oponente])
        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')
        tabuleiro_player = faz_jogada(tabuleiro_player, linha_oponente, coluna_oponente)
        if afundados(frota, tabuleiro_oponente) == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False

    
