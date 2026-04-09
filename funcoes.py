import random
def rolar_dados(dados):
    resultados = []
    for i in range(dados):
        s = random.randint(1, 6)
        resultados.append(s)
    return resultados
def guardar_dado(rolados, guardados, indice):
    guardados.append(rolados[indice])
    rolados.pop(indice)
    return [rolados, guardados]