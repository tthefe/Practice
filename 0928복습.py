#4
'''
A=[20,55,67,82,45,33,90,87,100,25]
student=0
total=0
for score in A:
    student=student+1
    if score>=50:
        total=total+score
    else:
        continue
print(total)
'''
#6
'''
a=input('숫자 다섯개를 입력하시오:')
b=a.split(',')
total=0
for i in b:
    total=total+int(i)
print(total)
'''
#7
'''
x=int(input('구구단을 출력할 숫자를 입력하세요(2-9):'))
for j in range(0,10):
    j=j+1
    g=x*j
    print('%d'%g, end=' ')
'''
#8
X=[AAA
BBB
CCC
DDD]
X.reverse()
print(X)

