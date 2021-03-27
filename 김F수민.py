#나는 정직하게 시험에 응할 것을 서약합니다.(김수민)


#12201284 김수민
#1
'''
def convert(string):
    s=[]
    for i in string:
        s.append(i)

    total=0
    for x in s:
        if ord('A')<=ord(x)<=ord('Z'):
            score=ord(x)-ord('A')+1
            total+=score
        elif ord('a')<=ord(x)<=ord('z'):
            score=ord(x)-ord('a')+1
            total+=score
    print('%s:%d'%(string,total))

while True:
    string=input('문자열을 입력하시오: ')
    if string=='!':
        break
    convert(string)
'''
#12201284 김수민
#2
'''
class CalBMI:
    def __init__(self,h,w):
        self.h=h
        self.w=w
    def BMI(self):
        H=int(self.h)/100
        bmi=int(self.w)/H**2
        
        if bmi>=30.0:
            print ('BMI=%f:고도비만'%(bmi))
        elif bmi>=25.0:
            print ('BMI=%f:비만'%(bmi))
        elif bmi>=23.0:
            print ('BMI=%f:과체중'%(bmi))
        elif bmi>=18.5:
            print ('BMI=%f:표준체중'%(bmi))
        else:
            print ('BMI=%f:체중미달'%(bmi))
a=CalBMI(180,70)
b=CalBMI(170,90)
a.BMI()
b.BMI()
'''
#12201284 김수민
#3
'''
import random
def getUser():
    me=int(input('가위는 1, 바위는 2, 보는 3: '))
    if me==1:
        print('당신은 가위를 선택했습니다.')
        return 1
    elif me==2:
        print('당신은 바위를 선택했습니다.')
        return 2
    elif me==3:
        print('당신은 보를 선택했습니다.')
        return 3
def getCom():
    com=int(random.choice([1,2,3]))
    if com==1:
        print('컴퓨터는 가위를 선택했습니다.')
        return 1
    elif com==2:
        print('컴퓨터는 바위를 선택했습니다.')
        return 2
    elif com==3:
        print('컴퓨터는 보를 선택했습니다.')
        return 3
def getResult(user,com):
    if user==com:
        print('===========')
        print('Draw')
        return 0
    elif user==1:
        if com==2:
            print('===========')
            print('You lose.The game is terminated')
            return -1
        elif com==3:
            print('===========')
            print('You win')
            return 1
    elif user==2:
        if com==3:
            print('===========')
            print('You lose.The game is terminated')
            return -1
        elif com==1:
            print('===========')
            print('You win')
            return 1
    elif user==3:
        if com==1:
            print('===========')
            print('You lose.The game is terminated')
            return -1
        elif com==2:
            print('===========')
            print('You win')
            return 1

win=0
lose=0
draw=0
while True:
    user=getUser()
    if 3<user or user<1:
        print('잘못 입력하셨습니다')
        continue
    com=getCom()
    result=getResult(user,com)
    if result==1:
        win=win+1
    elif result==0:
        draw=draw+1
    elif result==-1:
        lose=lose+1
        break
print('Game Score:%d wins %d draws %d loses'%(win,draw,lose))
'''

#12201284 김수민
#4

import random
import math

def pisim(total):
    
    inside=0
    for i in range(total):
        x2=(random.randrange(-1,1)+random.random())**2
        y2=(random.randrange(-1,1)+random.random())**2
        if math.sqrt(x2+y2)<1.0:
            inside+=1
    pi=(inside/total)
    e=pi-math.pi

    return e

while True:
    total=int(input('점의 개수를 입력하시오:'))
    if total==0:
        print('시뮬레이션을 중단합니다.')
        break
    E=pisim(total)
    print('n=%d:error=%f'%(total,E))

#!2201284 김수민
#5
'''
import turtle
import random

tur=int(input('거북이 갯수: '))
time=int(input('임의의 거리와 방향으로 이동할 횟수: '))

for i in range(tur):
    x=turtle.Turtle()
    x.shape('turtle')

    for k in range(time):
        l=random.randint(1,150)
        d=random.randint(0,360)
        x.forward(l)
        x.left(d)
'''
#12201284 김수민
#6
'''
import random
import numpy as np
def dice_prob(time):
    try:
        for i in range(time):
            x=random.choice([1,2,3,4,5,6])
        print('3이 나올 확률:%f'%(np.count_nonzero(x==3)/time))
    except ZeroDivisionError:
        print('division by zero')
    finally:
        print('기말고사 보느라 수고 많았습니다.')
        
time=int(input('주사위를 던질 횟수: '))
dice_prob(time)
'''
