#Q4
'''
A=[20,55,67,82,45,33,90,87,100,25]

total=0
for n in A:
    if n>=50:
        total+=n
    else:
        continue
print(total)
'''
#Q5
'''
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

a=int(input('정수 값을 입력하세요:'))
for i in range(a):
    print(fib(i),end=' ')
'''
#Q6
'''
a=input('총합을 구할 숫자를 입력하세요: ')
A=a.split(',')
total=0
for i in A:
    total+=int(i)
print(total)    
'''
#Q7
'''
n=int(input('구구단을 출력할 숫자를 입력하세요(2~9): '))

for i in range(1,10):
    print(n*i, end=' ')
'''
#Q9
'''
f=open('D:/sample.txt','w')
f.write('70\n60\n55\n75\n95\n90\n80\n80\n85\n100\n')
f.close()

f=open('D:/sample.txt','r')
line=f.readlines()
score=[]
for s in line:
    score.append(int(s))

total=0
for i in score:
    total+=i
mean=total/len(score)
print(total)
print(mean)
f.close()

f=open('D:/sample.txt','a')
f.write(str(mean))
f.close()
'''
#Q10
'''
class Calculator:

    def __init__(self,List):
        self.List=List

    def sum(self):
        total=0
        for num in self.List:
            total+=num
        return total
            
    def avg(self):
        total=0
        for num in self.List:
            total+=num
        average=total/len(self.List)
        return average
'''    
#중간고사 문제
#1
'''
N=[]
for i in range(5):
    red=float(input('%d번째 Red밴드 반사율= '%(i+1)))
    nir=float(input('%d번째 NIR밴드 반사율= '%(i+1)))

    NDVI=(nir-red)/(nir+red)

    N.append(NDVI)

total=0
for n in N:
    total+=n
mean=total/len(N)
print('Mean=%f'%mean)

v=0
for j in N:
    v+=(j-mean)**2
print('Variance=%f'%(v/len(N)))

print('Max=%f'%max(N))
print('Min=%f'%min(N))
'''
#2
'''
def solution(a,b,c):
    if a==0 and b==0:
        print('해가 없음')
    elif a==0:
        print('x=%f'%(-c/b))
    elif a!=0:
        if b**2-4*a*c>0:
            print((float(-b+pow((b*b-4*a*c),0.5)))/float(2*a))
            print((float(-b-pow((b*b-4*a*c),0.5)))/float(2*a))
        elif b**2-4*a*c==0:
            print('x=%f'%(-b/(2*a)))
        elif b**2-4*a*c<0:
            print('실수해가 없음')

while True:
    a=float(input('a= '))
    if a==-9999:
        print('프로그램을 종료합니다')
        break
    
    b=float(input('b= '))
    c=float(input('c= '))

    solution(a,b,c)
'''
#3
'''
def convert(word):
    total=0
    for l in word:
        if ord('A')<=ord(l)<=ord('Z'):
            score=ord(l)-ord('A')+1
            total+=score
        elif ord('a')<=ord(l)<=ord('z'):
            score=ord(l)-ord('a')+1
            total+=score
    return total

while True:
    word=input('문자열을 입력하시오: ')
    if word=='!':
        break
    print(convert(word))

    f=open('D:/result.txt','a')
    f.write('%s : %d\n'%(word,convert(word)))
    f.close()
'''
#제어문 문제
#1
'''
start=int(input('시작값 입력: '))
stop=int(input('끝값 입력: '))

total=0
for i in range(start,stop+1):
    total+=i
print('합은 %d'%total)
'''
#2
'''
n=int(input('팩토리얼을 계산할 1보다 큰 정수를 입력하시오: '))

total=1
for i in range(1,n+1):
    total=total*i

print('%d!=%d'%(n,total))
'''
#3
'''
while True:
    print('**********************************')
    d=int(input('위도의 도 단위값을 정수로 입력하시오: '))
    m=int(input('위도의 분 단위값을 정수로 입력하시오: '))
    if m<0:
        print('위도의 분 값에 음수를 입력하여 종료합니다')
        break
    s=int(input('위도의 초 단위값을 정수로 입력하시오: '))

    D=d+m/60+s/3600
    print('위도 %d도 %d분 %d초는 위도 %f입니다.'%(d,m,s,D))
    print('**********************************')
'''
#연습용문제
#파일 입출력
f=open('D:/sample.txt','w')
for i in range(1,11):
    f.write('%d\n'%(i//7))
