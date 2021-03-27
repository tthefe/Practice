#12201284 김수민 toktok0320@naver.com
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




#1

#자료입력
NDVI=[] #원소값 미지정하여 리스트 변수 선언

for i in range(1,6):   #반사율 shell창에서 입력
    Red=float(input('%d번째 Red밴드 반사율 = '%i))
    NIR=float(input('%d번째 NIR밴드 반사율 = '%i))

    ndvi=(NIR-Red)/(NIR+Red)  #NDVI계산
    NDVI.append(ndvi)  #리스트 요소로 추가(append함수 이용)

#평균구하기
total=0
for n in NDVI:
    total=total+n
mean=total/5
print('Mean=%f'%mean)  #문자열 포매팅-float

#분산구하기
total1=0
for v in NDVI:
    total1=total1+(v-mean)**2
variance=total1/5
print('Variance=%f'%variance)  #문자열 포매팅 이용-float

#최대,최소구하기
print('Max=%f'%(max(NDVI)))  #max함수 이용
print('Min=%f'%(min(NDVI)))  #min함수 이용

'''
float를 적절히 잘 사용했다.
문제를 잘 이해하고 풀었다.
'''

#2

#함수선언
def solution(a,b,c): #세 개의 파라미터
#이차방정식 해 구하기
    if a==0:
        if b==0:
            print('해가 없음')
        else:
            X=float(-(c/b))
            print('x=%f'%X)
                
    elif a!=0:
        if (b**2-4*a*c)>0:
            X1=float(pow((-b+(b**2-4*a*c)),0.5)/(2*a))  #pow함수 이용
            X2=float(pow((-b-(b**2-4*a*c)),0.5)/(2*a))
            print('x1=%f\nx2=%f'%(X1,X2))
                
        elif (b**2-4*a*c)==0:
            X3=float(-(b/(2*a)))
            print('x=%f'%X3)
                
        else:
            print('실수해가 없음')

#입력                
while True:        
    a=float(input('a='))   #shell 창에서 입력 받을 때 실수도 입력 가능-float
    if a==-9999:   #-9999를 입력 시 프로그램 종료
        print('프로그램을 종료합니다')
        break
    b=float(input('b='))
    c=float(input('c='))
    solution(a,b,c)   #solution함수 호출

'''
pow함수를 사용하는 조건을 지키지 못했다.
함수를 어떻게 선언해야 하는지에 대한 이해를 잘 한 것 같다.
'''

#3
    
#함수선언
def convert(word):   #shell창에 입력된 문자를 인자로 받아 점수 계산->전달인자
    #계산
    total=0
    for i in word:
        if 'A'<=i<='Z':
            score=ord(i)-ord('A')+1   #아스키코드 이용
            
        elif 'a'<=i<='z':
            score=ord(i)-ord('a')+1
                
        total=total+score
    return total   #함수 외부에 전달->return


#파일 입출력
f=open('result.txt','a')  #while루프 밖에 작성

while True:            
    word=input('문자열을 입력하시오:')
    if word[0]=='!':break   #첫 문자=word[0]
    x=convert(word)

    f.write(word+':'+str(x)+'\n')

f.close()
'''
ord함수를 이용하여 단어에 할당된 점수를 계산하는 방법을 잘 이해했다.
파일 입출력시 어느 부분까지 반복문에 포함해야 할지에 대한 이해가 아직 부족한 것 같다.
'''
