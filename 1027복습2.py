#연습용문제
#파일 입출력
'''
f=open('D:/sample.txt','w')
for i in range(1,11):
    j=i%7
    f.write('%d\n'%j)
f.close()

f1=open('D:/sample.txt','r')
a=f1.readlines()
total=0
for a1 in a:
    total=total+int(a1)
average=total/10
print(average)
f1.close()

f2=open('D:/sample.txt','w')
f2.write(str(average))
f2.close()
'''

#반복문
'''
while True:
    word=input('영어 단어: ')
    if word=='!':
        print('프로그램을 종료합니다.')
        break
    else:
        total=0
        for i in word:
            if 'A'<=i<='Z':
                j=ord(i)-ord('A')+1
            elif 'a'<=i<='z':
                j=ord(i)-ord('a')+1
            total=total+j
        print(total)
'''
#함수1
'''
def coord(d,m=0,s=0):
    x=d+m/60+s/3600
    print('%d도 %d분 %d초는 %f도입니다.'%(d,m,s,x))
'''
#함수2
'''
n=int(input('원하는 자료 개수를 입력하세요:'))

def data(n1):
    a1=[]
    for i in range(1,n+1):
        j=int(input('%d번째 자료 값을 입력하세요:'%i))
        a1.append(j)
    return a1
a=data(n)
print(a)

def sorting(b1):
    b1.sort()
    return b1
b=sorting(a)
print(b)

def output(c1):
    print(c1)
output(b)
'''
#함수3
'''
while True:
    print('*'*50)
    a=int(input('첫번째 복소수의 실수부를 입력하세요:'))
    b=int(input('첫번째 복소수의 허수부를 입력하세요:'))
    c=int(input('두번째 복소수의 실수부를 입력하세요:'))
    d=int(input('두번째 복소수의 허수부를 입력하세요:'))

    if a==0 and b==0:
        break

    def complex_print(a,b,c,d):
        if b>=0:
            print('첫번째 복소수:%d+%di'%(a,b))
        else:
            print('첫번째 복소수:%d%di'%(a,b))
            
        if d>0:
            print('두번째 복소수:%d+%di'%(c,d))
        else:
            print('두번째 복소수:%d%di'%(c,d))
    complex_print(a,b,c,d)

    def complex_add(a,b,c,d):
        if b+d>0:
            print('복소수 덧셈:%d+%di'%(a+c,b+d))
        else:
            print('복소수 덧셈:%d%di'%(a+c,b+d))
    complex_add(a,b,c,d)

    def complex_mul(a,b,c,d):
        if b*c+a*d>0:
            print('복소수 곱셈:%d+%d'%((a*c-b*d),(b*c+a*d)))
        else:
            print('복소수 곱셈:%d%di'%((a*c-b*d),(b*c+a*d)))
    complex_mul(a,b,c,d)
'''
#제어문 문제
#1
'''
a=int(input('시작값 입력:'))
b=int(input('끝값 입력:'))
total=0
for i in range(a,b+1):
    total=total+i
print(total)
'''
#2
'''
n=int(input('팩토리얼을 계산할 1보다 큰 정수를 입력하시오:'))
total=1
for i in range(n,0,-1):
    total=total*i
print('%d!=%d'%(n,total))
'''
#3
'''
while True:
    print('*'*50)
    
    d=int(input('위도의 도 단위값을 정수로 입력하시오:'))
    m=int(input('위도의 분 단위값을 정수로 입력하시오:'))
    if m<0:
        print('위도의 분 값에 음수를 입력하여 종료합니다.')
        break
    s=int(input('위도의 초 단위값을 정수로 입력하시오:'))

    x=d+m/60+s/3600
    print('위도 %d도 %d분 %d초는 위도 %f도 입니다.'%(d,m,s,x))

    print('*'*50)
'''
#Quiz1
#1
'''
for i in range(5,0,-1):
    for j in range(1,i+1):
        print('*', end='')
    print('')
'''
#2
'''
while True:
    n=input('문자 하나를 입력하시오:')
    if n=='!':
        break
    print(n.upper())
'''
#3
'''
def BMI(h,w):
    bmi=w/(h/100)**2

    if bmi>=30.0:
        print('BMI=%f:고도비만입니다.'%bmi)
    elif bmi>=25.0:
        print('BMI=%f:비만입니다.'%bmi)
    elif bmi>=23.0:
        print('BMI=%f:과체중입니다.'%bmi)
    elif bmi>=18.5:
        print('BMI=%f:표준체중입니다.'%bmi)
    else:
        print('BMI=%f:체중미달입니다.'%bmi)

h=int(input('키를 cm단위로 입력하시오.:'))
w=int(input('몸무게를 kg단위로 입력하시오.:'))
BMI(h,w)
'''
#2019 Quiz
#2
'''
total=0
for i in range(91,101):
    total=total+i
mean=total/10
print('Mean is %f'%mean)

v=0
for i in range(91,101):
    v=v+(i-mean)**2
variance=v/10
print('Variance is %f'%variance)
'''
#교과서


