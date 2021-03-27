#Q9
'''
import turtle
import random

t=[]

for i in range(5):
    i=turtle.Turtle()
    i.shape('turtle')
    t.append(i)
    

colors=['red','green','yellow','blue','black']
j=0
for x in t:
    t.color(colors[j])
    j=j+1
    for j in range(10):
        x.forward((random.randint(1,100)))
        x.left((random.randint(0,360)))
'''
#히스토그램
'''
import matplotlib.pyplot as plt   #plt.함수
plt.hist([1,1,2,3,4,5,6,6,7,8,10], bins=5)   #리스트형태, bins->전체 구간을 몇 개로 나눌 것인지
plt.show()
'''

'''
import matplotlib.pyplot as plt
import math

f=open('D:/score.txt', 'r')

lines=f.readlines()
score=[]

total=0
for n in lines:
    score.append(int(n))
    total=total+int(n)
m=total/len(lines)
print(m)

v=0
for n in lines:
    v=v+(int(n)-m)**2
M=math.sqrt(v/len(lines))
print(M)

f.close()

plt.hist(score, bins=5)
plt.show()
'''
#주사위 던지기 시뮬레이션
'''
import matplotlib.pyplot as plt
import random

n=60000
dice=[]
for i in range(n):
    dice.append(random.randint(1,6))

plt.hist(dice, bins=6)
plt.show()
'''
