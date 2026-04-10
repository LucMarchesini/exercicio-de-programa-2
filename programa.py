from funcoes import *

guardados = []
count_rolagens = 0
contador_para_rodar = 5
cartela_de_pontos = {
        'regra_simples':  {
            1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1
            },
        'regra_avancada' : {
            'sem_combinacao':-1,
            'quadra': -1,
            'full_house': -1,
            'sequencia_baixa': -1,
            'sequencia_alta': -1,
            'cinco_iguais': -1
            }
        }

imprime_cartela(cartela_de_pontos) # IMPRIME SEM PRINT
rolados = rolar_dados(contador_para_rodar)
