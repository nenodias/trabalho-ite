from reportlab.pdfgen.canvas import Canvas
from PollyReports import *

dados = [
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
    {"nome":"Horácio", "idade":23},
    {"nome":"Bianca", "idade":19},
    {"nome":"Luara", "idade":16},
    {"nome":"Pedro", "idade":23},
]

rpt = Report(dados)
rpt.detailband = Band([
    Element((36, 0), ('Helvetica', 11), key="nome"),
    Element((400, 0), ('Helvetica', 11), key="idade", align="right")
])

rpt.pageheader = Band([
    Element((36, 0), ('Helvetica', 11), text="Nome"),
    Element((400, 0), ('Helvetica', 11), text="Idade", align="right"),
    Rule((36, 42), 7.5*72, thickness=2)
])

orientacao_paisagem = (72 *11, 72*8.5)

#canvas = Canvas("sample2.pdf", orientacao_paisagem) usando Paisagem
canvas = Canvas("sample2.pdf")
rpt.generate(canvas)
canvas.save()