'''
import random
for i in range(0,100):
    a=random.randint(1,10)
    print(a)

for j in range(0,100):
    a=random.randrange(10)
    print(a)
'''
'''
import random

a=random.randint(1,6)
print(a)

b=random.randrange(1,7)
print(b)

c=random.choice([1,2,3,4,5,6])
print(c)

d=random.sample([1,2,3,4,5,6],k=1)
print(d)
'''
#pi시뮬레이션
import random
import math

total=1000000
inside=0

for i in range(0,total):
    x=random.random()
    y=random.random()

    if math.sqrt(x**2+y**2)<1.0:
        inside+=1

pi=(inside/total)*4
e=pi-math.pi   #오차=추정값-참값

print('When n is %d, pi~ %f, 오차=%f'%(total,pi,e))
