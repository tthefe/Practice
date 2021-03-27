#12201284 김수민
'''
a=int(input('시작값 입력: '))
b=int(input('끝값 입력: '))
s=0
for i in range(a,b+1):
   s=s+i
print('합은 %d'%s)
'''

#12201284 김수민
'''
n=int(input('팩토리얼을 계산할 1보다 큰 정수를 입력하시오: '))
s=1
for n in range(1,n):
   s=s*(n+1)
   int(s)
print('%d!=%d'%((n+1),s))
'''

#12201284 김수민
#while루프, break

while True:
    print('*'*30)
    d=int(input('위도의 도 단위값을 정수로 입력하시오.: '))
    m=int(input('위도의 분 단위값을 정수로 입력하시오.: '))
    if m<0:
        break
        print('위도의 분 값에 음수를 입력하여 종료합니다.')
    s=int(input('위도의 초 단위값을 정수로 입력하시오.: '))
    a=d+m/60+s/3600
    print('위도 %d도 %d %d는 위도 %f도입니다.'%(d,m,s,a))
    print('*'*30)
