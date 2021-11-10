"""
A variável 'tabela' se refere às estatísticas dos jogos já registrados por Maria.
A variável 'tabela' é ums lista de dicionários.
Cada dicionário contém o ID do jogo, o placar, e as outras estatísticas do jogo.
Cada dicionário se refere a um jogo.
"""
tabela = [
    {'Jogo': 1, 'Placar': 12, 'Min. temporada': 12, 'Max temporada': 12, 'Quebra recorde min.': 0, 'Quebra recorde máx.': 0},
    {'Jogo': 2, 'Placar': 24, 'Min. temporada': 12, 'Max temporada': 24, 'Quebra recorde min.': 0, 'Quebra recorde máx.': 1},
    {'Jogo': 3, 'Placar': 10, 'Min. temporada': 10, 'Max temporada': 24, 'Quebra recorde min.': 1, 'Quebra recorde máx.': 1},
    {'Jogo': 4, 'Placar': 24, 'Min. temporada': 10, 'Max temporada': 24, 'Quebra recorde min.': 1, 'Quebra recorde máx.': 1}
]

"""
Essa função cria um novo dicionário referente ao próximo jogo a ser registrado pelo usuário (Maria).

O jogo inserido será adicionado à lista de jogos (variável 'tabela'). 

Como será um dicionário, terá as mesmas chaves dos últimos jogos, porém receberá como valores variáveis geradas dentro \
da função 'basquete()'.

O resultado será o seguinte:

novo_jogo = {'Jogo': jogo, 'Placar': placar, 'Min. temporada': min_temporada, 'Max temporada': max_temporada, \
                 'Quebra recorde min.': quebra_min, 'Quebra recorde máx.': quebra_max}
"""
def basquete():

    """Filtrando o último item (último jogo) da tabela existente"""
    for chave, valor in tabela[-1].items():

        """Filtrando a chave 'Jogo' no último dicionário (último jogo) da tabela"""
        if chave == 'Jogo':
            jogo = valor + 1
            placar = int(input(f'Insira o placar do {jogo}º jogo '))

        """Filtrando a chave 'Min. temporada' no último último jogo da tabela"""
        if chave == 'Min. temporada':
            if placar >= valor:
                min_temporada = valor
            else:
                min_temporada = placar

        """Filtrando a chave 'Max temporada' no último último jogo da tabela"""
        if chave == 'Max temporada':
            if placar > valor:
                max_temporada = placar
            else:
                max_temporada = valor

        """Filtrando a chave 'Quebra recorde min.' no último último jogo da tabela"""
        if chave == 'Quebra recorde min.':
            if min_temporada == placar:
                quebra_min = valor + 1
            else:
                quebra_min = valor

        """Filtrando a chave 'Quebra recorde máx.' no último último jogo da tabela"""
        if chave == 'Quebra recorde máx.':
            if max_temporada == placar:
                quebra_max = valor + 1
            else:
                quebra_max = valor

    novo_jogo = {'Jogo': jogo, 'Placar': placar, 'Min. temporada': min_temporada, 'Max temporada': max_temporada, \
                 'Quebra recorde min.': quebra_min, 'Quebra recorde máx.': quebra_max}

    tabela.append(novo_jogo)
    print(tabela)
    """Criando variável que perguntará ao usuário se deseja continuar inserindo jogos."""
    reiniciar = input('Deseja adicionar o placar de um novo jogo? [s/n] ')
    if reiniciar == 's':
        basquete()
    else:
        print(tabela)
        print('Saindo...')
        exit()

basquete()
