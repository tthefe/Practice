#4장
#if~else문을 이용하여 짝홀수 판별하기
'''
def even_odd(n):
    if n%2==0:
        print('%d is an even number'%n)
    else:
        print('%d is an odd number'%n)
num=int(input('Enter the number:'))
even_odd(num)
'''
#if else를 이용하여 2개의 숫자를 입력 받아 최대값을 구하고 출력
#전달인자, 함수 안 출력
'''
def cal_max(a,b):
    if a>b:
        max=a
    else:
        max=b
    print('The mazimum value is %d'%max)
num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))
cal_max(num1,num2)
'''
#전달인자x, 함수 안 출력
'''
def cal_max():
    if a>b:
        max=a
    else:
        max=b
    print('The mazimum value is %d'%max)
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
cal_max()'''
#if else를 이용하여 2개의 숫자를 입력 받아 최댓값을 구하고 출력
#전달인자, 함수 밖 출력
'''
def cal_max(a,b):
    if a>b:
        max=a
    else:
        max=b
    return max
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
x=cal_max(a,b)
print('The mazimum value is %d'%x)
'''
#전달인자x, 함수 밖 출력
'''
def cal_max():
    if a>b:
        max=a
    else:
        max=b
    return max
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
x=cal_max()
print('The mazimum value is %d'%x)
'''
#problem 4
#4-1)
'''
def multiple1():
    if a%2==0 and a%3==0:
        print('yes')
    else:
        print('no')
a=int(input('enter the number:'))
multiple1()
'''
#4-2)
'''
def multiple2(a):
    if a%2==0 and a%3==0:
        print('yes')
    else:
        print('no')
num=int(input('enter the number:'))
multiple2(num)
'''
#5
'''
def one_to_ten_sum():
    total=0
    for i in range(1,11):
        total=total+i
    print('The sum is %d'%total)
one_to_ten_sum()
'''
#6
'''
def gugudan(a):
    for i in range(1,10):
        print('%d*%d=%d'%(a,i,a*i))
    return
dan=int(input('원하는 단을 입력하세요:'))
gugudan(dan)
'''
#7
'''
def any_sum(a,b):
    total=0
    for i in range(a,b+1):
        total=total+i
    return total                #return 다음에 돌려받을 값 적는 것 잊지 말기!!!!
start=int(input('시작값 입력:'))
end=int(input('끝값 입력:'))
x=any_sum(start,end)
print('합은 %d'%x)
'''





def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        
n=int(input('n을 입력하세요:'))
for i in range(1,n+1):
    print(fib(i))
