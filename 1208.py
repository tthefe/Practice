'''
import numpy as np
print(np.random.random())
rn=np.random.rand(5)   #5개의 숫자를 랜덤으로 뽑는다,0과 1사이에서 난수 발생(1은 포함x)
print(rn)
print(type(rn))   #<class 'numpy.ndarray'>:numpy에서 제공해주는 형태

print(np.random.randint(1,6,3))   #1<=x<6사이에서 3개의 정수난수 발생

print(np.random.choice(6,5))   #0<=x<6에서 5개의 정수난수 추출, 복원추출

print(np.random.choice(6,10,replace=False))   #비복원추출
'''
'''
import matplotlib.pyplot as plt
import numpy as np

dice=np.random.randint(1,7,120)   #7포함x
#random 모듈을 사용할 때는 리스트의 요솟값으로 추가해야한다
#numpy모듈에서는 for문 사용안 해도 되고 리스트의 요솟값으로 추가할 필요x
plt.hist(dice, bins=6)
plt.show()
'''
'''
import numpy as np

coord=[[128,129,130],[36.1,36.2,36.3]]
xy=np.array(coord)

print(xy.shape)
print(xy.dtype)

print(xy[0][0])
print(xy[:1,1:])   #첫번째행, 1부터 끝까지
print(xy[:,0])
print(xy+1)

int_xy=xy.astype(np.int32)   #자료형을 float에서 np.int32로 변
print(int_xy)
print(int_xy.dtype)
'''
import numpy as np

fliename='D:/score2.txt'

score=np.loadtxt(fliename, delimiter="\t")
print('Array size: '+ str(score.shape))
print(score)

mean1=np.mean(score[:,0])   #모든 행,첫번째 열
mean2=np.mean(score[:,1])   #모든 행,두번째 열

stdev1=np.std(score[:,0])
stdev2=np.std(score[:,1])

print('For variable 1, mean: %f, stdev %f'%(mean1,stdev1))
print('For variable 2, mean: %f, stdev %f'%(mean2,stdev2))


corr=np.corrcoef(score[:,0],score[:,1])
print(corr)

corr12=np.corrcoef(score[:,0], score[:,1])[0,1]
print('Correlation coefficient: %f'%corr12)
