#연습용문제
#함수2
'''
n=int(input('원하는 자료 개수를 입력하세요:'))
def data(n):
    a=[]
    for i in range(1,n+1):
        j=int(input('%d번째 자료 값을 입력하세요:'%i))
        a.append(j)
    return a

x=data(n)
print(x)

def sorting(b):
    b.sort()
    return b

y=sorting(x)
print(y)

def output(c):
    print(c)
output(y)
'''
#함수3
while True:
    print('*'*45)
    a=int(input('첫번째 복소수의 실수부를 입력하세요:'))
    b=int(input('첫번째 복소수의 허수부를 입력하세요:'))
    c=int(input('두번째 복소수의 실수부를 입력하세요:'))
    d=int(input('두번째 복소수의 허수부를 입력하세요:'))

    if a==0 and b==0:
        break
    else:
        def complex_print(a,b,c,d):
            if b>0:
                print('첫번째 복소수: %d+%di'%(a,b))
            else:
                print('첫번째 복소수: %d%di'%(a,b))

            if d>0:
                print('두번째 복소수: %d+%di'%(c,d))
            else:
                print('두번째 복소수: %d%di'%(c,d))
        complex_print(a,b,c,d)

        def complex_add(a,b,c,d):
            if b+d>0:
                print('복소수 덧셈: %d+%d'%((a+c),(b+d)))
            else:
                print('복소수 덧셈: %d%di'%((a+c),(b+d)))
        complex_add(a,b,c,d)

        def complex_mul(a,b,c,d):
            if b*c+a*d>0:
                print('복소수 곱셈: %d+%di'%(a*c-(b*d),(b*c+a*d)))
            else:
                print('복소수 곱셈: %d%di'%(a*c-(b*d),(b*c+a*d)))
        complex_mul(a,b,c,d)
