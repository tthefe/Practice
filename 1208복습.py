#5장 모듈 응용1
#p.4Q
'''
import math

l=int(input('거리: '))
d=int(input('각도: '))
D=math.radians(d)

h=l*math.tan(D)

print('건물의 높이는 %f입니다'%h)
'''
#p.5
#1
'''
import math
import turtle

a=math.pi

t=turtle.Turtle()

t.shape('classic')
t.pencolor('red')
t.width(3)

depth=200
for degree in range(360):
    radian=a*degree/180
    position=math.sin(radian)*depth
    t.goto(degree,position)
'''
#2
'''
import math
import turtle

t=turtle.Turtle()

t.shape('classic')
t.pencolor('red')
t.width(3)

depth=200
for degree in range(360):
    radian=math.radians(degree)
    position=math.sin(radian)*depth
    t.goto(degree,position)
'''
#p.11
'''
import random
a=random.sample([1,2,3,4,5,6],k=2)
print(a)
'''
#p.12 파이 시뮬레이션
'''
import random as r
import math as m

total=10000
inside=0

for i in range(0,total):
    x=r.random()**2
    y=r.random()**2

    if m.sqrt(x+y)<1.0:
        inside+=1

pi=(inside/total)*4

print('When n is %d, pi~%f'%(total,pi))    
'''
#p.13
'''
from random import choice

x=['head','tail']

while True:
    a=input('Toss the coin(y,n) ')
    if a=='y':
        print(choice(x))
    else:
        break
'''
#p.14
'''
import random

me=int(input('가위는 1, 바위는 2, 보는 3: '))

win=0
draw=0

while True:
    if 1>me or me>3:
        print('잘못 입력하셨습니다')
        continue

    else:
        com=random.choice([1,2,3])

        if me==1:
            print('당신은 가위를 냈습니다')

            if com==1:
                print('컴퓨터는 가위를 냈습니다')
                draw+=1
                print('=============================')
                print('draw')
            elif com==2:
                print('컴퓨터는 바위를 냈습니다')
                print('=============================')
                print('You lose.The game is terminated \n Game score: %d wins %d draws 1loses'%(win,draw)) 
                break
            else:
                print('컴퓨터는 보를 냈습니다')
                win+=1
                print('=============================')
                print('You win')
                
        if me==2:
            print('당신은 바위를 냈습니다')

            if com==1:
                print('컴퓨터는 가위를 냈습니다')
                win+=1
                print('=============================')
                print('You win')
            elif com==2:
                print('컴퓨터는 바위를 냈습니다')
                draw+=1
                print('=============================')
                print('Draw')
            else:
                print('컴퓨터는 보를 냈습니다')
                print('=============================')
                print('You lose.The game is terminated \n Game score: %d wins %d draws 1loses'%(win,draw)) 
                break

        if me==3:
            print('당신은 보를 냈습니다')

            if com==1:
                print('컴퓨터는 가위를 냈습니다')
                print('=============================')
                print('You lose.The game is terminated \n Game score: %d wins %d draws 1loses'%(win,draw)) 
                break
            elif com==2:
                print('컴퓨터는 바위를 냈습니다')
                win+=1
                print('=============================')
                print('You win')
            else:
                print('컴퓨터는 보를 냈습니다')
                draw+=1
                print('=============================')
                print('Draw')
'''   #다시 풀어보기
#p.18
'''
import time
start=time.time()
total=0
for i in range(1,101):
    total+=i
end=time.time()
print(end-start)
print(total)
'''
#p.19
'''
import timeit
start=timeit.default_timer()
total=0
for i in range(1,1000001):
    total+=i
end=timeit.default_timer()
print(end-start)
print(total)
'''


#6장 모듈 응용2
#p.2
'''
import turtle
x=turtle.Turtle()
x.shape('turtle')
x.width(5)
x.shapesize(5)
x.color('gold')

x.forward(100)
x.left(90)
x.forward(100)
x.left(90)
x.forward(100)
x.left(90)
x.forward(100)

x.reset()
'''
#Q1
'''
import turtle
l=int(input('정사각형의 한 변의 길이를 입력하시오: '))

x=turtle.Turtle()
x.shape('turtle')

for i in range(4):
    x.forward(l)
    x.left(90)
'''

'''
import turtle

x=turtle.Turtle()
x.shape('turtle')
x.shapesize(3)

l=int(turtle.textinput('정사각형','길이: '))

for i in range(4):
    x.forward(l)
    x.left(90)
'''
#Q2
'''
import turtle

t1=turtle.Turtle()
t1.shape('turtle')
t1.shapesize(3)
t1.color('blue')

t1.left(90)
t1.forward(100)
t1.right(90)
t1.forward(100)

t2=turtle.Turtle()
t2.shape('turtle')
t2.shapesize(3)
t2.color('red')

t2.forward(100)
t2.right(90)
t2.forward(100)
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
d=180*(n-2)/n

x=turtle.Turtle()
x.shape('turtle')
x.shapesize(3)

for i in range(n):
    x.forward(100)
    x.left(180-d)
'''
#p.7
'''
import turtle
a=turtle.Turtle()

a.pencolor('green')
a.speed('slowest')
a.width(5)

a.penup()   #이동할 때 선을 그리지 않음
a.goto(-100,-100)   #원하는 좌표로 이동
a.pendown()   #이동할 때 선을 그림

a.left(90)
a.forward(100)
a.left(120)
a.forward(100)
a.left(120)
a.forward(100)
'''
#Q6
'''
import turtle
x=turtle.Turtle()
x.shape('turtle')
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

for i in range(10):
    l=random.randint(1,100)
    x.forward(l)
    d=random.randint(0,360)
    x.left(d)
'''
#Q8
'''
import turtle
import random

t=[]
for i in range(5):
    i=turtle.Turtle()
    i.shape('turtle')
    t.append(i)

for T in t:
    for j in range(10):

        l=random.randint(1,100)
        d=random.randint(0,360)

        T.penup()
        T.speed('fastest')
        T.forward(l)
        T.left(d)
'''
#Q9

import turtle
import random

t=[]
for i in range(5):
    i=turtle.Turtle()
    i.shape('turtle')
    t.append(i)

colors=['red','green','yellow','blue','black']
n=0

for T in t:
    T.color(colors[n])
    n+=1
    
    for j in range(10):
        l=random.randint(1,100)
        d=random.randint(0,360)

        T.forward(l)
        T.left(d)

#p.15
'''
import matplotlib.pyplot as plt
plt.hist([1,1,2,3,4,5,6,6,7,8,10])
plt.show()
'''
#p.16
'''
import matplotlib.pyplot as plt

f=open('D:/score.txt', 'r')
n=f.readlines()

N=[]
total=0
for i in n:
    I=int(i)
    total+=I
    N.append(I)
m=total/len(n)
print(m)

v=0
for j in n:
    v+=(int(j)-m)**2
a=pow(v/len(n),0.5)
print(a)

f.close()

plt.hist(N)   #숫자형태의 리스트가 필요
plt.show()
'''
#p.17
'''
import matplotlib.pyplot as plt
import random

n=100
dice=[]
for i in range(n):
    dice.append(random.randint(1,6))
print(dice)

plt.hist(dice,bins=6)
plt.show()
'''
