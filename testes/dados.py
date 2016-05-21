# *-* coding:utf-8 *-*
import numpy as np

from timeit import default_timer as timer

start = timer()

colunas = {
    "ValContrato": 5,
    "ValTotal": 6,
    "DatAssinatura": 7,
    "DatInicioVigencia": 8,
    "DatFinalVigencia": 9,
}
dados = None
with open('dados.csv', 'r') as data:
    dados = data.read().split('\n')

somatoria = None

for dado in dados:
    try:
        valores = dado.split(';')

        contrato = np.float32( valores[ colunas['ValContrato'] ] )
        valor_total = np.float32( valores[ colunas['ValTotal'] ] )
        
        aux = np.array( [ contrato, valor_total ] )
        print(aux)
        try:
            somatoria = somatoria + aux
        except:
            somatoria = aux
    except:
        pass

print(somatoria)

end = timer()
print( end - start )