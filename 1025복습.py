#제어문 문제 퀴즈1)
'''
a=int(input('시작값 입력: '))
b=int(input('끝값 입력: '))

total=0
for i in range(a,b+1):
    total=total+i
print('합은 %d'%total)
'''
#제어문 문제 퀴즈2)
'''
a=int(input('팩토리얼을 계산할 1보다 큰 정수를 입력하시오: '))

total=1
for i in range(a,0,-1):
    total=total*i
print('%d!=%d'%(a,total))
'''
#제어문 문제 퀴즈3)
'''
while True:
    print('*'*50)
    d=int(input('위도의 도 단위값을 정수로 입력하시오: '))
    m=int(input('위도의 분 단위값을 정수로 입력하시오: '))
    s=int(input('위도의 초 단위값을 정수로 입력하시오: '))

    if m<0:
        break
    
    h=d+m/60+s/3600
    
    print('위도 %d도 %d분 %d초는 위도 %f도입니다.'%(d,m,s,h))
    print('*'*50)
'''

#3장 문제풀이1

#1
'''
a=int(input('숫자를 입력하시오: '))
b=int(input('숫자를 입력하시오: '))
if a>b:
    print(a)
else:
    print(b)
'''
#2
'''
total=1
a=1
while a<99:
    a=a+2
    total=total+a
print(total)
'''
#3
'''
total=2
a=2
while a<100:
    a=a+2
    total=total+a
print(total)
'''
#4
'''
total=0
for a in range(1,100):
    if a%2==1:
        total=total+a
    else:continue
print(total)
'''
#5
'''
total=0
for a in range(2,101):
    if a%2==0:
        total=total+a
    else:continue
print(total)
'''
#6
'''
n=int(input('원하는 단을 입력하세요: '))
for i in range(1,10):
    r=n*i
    print('%d*%d=%d'%(n,i,r))
'''
#7
'''
for c in range(100,-1,-5):
    f=int(c*1.8+32)
    print('섭씨 %d도: 화씨 %f도'%(c,f))
'''
#주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라.
'''
pocket=input('주머니에 무엇이 있나?: ')
print(pocket)
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')
'''
#if문을 이용하여 절대값 구하기
'''
num=int(input('enter the number:'))
if num < 0:
    num=-num
print(num)
'''
#if~else문을 이용하여 짝홀수 판별하기
'''
num=int(input('enter the number:'))
if num%2==0:
    print('%d is an even number'%num)
else:
    print('%d is an odd number'%num)
'''
#1부터 10까지의 합을 구해서 출력
'''
i=1
total=1
while i<10:
    i=i+1
    total=total+i
print('%d'%total)
'''
#0을 입력할 때까지 값 입력을 반복하는 프로그램 작성
'''
while True:
    num=int(input('enter the number:'))
    print('%d'%num)
    if num==0:
        print('you enter %d.so the loop is terminated'%num)
        break
'''
#1부터 10까지의 합을 구해서 출력
'''
total=0
for i in range(1,11):
    total=total+i
print(total)
'''
#for문을 이용하여 5개 숫자를 입력한 후 평균을 계산하고 출력하시오.
'''
total=0
for i in range(1,6):
    a=int(input('enter the %d number:'%i))
    total=total+a
    average=int(total)/5
print('평균은 %f입니다.'%average)
'''
#2단부터 9단까지 출력
'''
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ???? ')
    print('??')
'''
#1부터 10까지의 숫자 중에서 3의 배수를 뺀 나머지 값을 출력하시오.
#for루프 이용
'''
for i in range(1,11):
    if i%3==0:
        continue
    else:
        print(i)
'''
#while루프 이용
'''
i=0
while i<10:
    i=i+1
    if i%3==0:
        continue
    else:
        print(i)
'''
