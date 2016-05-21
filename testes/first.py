# *-* coding:utf-8 *-*
'''
Timeit é uma biblioteca para medir o tempo de execução
Teste de uma Leitura e Gravação de uma cópia de um Arquivo
'''
from timeit import default_timer as timer

start = timer()

with open('logo.png', 'rb') as origem:
    with open('logo-copia.png', 'wb') as destino:
        destino.write( origem.read() )

end = timer()
with open('result-first', 'a') as resultado:
    resultado.write( str(end - start) )
    resultado.write('\n')