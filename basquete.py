
# Criando um dicionário em que a chave é o jogo e o valor é uma lista das estatísticas do jogo:
# [placar, mínimo da temporada, máximo da temporada, quabra de recorde mínimo, quebra de recorde máximo].
# tabela = {jogo: [estatísticas]}

tabela = {1: [12, 12, 12, 0, 0],
          2: [24, 12, 24, 0, 1],
          3: [10, 10, 24, 1, 1],
          4: [24, 10, 24, 1, 1],
}
# print(list(tabela.keys())[-1])
# jogo[0] = placar
# jogo[1] = mínimo temporada
# jogo[2] = máximo temporada
# jogo[3] = quebra de recorde mínimo
# jogo[4] = quebra de recorde máximo

placar = int(input("Insira o placar do jogo: "))

# Aqui temos o último jogo registrado no dicionário "tabela"
ultimo_jogo = (list(tabela.keys())[-1])

# ID do jogo
jogo = ultimo_jogo + 1

for jogo in tabela.values():
    if placar > jogo[0]:
        min_temp = None # jogo[1] do último jogo # se a chave for a maior de todas, acessá-la
        max_temp = placar
        quebra_min = None # jogo[3] do último jogo
        quebra_max = None # jogo[4] do último jogo + 1
    elif placar < jogo[0]:
        min_temp = placar
        max_temp = None  # jogo[2] do último jogo
        quebra_min = None  # jogo[3] do último jogo + 1
        quebra_max = None  # jogo[4] do último jogo
    else:
        min_temp = None # jogo[1] do último jogo
        max_temp = None  # jogo[2] do último jogo
        quebra_min = None  # jogo[3] do último jogo
        quebra_max = None  # jogo[4] do último jogo

# Lista com as estatística do jogo
estatisticas = [placar, min_temp, max_temp, quebra_min, quebra_max]

# Dicionário com jogo + estatísticas que será gerado e acrescentado ao dicionário "tabela"

novo_jogo = dict( = estatisticas)

tabela.update(novo_jogo)
print(tabela)
"""
a_dict = {}
name = "John"
age = 20
height = 62

for variable in ["name", "age", "height"]:
    a_dict[variable] = eval(variable)

print(a_dict)
"""
