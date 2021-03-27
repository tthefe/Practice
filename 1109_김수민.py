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


def Calculator(num1,num2,operator):
    
    if operator=='+':
        Add(num1,num2)
    elif operator=='-':
        Sub(num1,num2)
    elif operator=='*':
        Mul(num1,num2)
    elif operator=='/':
        Div(num1,num2)

try:
    num1=input('첫 번째 정수입력:')
    operator=input('연산자 입력(+,-,*,/):')
    num2=input('두번째 정수 입력:')
    r=Calculator(num1,operator,num2)
    print(r)
except:
    print('0으로 나누기를 시도하여 종료합니다.')
