"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""
'''Herramientas Computacionales: El Arte de la Programación
Grupo: 201   TC1001S
Modified by:
        Léa Rodríguez Jouault A01659896   
        Mauricio Juárez Sánchez A01660336'''
#Importando librería math para calcular la raíz
#Importando turtle para figuras e instrucciones de movimiento.
from math import sqrt
from turtle import *
from freegames import vector

#Esta función toma los 2 puntos que selecciones el usuario y los une con una línea
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
# Dibuja utilizando líneas y giros de 90°
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()
#Dibuja un circulo obteniendo el radio y con ayuda de líneas forma la figura.
def circle(start, end):
    #x=rcos(theta) y=rsin(theta)
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    r=sqrt((end.x**2)+(end.y**2))

    down()
    begin_fill()
    forward(r)
    for i in range(1,360):
        speed(0)
        left(1)
        goto(start.x, start.y)
        forward(r)
    pass  # TODO
#Dibuja 2 líneas y con ayuda de fill se completa el rectángulo
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #Dibuja un rectangulo con base del tamaño de la pluma y altura siendo la mitad de su base
    if((start.x)-(end.x)!=0):
        for count in range(2):
            forward(end.x - start.x)
            left(90)
            forward((end.x - start.x)/2)
            left(90)
    end_fill()
    pass  # TODO
#Con un ángulo base, dibuja un triángulo con los clicks del usuario como referenciay apoyandose de un ángulo.
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    forward(end.x - start.x)
    left(135)
    forward(end.x - start.x)
    goto(start.x, start.y)
    end_fill()
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
#Se agregaron opciones de colores correspondientes a una tecla de teclado.
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('cyan'), 'C')
onkey(lambda: color('purple'), 'P')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
