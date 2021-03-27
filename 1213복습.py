#p.224 나혼자 코딩
'''
try:
    a=[1,2,3]
    b=[0,1,2]
    a[2]/b[3]
except IndexError as e:
    print(e)
'''

'''
print('Hello!')
try:
    age=int(input("Enter your age:"))
    print('You are %d years old'%age)
except:
    print('You entered the wrong number!')
print('Anyway, nice to meet you!')
'''
'''
print('Hello!')
try:
    age=int(input("Enter your age:"))
    print('You are %d years old'%age)
except ValueError:
    print('You entered the wrong number!')
print('Anyway, nice to meet you!')
'''
'''
print('Hello!')
try:
    age=int(input("Enter your age:"))
    print('You are %d years old'%age)
except ValueError as e:
    print(e)
print('Anyway, nice to meet you!')
'''
'''
try:
    a=[1,2]
    print(a[3])
    4/0
except (ZeroDivisionError,IndexError) as e:
    print(e)
'''
'''
class Calculator:
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result+=num
        return self.result

    def sub(self,num):
        self.result-=num
        return self.result

cal1=Calculator()
cal2=Calculator()
'''

#사칙연산 클레스
'''
class FourCal:
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
    def div(self):
        result=self.first/self.second
        return sesult

a=FourCal(4,2)
'''
#Problem
#실행결과에서 None이 나오는 이유?????????
'''
def Add(num1,num2):
    print('%d+%d=%d'%(int(num1),int(num2),int(num1)+int(num2)))
def Sub(num1,num2):
    print('%d-%d=%d'%(int(num1),int(num2),int(num1)-int(num2)))
def Mul(num1,num2):
    print('%d*%d=%d'%(int(num1),int(num2),int(num1)*int(num2)))
def Div(num1,num2):
    try:
        print('%d/%d=%f'%(int(num1),int(num2),int(num1)/int(num2)))
    except ZeroDivisionError:
        print('0으로 나누기를 시도하여 종료합니다.')

def Calculator(num1,operator,num2):
    if operator=='+':
        print(Add(num1,num2))
    elif operator=='-':
        print(Sub(num1,num2))
    elif operator=='*':
        print(Mul(num1,num2))
    elif operator=='/':
        print(Div(num1,num2))
        
num1=input('첫번째 정수 입력: ')
operator=input('연산자 입력(+,-,*,/): ')
num2=input('두번째 정수 입력: ')
Calculator(num1,operator,num2)
'''



#연습문제
#Q1
'''
class Calculator:
    def __init__(self):
        self.value=0

    def add(self,val):
        self.value+=val
        return self.value
    def minus(self,val):
        self.value-=val
        return self.value
cal=Calculator()
'''
#Q6
'''
print(list(map(lambda a:a*3, [1,2,3,4])))


def three(x):
    return x*3
print(list(map(three,[1,2,3,4])))
'''
#Q13
'''
import random

number=[]
num=1
for i in range(45):
    number.append(num)
    num+=1
print(random.sample(number,k=6))
'''
#Q13
def DashInsert(string):
    num=[]
    for s in string:
        num.append(int(s))

    N=[]
    for n in num:
        Nu=n%2
        N.append(Nu)
        for i in range(len(num)):
            if N[i]==N[i+1]:
                if N[i]==0:
                    print('num[i]*',end='')
                else:
                    print('num[i]-',end='')
            else:
                print('num[i]',end='')
        if num[-1]:
            print('num[i]')
string=input('a= ')
DashInsert(string)
