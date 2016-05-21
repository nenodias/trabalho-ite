# *-* coding:utf-8 *-*
import sys
from timeit import default_timer as timer

class Temporizador():

    def __init__(self, nome_arquivo = None):
        prefix = ('pypy' if 'pypy' in sys.executable  else 'python')
        sufix = '.txt'
        self.nome_arquivo = nome_arquivo or prefix + sufix

    def __call__(self, funcao, *args, **kwargs):
        def wrapper():
            inicio = timer()
            retorno = funcao(*args, **kwargs)
            fim = timer()
            tempo = fim - inicio
            #print(tempo)
            self._grava_arquivo(funcao, inicio, fim, tempo)
            return retorno
        return wrapper

    def _grava_arquivo(self, funcao, inicio, termino, tempo):
        with open(self.nome_arquivo, 'w') as arquivo:
            arquivo.write(sys.version)
            arquivo.write('\n')
            arquivo.write('Função: {funcao} \nInício: {inicio}\nTermino: {termino}\nExecução em {tempo} '.format(
                funcao=funcao.__name__,
                inicio=inicio,
                termino=termino,
                tempo=tempo
                ) 
            )
            arquivo.write('\n')

def temporizador(funcao, *args, **kwargs):
    nome_arquivo = None
    prefix = ('pypy' if 'pypy' in sys.executable  else 'python')
    sufix = '.txt'
    nome_arquivo = nome_arquivo or prefix + sufix
    def wrapper():
        inicio = timer()
        retorno = funcao(*args, **kwargs)
        termino = timer()
        tempo = termino - inicio
        print(tempo)
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(sys.version)
            arquivo.write('\n')
            arquivo.write('Função: {funcao} \nInício: {inicio}\nTermino: {termino}\nExecução em {tempo} '.format(
                funcao=funcao.__name__,
                inicio=inicio,
                termino=termino,
                tempo=tempo
                ) 
            )
            arquivo.write('\n')
        return retorno
    return wrapper

lista = []

@temporizador
def operacao_arquivo():
    with open('logo.png', 'r') as logo:
        text = logo.read()
        for char in text:
            lista.append( bin( ord(char) ) )

operacao_arquivo()