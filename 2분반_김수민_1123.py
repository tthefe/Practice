#math 모듈 pi
'''
r=float(input('원의 반지름:'))

import math

l=2*r*math.pi
m=math.pi*r**2

print('반지름 %f인 원의 둘레는 %f'%(r,l))
print('반지름 %f인 원의 넓이는 %f'%(r,m))
'''
#math 모듈 삼각함수
'''from math import raidans, tan'''   #radians, tan를 바로 사용가능

'''
d=int(input('거리:'))
g=float(input('각도:'))

import math   #import하는 모듈은 보통 맨 처음에 넣기

G=math.radians(g)
h=d*math.tan(G)

print('건물의 높이는 %fm 입니다.'%h)   #소수점 3자리까지 나타내기 %.3f
'''
