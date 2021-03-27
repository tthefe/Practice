#12201284 김수민
'''
def multiple1():
    a=int(input('숫자 입력:'))
    if a%2==0 and a%3==0:
        print('yes')
    else:
        print('no')
multiple1()
'''
'''
def multiple2(a):
    if a%2==0 and a%3==0:
        print('yes')
    else:
        print('no')
num=int(input('숫자 입력: '))
multiple2(num)
'''
#12201284 김수민
#8 문제는 갤러리에 캡처
'''
def avg_var(a,b):
    total=0
    for i in range(a,b+1):
        total=total+i
    total=total/(b-a+1)
    
    var=0
    for i in range(a,b+1):
        var=var+(i-total)**2
    var=var/(b-a+1)
    return total,var

a=int(input('시작값 입력:'))
b=int(input('끝값 입력:'))

n=avg_var(a,b)
print('평균:%f & 분산:%f'%(n[0],n[1]))#평균과 분산을 실수, 결과값은 튜플이므로 인덱스 이
#m,v=avg_var(a,b)
#print(''%(m,v))   도 가능
'''
