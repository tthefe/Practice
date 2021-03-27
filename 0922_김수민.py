#12201284 김수민
'''
a=int(input("원하는 단을 입력하세요: "))
for i in range(1,10):
    print("%d*%d=%d"%(a,i,a*i))
'''
#12201284 김수민
'''
for t in range(100,-1,-5):
    f=1.8*t+32
    print("섭씨 %d 도: 화씨 %d 도"%(t,f))
'''

#12201284 김수민
'''
a=input(" ")
n=a.split(",")#나눠준 숫자를 정의, 나눠준 숫자는 리스트에 들어간다
total=0
for b in n:
    total=total+int(b)
print(total)
'''
'''
#12201284 김수민

while True:
    a=int(input("숫자 입력: "))
    if a%2==0 and a%3==0:
        print("yes")
        continue
    else:
        if a%2!=0 or a%3!=0:
            print("no")
        else:
            a==0: #왜 안될까............
                print("0을 입력하여 프로그래밍을 종료합니다.")
                break
'''

#12201284 김수민

total=0
for i in range(91,101,1):
    total=total+i
mean=float(total/10)

var=0
for j in range(91,101,1):
    c=float(j-mean)**2
    var=var+c
var=var/10
print("Mean is %f"%mean)
print("variance is %f"%var)
    
