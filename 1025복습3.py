#Q5
'''
f1=open("D:/test.txt", 'w')
f1.write('Life is too short')
f1.close()

f2=open('D:/test.txt','r')
a=f2.read()
print(a)
f2.close()
'''
#Q6
'''
user_input=input('저장할 내용을 입력하세요:')
f=open('D:/test.txt','a')
f.write('\n')
f.write(user_input)
f.write('\n')
f.close()
'''
#Q7
'''
f=open('D:/test.txt','w')
f.write('Life is too short\nyou need java')
f.close()

f2=open('D:/test.txt','r')
a=f2.read()
print(a)
f2.close()

f1=open('D:/test.txt','w')
f1.write(a.replace('java', 'python'))
f1.close()
'''
#종합 문제 Q8---------다시 풀
'''
f=open('D:/test.txt','w')
f.write('AAA\nBBB\nCCC\nDDD\nEEE')
f.close()

f1=open('D:/test.txt','r')
f1.read()
f1.close

f2=open('D:/test.txt','w')
f2.reverse()
f2.close()
'''
#종합 문제 Q9
'''
f=open('D:/test.txt','w')
f.write('70\n60\n55\n75\n95\n90\n80\n80\n85\n100')
f.close()

f1=open('D:/test.txt','r')
num=f1.readlines()
f1.close()

total=0
for i in num:
    j=int(i)
    total=total+j
average=total/10

f2=open('D:/test.txt','a')
f2.write('\n')
f2.write(str(total))         #숫자는 파일에 바로 쓸 수 없으므로 str함수를 사용하여 문자열로 변
f2.write('\n')
f2.write(str(average))
f2.close()
'''
#연습용문제 파일 입출력
#1
'''
f=open('D:/sample.txt','w')
for i in range(1,11):
    a='%d\n'%(i%7)
    print(a)
    f.write(a)
f.close()

f1=open('D:/sample.txt','r')
num=f1.readlines()
print(num)
f1.close()

total=0
for i in num:
    j=int(i)
    total=total+j
print(total)
average=total/len(num)
print(average)

f2=open('D:/sample.txt','w')
f2.write('Mean=%f'%average)
f2.close()
'''
#함수1
'''
def coord(d,m=0,s=0):
    l=d+m/60+s/3600
    print('%d도 %d분 %d초는 %f도입니다.'%(d,m,s,l))
'''
#반복문
'''
while True:
    word=input('영어 단어:')
    
    if word=='!':
        print('프로그램을 종료합니다.')
        break
    else:
        total=0
        for i in word:
            if 'A'<=i<='Z':
                j=ord(i)-ord('A')+1
            elif 'a'<=i<='z':
                j=ord(i)-ord('a')+1
            total=total+j
        print(total)
'''
