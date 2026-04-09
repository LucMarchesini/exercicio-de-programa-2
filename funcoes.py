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

def remover_dado(rolados, guardados, indice):
    rolados.append(guardados[indice])
    guardados.pop(indice)
    return [rolados, guardados]

def calcula_pontos_regra_simples(lista):
    dic = {}
    conta1, conta2, conta3, conta4, conta5, conta6 = lista.count(1), lista.count(2), lista.count(3), lista.count(4), lista.count(5), lista.count(6)
    dic[1], dic[2], dic[3], dic[4], dic[5], dic[6] = 1*conta1, 2*conta2, 3*conta3, 4*conta4, 5*conta5, 6*conta6
    return dic

def calcula_pontos_soma(lista):
    soma = 0
    for i in range(len(lista)):
        soma+=lista[i]
    return soma

def calcula_pontos_sequencia_baixa(lista):
    if (1 in lista and 2 in lista and 3 in lista and 4 in lista) or (2 in lista and 3 in lista and 4 in lista and 5 in lista) or (3 in lista and 4 in lista and 5 in lista and 6 in lista):
        return 15
    else:
        return 0