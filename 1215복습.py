'''
class Calculator:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def dib(self):
        result=self.first/self.second
        return result
'''
#Problem
'''
def Add(n1,n2):
    result=int(n1)+int(n2)
    if int(n2)>=0:
        print('%s+%s=%d'%(n1,n2,result))
    else:
        print('%s+(%s)=%d'%(n1,n2,result))
def Sub(n1,n2):
    result=int(n1)-int(n2)
    if int(n2)>=0:
        print('%s-%s=%d'%(n1,n2,result))
    else:
        print('%s-(%s)=%d'%(n1,n2,result))
def Mul(n1,n2):
    result=int(n1)*int(n2)
    if int(n2)>=0:
        print('%s*%s=%d'%(n1,n2,result))
    else:
        print('%s*(%s)=%d'%(n1,n2,result))
def Div(n1,n2):
    try:
        result=int(n1)/int(n2)
        if int(n2)>=0:
            print('%s/%s=%f'%(n1,n2,result))
        else:
            print('%s/(%s)=%f'%(n1,n2,result))
    except ZeroDivisionError:
        print('0으로 나누기를 시도하여 종료합니다.')

def Calculator(n1,operator,n2):
    if operator=='+':
        Add(n1,n2)
    elif operator=='-':
        Sub(n1,n2)
    elif operator=='*':
        Mul(n1,n2)
    elif operator=='/':
        Div(n1,n2)

num1=input('첫번째 정수 입력: ')
operator=input('연산자 입력(+,-,*,/): ')
num2=input('두번째 정수 입력: ')
Calculator(num1,operator,num2)
'''
#Q6
'''
import turtle
x=turtle.Turtle()
x.circle(100)
'''
#Q7,#Q8
'''
import turtle
import random

Turtle=[]
for i in range(5):
    x=turtle.Turtle()
    x.shape('turtle')
    Turtle.append(x)

for t in Turtle:
    for j in range(10):
        l=random.randint(1,100)
        d=random.randint(0,360)

        t.penup()
        t.forward(l)
        t.left(d)
'''
#Q9
'''
import turtle
import random

Tur=[]
for i in range(5):
    x=turtle.Turtle()
    x.shape('turtle')
    Tur.append(x)

C=['red','green','yellow','blue','black']

c=0
for t in Tur:
    t.color(C[c])
    c+=1
    for j in range(10):
        l=random.randint(1,100)
        d=random.randint(0,360)

        t.forward(l)
        t.left(d)
'''


'''
import turtle
import math
a=math.pi

t1=turtle.Turtle()
t2=turtle.Turtle()

t1.shape('turtle')
t1.pencolor('red')
t1.width(5)

t2.shape('arrow')
t2.pencolor('gold')
t2.width(5)
t2.penup()
t2.goto(0,100)
t2.pendown()

def d2r(value):
    radian=math.radians(value)
    return radian

for degree in range(360):
    pos1=math.sin(d2r(degree))*100
    pos2=math.cos(d2r(degree))*100
    t1.goto(degree,pos1)
    t2.goto(degree,pos2)
'''
'''
import matplotlib.pyplot as plt
plt.hist([1,1,2,3,4,5,6,6,7,8,10],bins=2)
plt.show()
'''
#Q
'''
import matplotlib.pyplot as plt

f=open('D:/score.txt','r')
line=f.readlines()

score=[]
for s in line:
    score.append(int(s))
f.close()

total=0
for i in score:
    total+=i
mean=total/len(score)
print(mean)

total1=0
for j in score:
    total1+=(j-mean)**2
var=total1/len(score)
print(var)

plt.hist(score,bins=5)
plt.show()
'''
#주사위 던지기 시뮬레이션
'''
import matplotlib.pyplot as plt
import random

dice=[]
for i in range(1000):
    d=random.choice([1,2,3,4,5,6])
    dice.append(d)
print(dice)

plt.hist(dice,bins=6)
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

dice=np.random.randint(1,7,100)

plt.hist(dice,bins=6)
plt.show()
'''
#QUIZ5
#2
'''
def any_start(start,stop):
    total=0
    for i in range(start,stop+1):
        total+=i
    mean=total/(stop-start+1)

    total1=0
    for j in range(start,stop+1):
        total1+=(j-mean)**2
    var=total1/(stop-start+1)

    return ('Mean: %f\nVariance: %f'%(mean,var))

start=int(input('시작값 입력: '))
stop=int(input('끝값 입력: '))
f=open('D:/start.txt','w')
f.write(any_start(start,stop))
f.close()
'''
#1
'''
f=open('D:/sample1.txt','w')
for i in range(1,11):
    f.write('%d\n'%(i%7))
f.close()

f=open('D:/sample1.txt','r')
line=f.readlines()
s=[]
for l in line:
    s.append(int(l))
total=0
for S in s:
    total+=S
mean=total/len(s)
f.close()

f=open('D:/result.txt','w')
f.write('Mean=%f'%mean)
f.close()
'''

#Q13
'''
import random

n=[]
for i in range(1,46):
    n.append(int(i))

print(random.sample(n,k=6))
'''
'''
class Calculator:
    def __init__(self,List):
        self.List=List
        
    def sum(self):
        N=[]
        for i in self.List:
            N.append(int(i))

        total=0
        for n in N:
            total+=n
        return total
    def avg(self):
        N=[]
        for i in self.List:
            N.append(int(i))
            
        total=0
        for n in N:
            total+=n
        avg=total/len(N)
        return avg
'''

