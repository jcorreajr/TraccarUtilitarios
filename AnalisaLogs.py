'''
Analisa informações no arquivo de LOG e retorna informações solicitadas.
. Algumas informações:
.. TOP 10 com a qtd de posição enviada em um dia.
.. Comandos (desligar/ligar) enviados conforme IMEI
'''


def qtdposicao():
    dict_imei_filtrado = {}
    dict_imei_processado = {}

    with open('log.log', 'r') as file:
        for v in file.readlines():
            if v.split()[2] == 'INFO:':
                '''
                 Criar 2 dicionários com:
                 imei : quantidade
                 uma para atualização OK e outra para filtrado
                 Se ja existe o imei na lista, adicionar 1 na quantidade
                 Para isso, criar filtro p/ determinar quando é filtrado e quando é ok
                '''
                if v.split()[3] == 'Position' and v.split()[4] == 'filtered':
                    imei = v.split()[-1]
                    if imei in dict_imei_filtrado:
                        dict_imei_filtrado[imei] += 1
                    else:
                        dict_imei_filtrado[imei] = 1
                elif v.split()[4] == 'id:' and v.split()[6] == 'time:':
                    imei = v.split()[5]
                    if imei in dict_imei_processado:
                        dict_imei_processado[imei] += 1
                    else:
                        dict_imei_processado[imei] = 1

    sort_dict_imei_filtrado = sorted(dict_imei_filtrado.items(), key=lambda x: x[1], reverse=True)
    sort_dict_imei_processado = sorted(dict_imei_processado.items(), key=lambda x: x[1], reverse=True)

    print(f'...: Lista de IMEI filtrados Top 10 :... ')
    print(f'imei;qtd')
    for v in range(11):
        print(f'{sort_dict_imei_filtrado[v][0]};{sort_dict_imei_filtrado[v][1]}')

    print()
    print(f'...: Lista de IMEI processados Top 10 :... ')
    for v in range(11):
        print(f'{sort_dict_imei_processado[v][0]};{sort_dict_imei_processado[v][1]}')
    print()


def qtdcomandos():
    '''
    Analisa o Log e retorna a contagem dos comandos Stop e Start enviados
    2020-05-27 20:13:47  INFO: [C4055577] id: 874611123380643, command type: engineStop sent
    2020-05-27 20:17:38  INFO: [C4055577] id: 874611123380643, command type: engineResume sent
    :return:
    '''
    dict_imei_comandos_stop = {}
    dict_imei_comandos_resume = {}

    with open('log.log', 'r') as file:
        for v in file.readlines():
            if v.split()[2] == 'INFO:':
                try:
                    comando = v.split()[8]
                except IndexError:
                    comando = 'null'

                if comando == 'engineStop':

                    imei = v.split()[5][0:-1]

                    if imei in dict_imei_comandos_stop:
                        dict_imei_comandos_stop[imei] += 1
                    else:
                        dict_imei_comandos_stop[imei] = 1

                if comando == 'engineResume':

                    imei = v.split()[5][0:-1]
                    if imei in dict_imei_comandos_resume:
                        dict_imei_comandos_resume[imei] += 1
                    else:
                        dict_imei_comandos_resume[imei] = 1

    sort_dict_imei_comandos_stop = sorted(dict_imei_comandos_stop.items(), key=lambda x: x[1], reverse=True)
    sort_dict_imei_comandos_resume = sorted(dict_imei_comandos_resume.items(), key=lambda x: x[1], reverse=True)

    print(f'...: Lista de IMEIs com mais comandos STOP Top 10 :... ')
    print(f'imei;qtd')
    if len(sort_dict_imei_comandos_stop) >= 10:
        qtdlista = 10
    else:
        qtdlista = len(sort_dict_imei_comandos_stop)

    for v in range(qtdlista):
        print(f'{sort_dict_imei_comandos_stop[v][0]};{sort_dict_imei_comandos_stop[v][1]}')

    print()
    print(f'...: Lista de IMEIs com mais comandos START Top 10 :... ')
    if len(sort_dict_imei_comandos_resume) >= 10:
        qtdlista = 10
    else:
        qtdlista = len(sort_dict_imei_comandos_resume)

    for v in range(qtdlista):
        print(f'{sort_dict_imei_comandos_resume[v][0]};{sort_dict_imei_comandos_resume[v][1]}')
    print()
