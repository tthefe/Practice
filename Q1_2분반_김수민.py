#12201284 김수민 toktok0320@naver.com

#2
'''
while True:
    X=input('문자 하나를 입력하시오: ')
    S=X.upper()
    
    if X=='!':
        break
    print(S)   #print함수를 여기에 써야지 !를 변환하지 않는다.
'''

#print함수에서 값이 출력되는 함수라면 출력값을 가지고 있다는 것!!!

#3
'''
def BMI(t, w):
    bmi=w/(t/100)**2
    if bmi>=30.0:
        print('BMI= %f:고도비만입니다.'%bmi)
    elif bmi>=25.0:
        print('BMI= %f:비만입니다.'%bmi)
    elif bmi>=23.0:
        print('BMI= %f:과체중입니다.'%bmi)
    elif bmi>=18.5:
        print('BMI= %f:표준체중입니다.'%bmi)
    else:
        print('BMI= %f:체중미달입니다.'%bmi)

t=int(input('키를 cm단위로 입력하시오. = '))
w=int(input('몸무게를 kg단위로 입력하시오. = '))
BMI(t, w)
'''
#1
'''
for i in range(5,0,-1):
    for j in range(1,i+1):# *을 i번 곱해라
        print('*',end='')
    print('')
'''