#4장
#Q1
'''
def is_odd(number):
    if number%2==1:
        return True
    else:
        return False
''' 
#Q2
'''
def avg_numbers(*args):
    result=0
    for i in args:
        result+=i
    return result/len(args)
'''
#Q3
'''
input1=input('첫번째 숫자를 입력하세요:')
input2=input('두번째 숫자를 입력하세요:')

total=int(input1)+int(input2)
print('두 수의 합은 %d 입니다.'%total)
'''
#Q5
'''
f1=open('D:/test.txt','w')
f1.write('Life is too short')
f1.close()

f2=open('D:/test.txt','r')
print(f2.read())
f2.close()
'''
#Q6
'''
user_input=input('저장할 내용을 입력하세요:')
f=open('D:/test.txt','a')
f.write(user_input)
f.write('\n')
f.close()
'''
#Q7
'''
f=open('D:/test.txt','w')
f.write('Life is too short\nyou need java')
f.close()

f1=open('D:/test.txt','r')
body=f1.read()
f1.close()

body=body.replace('java','python')

f2=open('D:/test.txt','w')
f2.write(body)
f2.close()
'''

#3장
#Q2
'''
result=0
i=1
while i<=1000:
    i=i+1
    if i%3==0:
        result=result+i
print(result)
'''
#Q3
'''
i=0
while True:
    i=i+1
    if i>5:break
    print('*'*i)
'''
#Q4
'''
for i in range(1,101):
    print(i)
'''
#Q5
'''
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    total=total+score
average=total/10
print(average)
'''
#Q6
'''
numbers=[1,2,3,4,5]

result=[n*2 for n in numbers if n%2==1]
print(result)
'''
#코딩 면허 시험
#Q1
'''
a='a:b:c:d'
b=a.split(':')
c='#'.join(b)

print(c)
'''
#Q4
'''
A=[20,55,67,82,45,33,90,87,100,25]

total=0
for score in A:
    if score>=50:
        total=total+score
    else:pass
print(total)
'''
#Q5
'''
def fib(n):
    for i in range(1,n+1):
        if i==1:return 0
        elif i==2:return 1
        else:return fib(i-1)+fib(i-2)
n=int(input('n을 입력하시오:'))
F=fib(n)
print(F)
'''#풀다 말음

#Q6
'''
a=input('숫자를 입력하시오:')
b=a.split(',')

total=0
for i in b:
    total=total+int(i)
print(total)
'''
#Q7
'''
dan=int(input('구구단을 출력할 숫자를 입력하세요(2-9):'))
for i in range(1,10):
    print(dan*i,end=' ')
'''
#Q8
'''
f=open('D:/abe.txt','w')
f.write('AAA\nBBB\bCCC\nDDD\nEEE')
f.close()

f1=open('D:/abe.txt','r')
a=f1.readlines()
f1.close

f2=open('D:/abe.txt','w')
for i in a:
    i=i.strip()
    f2.write(i)
    f2.write('\n')
f2.close()
'''
#Q9
f=open('D:/abe.txt','w')
f.write('''70
60
55
75
95
90
80
80
85
100''')
f.close()

f1=open('D:/abe.txt','r')
num=f1.readlines()
f1.close()

total=0
for i in num:
    i=i.strip()
    total=total+int(i)
print(total)
average=total/10
print(average)

f2=open('D:/abe.txt','w')
f2.write(str(total))
f2.write('\n')
f2.write(str(average))
f2.close()
