# Exercício 1

import turtle

class Forma:
    def desenhar(self):
        pass

class Circulo(Forma):
    def desenhar(self):
        t = turtle.Turtle()
        t.circle(50)  
        turtle.done()

class Quadrado(Forma):
    def desenhar(self):
        t = turtle.Turtle()
        for _ in range(4):
            t.forward(100)  
            t.right(90)     
        turtle.done()

quadrado = Quadrado()
quadrado.desenhar()

