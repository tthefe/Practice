#12201284 김수민
#3
'''
def convert(word):
    total=0
    for i in word:
        if i=='!':break
        elif 'A'<=i<='Z':
            score=ord(i)-ord('A')+1
        elif 'a'<=i<='z':
            score=ord(i)-ord('a')+1
                
        total=total+score
    return total

while True:            
    word=input('문자열을 입력하시오:')
    x=convert(word)
    print(x)

    f=open('result.txt','a')
    f.write(word+':'+str(x)+'\n')
    f.close()
'''
#2
'''
def solution(a,b,c):
        if a==0:
            if b==0:
                print('해가 없음')
            else:
                X=float(-(c/b))
                print('x=%f'%X)
        elif a!=0:
            if (b**2-4*a*c)>0:
                X1=float((-b+(b**2-4*a*c)**0.5)/(2*a))
                X2=float((-b-(b**2-4*a*c)**0.5)/(2*a))
                print('x1=%f\nx2=%f'%(X1,X2))
            elif (b**2-4*a*c)==0:
                X3=float(-(b/(2*a)))
                print('x=%f'%X3)
            else:
                print('실수해가 없음')
while True:        
    a=float(input('a='))
    if a==-9999:
        print('프로그램을 종료합니다')
        break
    b=float(input('b='))
    c=float(input('c='))
    solution(a,b,c)
'''
#1
'''
NDVI=[]
for i in range(1,6):
    Red=float(input('%d번째 Red밴드 반사율:'%i))
    NIR=float(input('%d번째 NIR밴드 반사율:'%i))
    ndvi=(NIR-Red)/(NIR+Red)
    NDVI.append(ndvi)

total=0
for n in NDVI:
    total=total+n
mean=total/5
print('Mean=%f'%mean)

total1=0
for v in NDVI:
    total1=total1+(v-mean)**2
variance=total1/5
print('Variance=%f'%variance)

x=max(NDVI)
y=min(NDVI)
print('Max=%f'%x)
print('Min=%f'%y)
'''


########


#1
'''
#자료입력
NDVI=[]

for i in range(1,6):
    Red=float(input('%d번째 Red밴드 반사율 = '%i))
    NIR=float(input('%d번째 NIR밴드 반사율 = '%i))

    ndvi=(NIR-Red)/(NIR+Red)
    NDVI.append(ndvi)

#평균
total=0
for n in NDVI:      #인덱싱 이용하는 것도 가능
    total=total+n
mean=total/5
print('Mean=%f'%mean)
#분산
total1=0
for v in NDVI:
    total1=total1+(v-mean)**2
variance=total1/5
print('Variance=%f'%variance)

#최대,최소
print('Max=%f'%(max(NDVI)))
print('Min=%f'%(min(NDVI)))
'''

#2
'''
def solution(a,b,c):
    if a==0:
        if b==0:
            print('해가 없음')
        else:
            X=float(-(c/b))
            print('x=%f'%X)
                
    elif a!=0:
        if (b**2-4*a*c)>0:
            X1=float(pow((-b+(b**2-4*a*c)),0.5)/(2*a))    #pow함수 사용!!, d=b*b-4*a*c, (-b+pow(d,0.5))/(2*a)
            X2=float(pow((-b-(b**2-4*a*c)),0.5)/(2*a))
            print('x1=%f\nx2=%f'%(X1,X2))
                
        elif (b**2-4*a*c)==0:
            X3=float(-(b/(2*a)))
            print('x=%f'%X3)
                
        else:
            print('실수해가 없음')
                
while True:        
    a=float(input('a='))
    if a==-9999:
        print('프로그램을 종료합니다')
        break
    b=float(input('b='))  #문자열 포메팅 안 해도 됨
    c=float(input('c='))
    solution(a,b,c)
'''

#3
#전달인자. return 필요
def convert(word):
    total=0
    for i in word:
        if 'A'<=i<='Z':
            score=ord(i)-ord('A')+1
            
        elif 'a'<=i<='z':
            score=ord(i)-ord('a')+1
                
        total=total+score
    return total

f=open('result.txt','a')  #while루프 밖에 작성

while True:            
    word=input('문자열을 입력하시오:')
    if word[0]=='!':break   #첫 문자=word[0]
    x=convert(word)

    f.write(word+':'+str(x)+'\n')

f.close()  #while루프 밖에 작성
