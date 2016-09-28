# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch

'''
canvas.showPage()#break the page
canvas.getPageNumber()
'''

def hello(c):
    c.saveState()
    c.translate(inch,inch)
    c.setFont('Helvetica', 14)
    c.drawString(100,100,"Hello World")
    c.setStrokeColorRGB(0.2,0.5,0.4)
    c.setFillColorRGB(1,0,1)
    c.line(0, 0, 0, 1.7 * inch)
    c.line(0, 0, 1 * inch, 0)
    c.rect(0.2 * inch, 0.2 * inch, 1* inch, 1.5*inch, fill=1 )
    c.rotate(90)
    c.setFillColorRGB(0,0,0.77)
    c.drawString(0.3*inch, -inch, "Hello World")
    x = 100
    y = 200
    c.restoreState()
    image = "logo.png"
    c.drawInlineImage(image, 100,10, width=100,height=100)
    print(c.pageHasData())
    #c.showPage()


def coords(c):
    from reportlab.lib.colors import pink, black, red, blue, green
    c.setStrokeColor(pink)
    c.grid( [inch, 2*inch, 3*inch, 4*inch], [0.5*inch, inch,1.5*inch, 2*inch, 2.5*inch] )
    c.setStrokeColor(black)
    c.setFont("Times-Roman", 20)
    c.drawString(0, 0, "(0,0) of the origin")
    c.drawString(2.5 * inch, inch, "(2.5,1) in inches")
    c.drawString(4 * inch, 2.5*inch, "(4,2.5) in inches")
    c.setFillColor(red)
    c.rect(0, 2*inch, 0.2*inch, 0.3*inch, fill=1)
    c.setFillColor(green)
    c.rect(0, 4.5*inch, 0.4*inch, 0.2*inch, fill=1)
    c.circle(4.5*inch, 0.4*inch, 0.2*inch, fill=1)
    c.setFillColor(black)

def translate(c):
    from reportlab.lib.units import cm
    c.translate(2.3 * cm, 0.3*cm)
    coords(c)

def scale(c):
    from reportlab.lib.units import cm
    c.scale(0.75, 0.5)
    coords(c)

def mirror(c):
    c.translate(5.5 * inch, 0)
    c.scale(-1.0, 1.0)
    coords(c)

c = Canvas("hello.pdf",pagesize=letter)
mirror(c)
width, height = letter
print(width, height)
c.showPage()
c.save()