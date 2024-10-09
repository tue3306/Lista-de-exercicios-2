# Exercício 3

import turtle

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover_para_ponto(self):
        t = turtle.Turtle()
        t.penup()  
        t.goto(self.x, self.y)  
        t.pendown()  
        turtle.done()  

ponto = Ponto(100, 150)
ponto.mover_para_ponto()
