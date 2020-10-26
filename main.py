'''
Utilitario traccar
funções:
.. Analisa Logs e retorna conforme função selecionada
.. precisa do arquivo log.log com os logs de saída do Traccar no mesmo diretório para análise

'''
import AnalisaLogs

while True:
    print(f'Escolha a opção abaixo:.. ')
    print(f'1 - Posições enviadas, Top-10')
    print(f'2 - Comandos (desligar/ligar) enviados')
    print(f'0 - Sair')
    escolha = int(input('__| '))

    if escolha == 1:
        AnalisaLogs.qtdposicao()
    if escolha == 2:
        AnalisaLogs.qtdcomandos()
    elif escolha == 0:
        break

