#12201284 김수민
'''
h=int(input("키를 cm단위로 입력하시오."))
w=int(input("몸무게를 kg단위로 입력하시오."))

bmi=w/(h/100)**2
if bmi>=30.0:
    print("BMI = %f:고도비만입니다."%bmi)
elif 25.0<=bmi<30.0:
    print("BMI = %f:비만입니다."%bmi)
elif 23.0<=bmi<25.0:
    print("BMI = %f:과체중입니다."%bmi)
elif 18.5<=bmi<23.0:
    print("BMI = %f:표준체중입니다."%bmi)
else:
    print("BMI = %f:체중미달입니다."%bmi)
'''

#12201284 김수민
'''
i=1
total=0
while i<=10:
    total=total+i #total+=i
    i=i+1 #i+=1
print("The sum is %d"%total)
'''

#12201284 김수민
'''
i=1
total=0
while i<=100:
    total=total+i
    i=i+2
print("The sum is %d"%total)

i=2
total=0
while i<=100:
    total=total+i
    i=i+2
print("The sum is %d"%total)
'''

#12201284 김수민
'''
num=int(input("Enter the number(if zero, stop): "))
count=0
while num!=0:#0아닐 때만 반복
    print("You enter %d"%num)
    count=count+1
    num=int(input("Enter the number(if zero, stop): "))
print("You enter%d.So the loop is terminated"%num)
print("0이 아닌 숫자를 %d번 입력"%count)
'''

#12201284 김수민

test_list=['one','two','three']
for t in test_list:
    print(t)


