#12201284 김수민
'''
def data(nn):
    a1=[]
    for i in range(1,nn+1):
    j=int(input('%d번째 자료 값을 입력하세요:'%i))
    a1.append(j)
    return a1

def sorting(b):
    b.sort()
    return b

def output(c):
    print(c)
'''
def complex_print(a,b,c,d):
    while True:
        print('*'*50)
        a=int(input('첫번째 복소수의 실수부를 입력하세요:'))
        b=int(input('첫번째 복소수의 허수부를 입력하세요:'))
        if a==0 and b==0:
            break
        if b>0:
            b='+'+b
        c=int(input('두번째 복소수의 실수부를 입력하세요:'))
        d=int(input('두번째 복소수의 허수부를 입력하세요:'))
        if d>0:
            d='+'+d
    
    
a=int(input('첫번째 복소수의 실수부를 입력하세요:'))
b=int(input('첫번째 복소수의 허수부를 입력하세요:'))
c=int(input('두번째 복소수의 실수부를 입력하세요:'))
d=int(input('두번째 복소수의 허수부를 입력하세요:'))
complex_print(a,b,c,d)
