coffee=10
while True:
    money=int(input('돈을 넣어주세요: '))
    if money==300:
        print('coffee')
        coffee-=coffee
    elif money>300:
        print('거스름돈 %d를 받고 커피를 준다.'%(money-300))
        coffee-=1
    else:
        print('돈이 부족')
        
    if coffee==0:
        print('커피가 다 팔렸으므로 판매중단')
        break
