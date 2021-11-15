"""
A variável 'tabela' se refere às estatísticas dos jogos já registrados por Maria.
A variável 'tabela' é ums lista de dicionários.
Cada dicionário contém o ID do jogo, o placar, e as outras estatísticas do jogo.
Cada dicionário se refere a um jogo.
"""
import pandas as pd
"""Importando biblioteca pandas pra geração de tabela no terminal."""

tabela = [
    {'Jogo': 1, 'Placar': 12, 'Min_temp': 12, 'Max_temp': 12, 'Recorde_min': 0, 'Recorde_max': 0},
    {'Jogo': 2, 'Placar': 24, 'Min_temp': 12, 'Max_temp': 24, 'Recorde_min': 0, 'Recorde_max': 1},
    {'Jogo': 3, 'Placar': 10, 'Min_temp': 10, 'Max_temp': 24, 'Recorde_min': 1, 'Recorde_max': 1},
    {'Jogo': 4, 'Placar': 24, 'Min_temp': 10, 'Max_temp': 24, 'Recorde_min': 1, 'Recorde_max': 1}
]

"""
Essa função cria um novo dicionário referente ao próximo jogo a ser registrado pelo usuário (Maria).

O jogo inserido será adicionado à lista de jogos (variável 'tabela'). 

Como será um dicionário, terá as mesmas chaves dos últimos jogos, porém receberá como valores variáveis geradas dentro \
da função 'basquete()'.

O resultado será o seguinte:

novo_jogo = {
            'Jogo': jogo,
            'Placar': placar, 
            'Min_temp': min_temporada, 
            'Max_temp': max_temporada,
            'Recorde_min': quebra_min,
            'Recorde_max': quebra_max
            }
"""

def basquete():
    print('\nESTA É A TABELA DE ESTATÍSTICAS ATUAIS:\n')
    """Usando a função DataFrame da bib pandas e eliminado o index (primeira coluna do DataFrame)"""
    tabela_format = (pd.DataFrame(tabela)).to_string(index = False)
    print(f'{tabela_format}\n')

    """Filtrando o último item (último jogo) da tabela existente"""
    for chave, valor in tabela[-1].items():

        """Filtrando a chave 'Jogo' no último dicionário (último jogo) da tabela"""
        if chave == 'Jogo':
            jogo = valor + 1
            placar = int(input(f'Insira o placar do {jogo}º jogo: '))

        """Filtrando a chave 'Min temp' no último último jogo da tabela"""
        if chave == 'Min_temp':
            if placar >= valor:
                min_temporada = valor
            else:
                min_temporada = placar

        """Filtrando a chave 'Max temp' no último último jogo da tabela"""
        if chave == 'Max_temp':
            if placar > valor:
                max_temporada = placar
            else:
                max_temporada = valor

        """Filtrando a chave 'Recorde min' no último último jogo da tabela"""
        if chave == 'Recorde_min':
            if min_temporada == placar:
                quebra_min = valor + 1
            else:
                quebra_min = valor

        """Filtrando a chave 'Recorde max' no último último jogo da tabela"""
        if chave == 'Recorde_max':
            if max_temporada == placar:
                quebra_max = valor + 1
            else:
                quebra_max = valor

    novo_jogo = {'Jogo': jogo,
                 'Placar': placar,
                 'Min_temp': min_temporada,
                 'Max_temp': max_temporada,
                 'Recorde_min': quebra_min,
                 'Recorde_max': quebra_max}

    tabela.append(novo_jogo)
    tabela_format = (pd.DataFrame(tabela)).to_string(index=False)
    print('\nESTA É A TABELA ATUALIZADA:\n')
    print(f'{tabela_format}\n')

    """Criando variável que perguntará ao usuário se deseja continuar inserindo jogos."""
    reiniciar = input('Deseja adicionar o placar de um novo jogo? [s/n] ')
    if reiniciar == 's':
        basquete()
    else:
        print('\nESTA É A TABELA DE ESTATÍSTICAS ATUAIS ANTES DE SAIR...\n')
        print(f'{tabela_format}\n')
        print('Saindo...')
        exit()

basquete()
