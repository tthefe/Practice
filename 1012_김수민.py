#1
'''
f=open('D:/새파일.txt','w')
for i in range(1,11):
    data='%d번째 줄입니다.\n'%i
    print(data)
    f.write(data)
f.close()
'''
#2

f1=open('D:/test.txt','w')
f1.write("Life is too short")
f1.close()

f2=open('D:/test.txt','r')
print(f2.read())
f2.close()

f3=open('D:/test.txt','a')
f3.write('\nI am still young')#자동 줄바꿈이 안되서 \n을 써서 줄바꿈을 해야한다
f3.close()
