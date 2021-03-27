#Q2
'''
import turtle

x=turtle.Turtle()   #객체생성-빨간 거북이
x.shape('turtle')
x.shapesize(3)
x.color('red')

x.forward(100)
x.right(90)
x.forward(100)

y=turtle.Turtle()   #객체생성-파란 거북
y.shape('turtle')
y.shapesize(3)
y.color('blue')

y.left(90)
y.forward(100)
y.right(90)
y.forward(100)
'''
#Q3
'''
import turtle

x=turtle.Turtle()
x.shape('turtle')
x.shapesize(3)

x.forward(100)
x.left(120)
x.forward(100)
x.left(120)
x.forward(100)
'''
#Q4
'''
import turtle

x=turtle.Turtle()
x.shape('turtle')
x.shapesize(3)

for i in range(3):
    x.forward(100)
    x.left(120)
'''
#Q5
'''
import turtle

n=int(turtle.textinput('다각형','몇각형?'))
d=180*(n-2)/n

x=turtle.Turtle()
x.shape('turtle')
x.shapesize(3)

for i in range(n):
    x.forward(100)
    x.left(180-d)   #180-d=360/n
'''
#위치 이동 후 삼각형 그리기
'''
import turtle
y=turtle.Turtle()
y.pencolor('gold')
y.speed('slowest')
y.penup()
y.goto(-200,-200)
y.left(90)
y.pendown()
y.width(10)
y.forward(100)
y.left(120)
y.forward(100)
y.left(120)
y.forward(100)
'''
#Q6
'''
import turtle
a=turtle.Turtle()
a.color('red')
a.shape('turtle')

a.circle(100)
a.forward(200)
a.circle(100)
'''
#Q7
'''
import random
import turtle

x=turtle.Turtle()
x.shape('turtle')

for i in range(10):
    l=int(random.randint(1,100))
    d=int(random.randint(0,360))
    
    x.forward(l)
    x.left(d)
'''
#Q8
import turtle
import random

t=[]
for i in range(10):
    i=turtle.Turtle()
    i.shape('turtle')
    t.append(i)

for x in t:
    for j in range(10):
        l=int(random.randint(1,100))
        d=int(random.randint(0,360))
        
        x.penup()
        x.forward(l)
        x.left(d)
