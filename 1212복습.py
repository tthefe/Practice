'''
import math

r=float(input('원의 반지름을 입력하세요: '))

l=2*r*math.pi
s=math.pi*pow(r,2)

print('반지름 %f인 원의 둘레는 %f'%(r,l))
print('반지름 %f인 원의 넓이는 %f'%(r,s))
'''
'''
import math

l=int(input('거리: '))
d=int(input('각도: '))

r=math.radians(d)
h=l*math.tan(r)

print('건물의 높이는 %f입니다'%h)
'''
'''
import math
import turtle

t=turtle.Turtle()

t.penup()
t.goto(-300,0)

t.pendown()
t.shape('turtle')
t.color('gold')
t.width(5)

for degree in range(720):
    radian=math.radians(degree)
    position=math.sin(radian)*200
    t.goto(degree-300,position)
'''
'''
import random
a=random.randint(1,6)
b=random.randrange(1,7)
c=random.randrange(1,7,1)
d=random.choice([1,2,3,4,5,6])
e=random.sample([1,2,3,4,5,6],k=1)

print(a,b,c,d,e)
'''
#파이 시뮬레이션
'''
import random
import math

total=100000000
inside=0

for i in range(0,total):
    x=random.random()**2
    y=random.random()**2
    if math.sqrt(x+y)<1.0:
        inside+=1

pi=(inside/total)*4

print('when n is %d, pi~%f'%(total,pi))
'''
#동전 던지기 게임
'''
import random

while True:
    a=input('Toss the coin(y,n) ')
    if a=='y':
        print(random.choice(['head','tail']))
    else:
        break
'''
#가위 바위 보 게임

import random

win=0
draw=0

while True:
    me=int(input('가위는 1, 바위는 2, 보는 3: '))
    if me<=0 or me>=4:
        print('잘못 입력하셨습니다.')
        continue
    computer=random.choice([1,2,3])

    if me==computer:
        if me==3:
            print('당신은 보를 냈습니다 \n컴퓨터는 보를 냈습니다')
            print('============================')
            print('Draw')
            draw+=1
        elif me==2:
            print('당신은 바위를 냈습니다 \n컴퓨터는 바위를 냈습니다')
            print('============================')
            draw+=1
            print('Draw')
        elif me==1:
            print('당신은 가위를 냈습니다 \n컴퓨터는 가위를 냈습니다')
            print('============================')
            draw+=1
            print('Draw')

    elif me==1:
        if computer==2:
            print('당신은 가위를 냈습니다 \n컴퓨터는 바위를 냈습니다')
            print('============================')
            break
        elif computer==3:
            print('당신은 가위를 냈습니다 \n컴퓨터는 보를 냈습니다')
            print('============================')
            win+=1
            print('You win')

    elif me==2:
        if computer==3:
            print('당신은 바위를 냈습니다 \n컴퓨터는 보를 냈습니다')
            print('============================')
            break
        elif computer==1:
            print('당신은 바위를 냈습니다 \n컴퓨터는 가위를 냈습니다')
            print('============================')
            win+=1
            print('You win')

    elif me==3:
        if computer==1:
            print('당신은 보를 냈습니다 \n컴퓨터는 가위를 냈습니다')
            print('============================')
            break
        elif computer==2:
            print('당신은 보를 냈습니다 \n컴퓨터는 바위를 냈습니다')
            print('============================')
            win+=1
            print('You win')

print('You lose.The game is terminated')
print('Game score: %d wins %d draws 1loses'%(win,draw))

#7장Q1
'''
import turtle
l=int(input('한 변의 길이 입력:'))

x=turtle.Turtle()

for i in range(4):
    x.forward(l)
    x.left(90)
'''
'''
import turtle

x=turtle.Turtle()
l=int(turtle.textinput('정사각형','길이'))

for i in range(4):
    x.forward(l)
    x.left(90)
'''
#Q2
'''
import turtle

r=turtle.Turtle()
r.shape('turtle')
r.color('red')
r.shapesize(3)
r.width(3)

r.forward(150)
r.right(90)
r.forward(150)

b=turtle.Turtle()
b.shape('turtle')
b.color('blue')
b.shapesize(3)
b.width(3)

b.left(90)
b.forward(150)
b.right(90)
b.forward(150)
'''
#Q3,Q4
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

x=turtle.Turtle()
x.shape('turtle')
x.shapesize(3)
x.width(3)

for i in range(n):
    x.forward(100)
    x.left(180-(180*(n-2)/n))
'''
#Q6
'''
import turtle

x=turtle.Turtle()
x.shape('turtle')
x.shapesize(3)
x.color('red')

x.circle(100)
x.forward(200)
x.circle(100)
'''
#Q7
'''
import turtle
import random

x=turtle.Turtle()
x.shape('turtle')
x.speed('fastest')

for i in range(10):
    l=random.randint(1,100)
    d=random.randint(0,360)

    x.forward(l)
    x.left(d)
'''
#Q8
'''
import turtle
import random

T=[]

for i in range(5):
    a=turtle.Turtle()
    T.append(a)

for a in T:
    for j in range(10):
        l=random.randint(1,100)
        d=random.randint(0,360)

        a.shape('turtle')
        a.penup()
        a.forward(l)
        a.left(d)
'''
#Q9
'''
import turtle
import random

T=[]

for i in range(5):
    i=turtle.Turtle()
    i.shape('turtle')
    i.shapesize(2)
    i.width(2)
    T.append(i)

c=['red','green','yellow','blue','black']

k=0
for a in T:
    a.color(c[k])
    k+=1
    
    for j in range(10):
        l=random.randint(1,100)
        d=random.randint(0,360)

        a.forward(l)
        a.left(d)
'''
#Q
'''
import math
import matplotlib.pyplot as plt

f=open('D:/score.txt','r')
score=f.readlines()

total=0
for s in score:
    total+=int(s)
mean=total/len(score)
print(mean)

total1=0
for n in score:
    v=pow((int(n)-mean),2)
    total1+=v
V=v/len(score)
a=math.sqrt(V)
print(a)

f.close()

plt.hist(score,bins=5)
plt.show()
'''
'''
from math import sqrt
import matplotlib.pyplot as plt

f=open('D:/score.txt','r')
line=f.readlines()

score=[]
total=0
for i in line:
    n=float(i)
    total+=n
    score.append(n)
mean=total/len(line)
print(mean)

total1=0
for j in range(len(score)):
    total1+=(score[j]-mean)**2
a=sqrt(total1/len(score))
print(a)

f.close()

plt.hist(score,bins=5)
plt.show()
'''
