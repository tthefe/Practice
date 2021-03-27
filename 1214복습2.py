#반복문
'''
while True:
    word=input('영어 단어: ')
    if word=="!":
        print('프로그램을 종료합니다.')
        break

    total=0
    for i in word:
        if ord('A')<=ord(i)<=ord('Z'):
            score=ord(i)-ord('A')+1
            total+=score
        elif ord('a')<=ord(i)<=ord('z'):
            score=ord(i)-ord('a')+1
            total+=score

    print('점수: %d'%total)
'''
#함수(1)
'''
def coord(d,m=0,s=0):
    D=d+m/60+s/3600
    print('%d도 %d분 %d초는 %f도입니다.'%(d,m,s,D))
'''
#함수(2)
'''
def data(n):
    N=[]
    for i in range(1,n+1):
        num=int(input('%d번째 자료 값을 입력하세요: '%i))
        N.append(num)
    return N
def sorting(a):
    a.sort()
    return a
def output(b):
    print(b)

n=int(input('원하는 자료 개수를 입력하세요: '))
a=data(n)
b=sorting(a)
output(b)
'''
#함수(3)
'''
def complex_print(a,b,c,d):
    if b>0:
        if d>0:
            print('첫번째 복소수:%d+%di'%(a,b))
            print('두번째 복소수:%d+%di'%(c,d))
        else:
            print('첫번째 복소수:%d+%di'%(a,b))
            print('두번째 복소수:%d%di'%(c,d))

    else:
        if d>0:
            print('첫번째 복소수:%d%di'%(a,b))
            print('두번째 복소수:%d+%di'%(c,d))
        else:
            print('첫번째 복소수:%d%di'%(a,b))
            print('두번째 복소수:%d%di'%(c,d))

def complex_add(a,b,c,d):
    if b+d<0:
        print('복소수 덧셈: %d%di'%(a+c,b+d))
    else:
        print('복소수 덧셈: %d+%di'%(a+c,b+d))

def complex_mul(a,b,c,d):
    if a*d+b*c>0:
        print('복소수 곱셈: %d+%di'%(a*c-b*d,a*d+b*c))
    else:
        print('복소수 곱셈: %d+%di'%(a*c-b*d,a*d+b*c))
        
while True:
    print('***************************************')
    a=int(input('첫번째 복소수의 실수부를 입력하세요: '))
    b=int(input('첫번째 복소수의 허수부를 입력하세요: '))
    if a==0 and b==0:
        break
    c=int(input('두번째 복소수의 실수부를 입력하세요: '))
    d=int(input('두번째 복소수의 허수부를 입력하세요: '))

    complex_print(a,b,c,d)
    complex_add(a,b,c,d)
    complex_mul(a,b,c,d)

    print('***************************************')
'''
#파일 입출력
'''
f=open('D:/sample.txt','w')
for i in range(1,11):
    f.write('%s\n'%str(i%7))
f.close()

f=open('D:/sample.txt','r')
n=f.readlines()

total=0
for num in n:
    N=int(num)
    total+=N
mean=total/len(n)
f.close()

f=open('D:/result.txt','w')
f.write('Mean=%s'%str(mean))
f.close()
'''
#QUIZ1
#2
'''
while True:
    w=input('문자 하나를 입력하시요: ')
    if w=="!":
        break
    print(w.upper())
'''
#3
'''
h=int(input('키를 cm단위로 입력하시오.= '))
w=int(input('몸무게를 kg단위로 입력하시오.= '))
H=h/100

def BMI(H,w):
    bmi=w/H**2
    if bmi>=30.0:
        print('BMI=%f:고도비만입니다.'%bmi)
    elif bmi>25.0:
        print('BMI=%f:비만입니다.'%bmi)
    elif bmi>23.0:
        print('BMI=%f:과체중입니다.'%bmi)
    elif bmi>18.5:
        print('BMI=%f:표준체중입니다.'%bmi)
    else:
        print('BMI=%f:체중미달입니다.'%bmi)
BMI(H,w)
'''

#2019Quiz5
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

    result='Mean:%f\nVariance:%f'%(mean,var)
    return result

start=int(input('시작값 입력: '))
stop=int(input('끝값 입력: '))

x=any_start(start,stop)
print(x)

f=open('D:/start.txt','w')
f.write(x)
f.close()
'''
