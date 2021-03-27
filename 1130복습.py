#05-1 클래스는 왜 필요한가?
'''
result1=0
result2=0

def add1(num):
    global result1
    result1+=num
    return result1

def add2(num):
    global result2
    result2+=num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))
'''
'''
class Calculator:
    def __init__(self):
        self.result=0

    def add(self, num):
        self.result+=num
        return self.result

    def sub(self, num):
        self.result-=num
        return self.result

cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal2.sub(5))
'''
#사칙연산 클래스 만들기
'''
>>> class FourCal:
	pass

>>> a=FourCal()
>>> type(a)
<class '__main__.FourCal'>   #a가 FourCal 클래스의 객체
>>>
'''

#5장 Problem
'''
def Add(num1,num2):
    result=num1+num2
    print('%d+%d=%d'%(num1,num2,result))

def Sub(num1,num2):
    result=num-num2
    print('%d-%d=%d'%(num1,num2,result))

def Mul(num,num2):
    result=num*num2
    print('%d*%d=%d'%(num1,num2,result))

def Div(num,num2):
    try:
        result=num/num2
        print('%d/%d=%d'%(num1,num2,result))
    except ZeroDivisionError:
        print('0으로 나누기를 시도하여 종료합니다.')

def Calculator(n1,o,n2):
    if o=='+':
        Add(n1,n2)
    elif o=='-':
        Sub(n1,n2)
    elif o=='*':
        Mul(n1,n2)
    else:
        Div(n1,n2)

num1=int(input('첫번째 정수 입력:'))
operator=input('연산자 입력(+,-,*,/):')
num2=int(input('두번째 정수 입력:'))
Calculator(num1,operator,num2)
'''
#05-4 오류 예외 처리 기법 나 혼자 코딩
'''
i=[1,5]
try:
    print(i[5])
except IndexError as a:
    print(a)
'''
#6장 p.2
'''
import math
r=float(input('원의 반지름을 입력하세요:'))
l=2*math.pi*r
s=math.pi*r**2
print('반지름 %f인 원의 둘레는 %f'%(r,l))
print('반지름 %f인 원의 넓이는 %f'%(r,s))
'''
#6장 p.4
import math

l=int(input('거리:'))
d=float(input('각도:'))

r=math.radians(d)
h=math.tan(r)*l
print(h)
