# -*- coding: utf-8 -*-
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame

styles = getSampleStyleSheet()
styleN = styles["Normal"]
styleH = styles["Heading1"]

story = []

story.append( Paragraph("This is a heading", styleH) )
story.append( Paragraph("This is a paragraph in <i>Normal</i> style.", styleN) )

c = Canvas("hello.pdf")
f = Frame(inch, inch, 6*inch, 9*inch, showBoundary=1)
f.addFromList(story,c)
c.save()