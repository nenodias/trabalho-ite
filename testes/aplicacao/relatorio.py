# -*- coding: utf-8 -*-
import io
from reportlab.pdfgen import canvas

'''
SEEK_SET or 0 – Posição Inicial do arquivo
SEEK_CUR or 1 – Posição Atual do arquivo whence é passado
SEEK_END or 2 – Posição Final do arquivo
'''

def gerar_pdf():
    byte_array = io.BytesIO()
    c = canvas.Canvas(byte_array)
    c.drawString(100,750,"Welcome to Reportlab!")
    c.save()
    byte_array.seek(io.SEEK_SET)
    return byte_array
    '''
    #Exemplo de como gravar com o byte_array depois do pdf ser gerado
    with open('arquivo.pdf', 'wb') as f:
        f.write(byte_array.read())
    '''