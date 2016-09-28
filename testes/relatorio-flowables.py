# -*- coding: utf-8 -*-
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.pdfgen.canvas import Canvas

stylesheet = getSampleStyleSheet()

style = stylesheet["BodyText"]
p = Paragraph('This is a very silly example', style)
c  = Canvas("hello.pdf")
aW = 460
aH = 800
w, h = p.wrap(aW, aH)
if w <= aW and h <= aH:
    p.drawOn(c, 0, aH)
    aH = aH - h
    c.save()
else:
    raise ValueError, "Not enought room"