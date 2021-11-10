tabela = [
    {'Jogo': 1, 'Placar': 12, 'Min. temporada': 12, 'Max temporada': 12, 'Quebra recorde min.': 0, 'Quebra recorde máx.': 0},
    {'Jogo': 2, 'Placar': 24, 'Min. temporada': 12, 'Max temporada': 24, 'Quebra recorde min.': 0, 'Quebra recorde máx.': 1},
    {'Jogo': 3, 'Placar': 10, 'Min. temporada': 10, 'Max temporada': 24, 'Quebra recorde min.': 1, 'Quebra recorde máx.': 1},
    {'Jogo': 4, 'Placar': 24, 'Min. temporada': 10, 'Max temporada': 24, 'Quebra recorde min.': 1, 'Quebra recorde máx.': 1}
]

def basquete():
    for chave, valor in tabela[-1].items():
        if chave == 'Jogo':
            jogo = valor + 1
            placar = int(input(f'Insira o placar do {jogo}º jogo '))

        if chave == 'Min. temporada':
            if placar >= valor:
                min_temporada = valor
            else:
                min_temporada = placar

        if chave == 'Max temporada':
            if placar > valor:
                max_temporada = placar
            else:
                max_temporada = valor

        if chave == 'Quebra recorde min.':
            if min_temporada == placar:
                quebra_min = valor + 1
            else:
                quebra_min = valor

        if chave == 'Quebra recorde máx.':
            if max_temporada == placar:
                quebra_max = valor + 1
            else:
                quebra_max = valor

    novo_jogo = {'Jogo': jogo, 'Placar': placar, 'Min. temporada': min_temporada, 'Max temporada': max_temporada, \
                 'Quebra recorde min.': quebra_min, 'Quebra recorde máx.': quebra_max}
    tabela.append(novo_jogo)
    print(tabela)
    reiniciar = input('Deseja adicionar o placar de um novo jogo? [s/n] ')
    if reiniciar == 's':
        basquete()
    else:
        print(tabela)
        print('Saindo...')
        exit()

basquete()
