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

while True: # Esse loop serve para verificar se a tabela esta completa e contempla o jogo inteiro
    cartela_cheia = True

    for chave1 in cartela_de_pontos["regra_simples"]:
        if cartela_de_pontos["regra_simples"][chave1] == -1:
            cartela_cheia = False
    for chave2 in cartela_de_pontos["regra_avancada"]:
        if cartela_de_pontos["regra_avancada"][chave2] == -1:
            cartela_cheia = False

    if cartela_cheia == True: # Acaba o jogo se nao tiver nenhuma vazia
        break

    print(f'Dados rolados: {rolados}')
    print(f"Dados guardados: {guardados}")
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:') # Solicitação para o usuário no print
    
    while True: # Roda o loop enquanto o usuário não digita uma entrada válida (opção das listas)
        usuario = input()
        if usuario == '1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            indice_guardar = int(input())
            contador_para_rodar -= 1
            dados_guardados = guardar_dado(rolados, guardados, indice_guardar)
            rolados = dados_guardados[0]
            guardados = dados_guardados[1]
            break

        elif usuario == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice_remover = int(input())
            contador_para_rodar += 1
            dados_removidos = remover_dado(rolados, guardados, indice_remover)
            rolados = dados_removidos[0]
            guardados = dados_removidos[1]
            break

