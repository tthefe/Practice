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
'''
from random import choice

win=0
lose=0
draw=0

while True:
    u=int(input('가위는 1, 바위는 2, 보는 3: '))
    if u<1 or u>3:
        print('잘 못 입력하셨습니다')
        continue
    elif u==1:
        print('당신은 가위를 냈습니다')
    elif u==2:
        print('당신은 바위를 냈습니다')
    else:
        print('당신은 보를 냈습니다')

        com=choice([1,2,3])
        if com==1:
            print('컴퓨터는 가위를 냈습니다')
        elif com==2:
            print('컴퓨터는 바위를 냈습니다')
        else:
            print('컴퓨터는 보를 냈습니다')

    if u==com:
        print('===================')
        print('draw')
        result=0
    elif u==1 and com==3:
        print('===================')
        print('draw')
        result=0
    elif u==2 and com==1:
        print('===================')
        print('draw')
        result=0
    elif u==3 and com==2:
        print('===================')
        print('draw')
        result=0
    elif u==1 and com==2:
        print('===================')
        print('You lose. The game is terminated')
        result=-1
    elif u==2 and com==3:
        print('===================')
        print('You lose. The game is terminated')
        result=-1
    elif u==3 and com==1:
        print('===================')
        print('You lose. The game is terminated')
        result=-1

    if result==1:
        win+=win
    elif result==0:
        draw+=draw
    else:
        lose+=lose
        break
print('Game Score:%d wins %d draws %d loses'%(win, draw, lose))
'''
'''
import time
print('지금부터 5초 동안 정지합니다')
time.sleep(5)
print('프로그램을 종료합니다')

for i in range(10,0,-1):
    print(i, end=' ')
    time.sleep(1)
print('발사!')
'''
'''
import time

start=time.time()
for i in range(100):
    print(i+1)
end=time.time()
print(end-start)
print('프로그램을 종료합니다')
'''
'''
import timeit
start=timeit.default_timer()
total=0
for i in range(1,10001):
    total+=i
end=timeit.default_timer()
print(end-start)
print(total)
'''
#7장 Q1
import turtle

x=turtle.Turtle()   #객체생성
x.shape('turtle')   #함수호출

l=int(turtle.textinput('정사각형','길이'))

for i in range(4):
    x.forward(l)
    x.left(90)
