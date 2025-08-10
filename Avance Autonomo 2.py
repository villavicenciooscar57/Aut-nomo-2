import turtle
import random

# Lista de palabras posibles
# Puedes agregar más palabras, pero asegúrate de que sean adecuadas para la dificultad.
palabras = ["casa", "lobo", "flor", "rayo", "arbol", "coche", "gato"]

# Elegir una palabra aleatoria de la lista
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
vidas = 6  # Número de vidas para el juego
intentos_fallidos = 0 # Contador para saber qué parte del cuerpo dibujar

# Configurar la pantalla del juego
pantalla = turtle.Screen()
pantalla.title("Juego del Ahorcado")
pantalla.bgcolor("lightblue")

# Tortuga para dibujar el ahorcado
dibujo = turtle.Turtle()
dibujo.hideturtle()
dibujo.speed(5) # Aumenté la velocidad para que el dibujo sea más rápido
dibujo.width(3)

# Tortuga para mostrar texto
texto = turtle.Turtle()
texto.hideturtle()
texto.penup()
texto.goto(-150, 200)

# Función para dibujar la base del ahorcado
def dibujar_base():
    dibujo.penup()
    dibujo.goto(-100, -150)
    dibujo.pendown()
    dibujo.forward(200)  # Base
    dibujo.backward(100)
    dibujo.left(90)
    dibujo.forward(250)  # Poste vertical
    dibujo.right(90)
    dibujo.forward(150)  # Poste horizontal
    dibujo.right(90)
    dibujo.forward(40)   # Cuerda

# Función para dibujar una parte del cuerpo según el número de intentos fallidos
def dibujar_ahorcado(intentos):
    if intentos == 1:
        # Cabeza
        dibujo.penup()
        dibujo.goto(50, 110)
        dibujo.setheading(0)
        dibujo.pendown()
        dibujo.circle(20)
    elif intentos == 2:
        # Cuerpo
        dibujo.penup()
        dibujo.goto(50, 90)
        dibujo.setheading(-90)
        dibujo.pendown()
        dibujo.forward(80)
    elif intentos == 3:
        # Brazo izquierdo
        dibujo.penup()
        dibujo.goto(50, 70)
        dibujo.setheading(135)
        dibujo.pendown()
        dibujo.forward(40)
    elif intentos == 4:
        # Brazo derecho
        dibujo.penup()
        dibujo.goto(50, 70)
        dibujo.setheading(45)
        dibujo.pendown()
        dibujo.forward(40)
    elif intentos == 5:
        # Pierna izquierda
        dibujo.penup()
        dibujo.goto(50, 10)
        dibujo.setheading(-135)
        dibujo.pendown()
        dibujo.forward(50)
    elif intentos == 6:
        # Pierna derecha
        dibujo.penup()
        dibujo.goto(50, 10)
        dibujo.setheading(-45)
        dibujo.pendown()
        dibujo.forward(50)