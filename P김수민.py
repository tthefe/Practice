#12201284
#1
'''
n=int(input('연산을 반복할 횟수='))

print('='*50)
for a in range(1,n+1):
    N=[]
    
    for i in range(1,6):
        j=int(input('%d번째 정수='%i))
        N.append(j)

    total=0
    for n1 in N:
        total=total+n1
    mean=total/5
    print('Mean=%f'%mean)

    total1=0
    for n1 in N:
        total1=total1+(n1-mean)**2
    variance=total1/5
    print('Variance=%f'%variance)

    print('Max=%d'%(max(N)))
    print('Min=%d'%(min(N)))
    
    print('='*50)
'''

'''
N=[]을 for루프 밖에 쓰면 새로 실행할때 리셋이 되지 않고 앞에 입력값도 포함
'''

#2
'''
def Add(a,b):
    r=int(a)+int(b)
    print('%s+%s=%d'%(a,b,int(r)))

def Sub(a,b):
    r=int(a)-int(b)
    print('%s-%s=%d'%(a,b,int(r)))
    
def Mul(a,b):
    r=int(a)*int(b)
    print('%s*%s=%d'%(a,b,int(r)))

def Div(a,b):
    r=int(a)/int(b)
    print('%s/%s=%d'%(a,b,int(r)))
    
def Rem(a,b):
    r=int(a)%int(b)
    print('%s%%%s=%d'%(a,b,int(r)))
    
def Quo(a,b):
    r=int(a)//int(b)
    print('%s//%s=%d'%(a,b,int(r)))

def Calculator(num1,num2,operator):
    
    if operator=='+':
        Add(num1,num2)
    elif operator=='-':
        Sub(num1,num2)
    elif operator=='*':
        Mul(num1,num2)
    elif operator=='/':
        Div(num1,num2)
    elif operator=='%':
        Rem(num1,num2)
    elif operator=='//':
        Quo(num1,num2)

        
while True:
    num1=input('첫 번째 정수(종료하려면 !입력):')
    if num1=='!':
        print('종료합니다!')
        break
    operator=input('Enter the operator type(+,-,*,/,%,//):')
    num2=input('Enter the second integer:')
    Calculator(num1,num2,operator)
'''
#함수를 호출할 때 다른 함수를 호출가능

#3

def idcard(a):
    year='20'+a[0:2]
    
    month=a[2:4]
    day=a[4:6]
        
    old=2020-int(year)+1
    
    print('당신은 %s년에 태어났습니다.'%year)
    print('당신의 생일은 %s월 %s일입니다.'%(month,day))
    print('당신은 2020년 현재 %s살입니다.'%old)

    if int(a[7])==3:
        print('당신은 남성입니다.')
    elif int(a[7])==4:
        print('당신은 여성입니다.')
    else:
        print('당신의 성별을 판단할 수 없습니다.')
    print('='*50)

while True:
    number=input('당신의 주민등록번호를 -을 포함해서 입력하세요:')
    if int(number[0])<0:
        print('당신은 2000년 이전에 태어나서 계산할 수 없습니다ㅠ0ㅠ')
        break
    idcard(number)
