#p.130
'''
tree=0
while tree<10:
    tree+=1
    print('나무를 %d번 찍었습니다.'%tree)
    if tree==10:
        print('tree is falling down')
    
'''
#p.132
'''
prompt=
'''
'''1.add
   2.del
   3,list
   4,quit
   Enter number: '''
'''
number=0
while number!=4:
    print(prompt)
    number=int(input())
'''
#p.134
'''
coffee=10
while True:
    money=int(input('돈을 넣어주세요: '))
    if money==300:
        print('coffee')
        coffee=coffee-1
    elif money>300:
        print('거스름돈 %d를 받고 커피를 준다.'%(money-300))
        coffee=coffee-1
    else:
        print('돈이 부족')
        
    if coffee==0:
        print('커피가 다 팔렸으므로 판매중단')
        break
'''    
#p.136
'''
a=0
while a<10:
    a=a+1
    if a%2==0:continue
    print(a)
'''
#p.137
'''
while True:
    print('Ctrl+C를 눌러야 while문을 빠져나갈 수 있음')
'''
#p.139
'''
score=[38,29,47,70,72]
student=0
for s in score:
    student=student+1
    if s>=60:
        print('%d번째 학생은 합격'%student)
    else:
        print('%d번째 학생은 불합격'%student)
'''    
#p.140
'''
score=[50,91,6,51,34]
student=0
for s in score:
    student=student+1
    if s>60:
        print('%d번째 학생 합격 축하'%student)
    else:continue
'''
#p.142
'''
s=0
for i in range(1,11):
    s=s+i
print(s)
'''
#p.136
'''
a=0
while a<10:
    a=a+1
    if a%3==0:continue
    print(a)#각각의 결과값을 보고 싶을 때에는 for문에 포함하여 작성
'''
'''
s=0
for a in range(1,101,2):
    s=s+a
print(s)#최종 결과만 보고 싶을 때에는 for문과 별개로 작성
'''
#p.143
'''
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')#end='여기에 쓰여진 것을 사이에 넣고 한 줄로 나옴'
    print('')
'''
#연습문제2
'''s=0
a=0
while a<999:
    a=a+3
    s=s+a
print(s)
'''
'''
s=0
a=0
while a<1000:
    if a%3==0:
        s=s+a
    a=a+1
print(s)
'''
#연습문제3
'''
a=0
while a<5:
    a=a+1
    print("'*'*%d"%int(a))
'''
'''
a=0
while True:
    a=a+1
    if a>5:break
    print('*'*a)
'''
#연습문제4
'''
for i in range(1,101):
    print(i)
'''
#연습문제5
'''
A=[70,60,55,75,95,90,80,80,85,100]
s=0
for score in A:
    s=s+score
print(s)
average=s/10
print(average)
'''
#연습문제6
'''
numbers=[1,2,3,4,5]
result=[n*2 for n in numbers if n%2==1]
print(result)
'''
