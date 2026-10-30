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