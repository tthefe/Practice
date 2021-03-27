#12201284 김수민
'''
def add(a,b):   #함수원형, a와 b는 형식매개변수
    return a+b   #함수정의


add(3,4)   #함수호출, 3과 4는 실 매개변수
#a=3,b=4
'''
'''
함수를 출력하는 방법
1. 변수에 assign
2, print()함수 안에 인자로 넣는다.
   ex)d=add(3,4)
      print(d)는

      print(add(3,4))와 동일
'''
#12201284 김수민
'''
def even_odd(x):
    if x%2==1:
        print('%d is an odd number'%x)
    else:
        print('%d is an even number'%x)
num=int(input('Enter the number:'))#함수호출을 하지 않아도 된다면 def안에 집어넣어도 된다.
even_odd(num)
'''
#12201284 김수민
#함수 안에서 출력
'''
def cal_max(a,b):
    if a>b:
        max=a
    else:
        max=b
    print('The maximum value is %d'%max)
a=int(input('Enter the a:'))
b=int(input('Enter the b:'))
cal_max(a,b)
'''
#함수 밖에서 출력
def cal_max(a,b):
    if a>b:
        max=a
    else:
        max=b
    return max
a=int(input('Enter the a:'))
b=int(input('Enter the b:'))
x=cal_max(a,b)
print('The maximun value is %d'%x)#%cal_max(a,b)도 가능

#12201284 김수민
'''
def one_to_ten_sum():
    total=0
    for  i in range(1,11):
        total=total+i
    print('The sum is %d'%total)
one_to_ten_sum()
'''
#12201284 김수민
'''
def gugudan(a):
    for i in range(1,10):
        print('%d*%d=%d'%(a,i,a*i))
a=int(input('원하는 단을 입력하세요:'))
gugudan(a)
'''
#12201284 김수민
'''
def any_sum(a,b):
    total=0
    for i in range(start,end+1):
        total=total+i
    return total
start=int(input('시작값 입력:'))
end=int(input('끝값 입력:'))
a=any_sum(start,end)
print('합은 %d'%a)    
'''





























