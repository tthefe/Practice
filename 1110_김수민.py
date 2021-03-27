'''
import math
import turtle
a=math.pi   #모듈.파이(3.14)->math 모듈에 pi라는 값이 지정되어 있다.

t=turtle.Turtle()

t.shape('turtle')
t.pencolor('red')
t.width(3)

def d2r(value):
    radian=a*value/180
    return radian

for degree in range(360):
    pos=math.sin(d2r(degree))*100   #*100은 최댓값을 증폭하는 역할
    t.goto(degree,pos)
'''

result=0

def add(num):
    global result   #전역변수 사
    result=result+num
    return result
