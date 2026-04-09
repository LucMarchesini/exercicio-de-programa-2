import random
def rolar_dados(dados):
    resultados = []
    for i in range(dados):
        s = random.randint(1, 6)
        resultados.append(s)
    return resultados
