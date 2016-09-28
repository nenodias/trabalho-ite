# -*- coding: utf-8 -*-
import io
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate
from PollyReports import *

'''
SEEK_SET or 0 – Posição Inicial do arquivo
SEEK_CUR or 1 – Posição Atual do arquivo whence é passado
SEEK_END or 2 – Posição Final do arquivo
'''

def gerar_pdf(dados):
    byte_array = io.BytesIO()
    if not dados or len(dados) < 1:
        c = Canvas(byte_array)
        c.drawString(100,750,"Sem registros")
        c.save()
    else:
        rpt = Report(dados)
        rpt.detailband = Band([
            Element((36, 0), ("Helvetica", 11), key = "nome", align='left'),
            Element((236, 0), ("Helvetica", 11), key = "email"),
            Element((380, 0), ("Helvetica", 11), key = "data_nascimento"),
            Element((500, 0), ("Helvetica", 11), key = "cpf"),
        ])
        rpt.pageheader = Band([
            Element((36, 0), ("Times-Bold", 20), text = "Usuários"),
            Element((36, 24), ("Helvetica", 12), text = "Nome", align='left'),
            Element((236, 24), ("Helvetica", 12), text = "E-mail"),
            Element((380, 24), ("Helvetica", 12), text = "Data Nascimento"),
            Element((500, 24), ("Helvetica", 12), text = "CPF"),
            Rule((36, 42), 7.5*72, thickness = 2),
        ])
        rpt.pagefooter = Band([
            Rule((36, 42), 7.5*72, thickness = 2),
            Element((36, 16), ("Helvetica-Bold", 12), sysvar = "pagenumber", format = lambda x: "Página %d" % x),
        ])

        c = Canvas(byte_array, (72*11, 72*8.5))
        rpt.generate(c)
        c.save()

    byte_array.seek(io.SEEK_SET)
    return byte_array
    '''
    #Exemplo de como gravar com o byte_array depois do pdf ser gerado
    with open('arquivo.pdf', 'wb') as f:
        f.write(byte_array.read())
    '''