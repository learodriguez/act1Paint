'''Herramientas Computacionales: El Arte de la Programación
Grupo: 201   TC1001S
Modified by:
        Léa Rodríguez Jouault A01659896   
        Mauricio Juárez Sánchez A01660336'''

from turtle import *
from freegames import vector
from math import sqrt # se añade la librería math para utilizar la raiz cuadrada

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

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

def circle(start, end):
    #x=rcos(theta) y=rsin(theta)
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    r=sqrt((end.x*2)+(end.y*2)) # radio

    down()
    begin_fill()
    forward(r)
    for i in range(1,360): # total del círculo
        speed(0) # velocidad máxima
        left(1)
        goto(start.x, start.y)
        forward(r); # se llenará el cículo con los radios
    pass  # TODO

def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO

def triangle(start, end):
    "Draw triangle from start to end."
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
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

# Se añaden colores
onkey(lambda: color('cyan'), 'C')
onkey(lambda: color('purple'), 'P')
onkey(lambda: color('yellow'), 'Y')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
