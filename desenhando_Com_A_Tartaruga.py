import turtle
import twilio

print (twilio.__version__)

def draw_square ():
    window = turtle.Screen()
    window.bgcolor("white")

    quadrado = turtle.Turtle()

    quadrado.shape ("turtle")
    quadrado.color("blue")
    quadrado.speed (10)
    drawQuadrado(quadrado)
    
def drawQuadrado(quadrado):
    for i in range(1,5):
        quadrado.forward (100)
        quadrado.right (90)

        
    
    

    
    circulo = turtle.Turtle()

    circulo.color ("red")
    circulo.shape ("turtle")
    circulo.circle (50)
    
    
    
    
    

    

    window.exitonclick()

draw_square()
