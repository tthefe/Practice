#p.117
'''
money=True   #True에서 T는 대문자로 적어야 한다.
if money:
    print("택시")
else:
    print("걸어감")
'''
#p.122
'''
money=int(input("돈이 얼마 있습니까?: "))
if money>=3000:
    print("택시")
else:
    print("걸어가라")
'''
#p.123
'''
money=int(input("돈이 얼마 있습니까?: "))
card=int(input("카드를 몇 개 가지고 있습니까?: "))
if money>=3000 or card>=1:
    print("택시")
else:
    print("걸어가")
'''
#p.124
'''
pocket=['money','cellphone','watch']
if 'money' in pocket:
    print("Taxi")
else:
    print("Walk")
'''
'''
pocket=str(input("주머니에 무엇이 들어있는가?: "))
if 'money' in pocket:
    print('taxi')
else:
    print('walk')
'''
#p.125 나혼자코딩
'''
pocket=str(input('주머니에 무엇이 들어있나요?:'))
if 'card' in pocket:
    print('bus')
else:
    print('walk')


pocket={'cellphone','money'}
if 'card' not in pocket:
    print('walk')
else:
    print('bus')
'''
#p.125-1
'''
pocket=str(input("What's in your pocket?: "))
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
'''
'''
pocket=['card','money','candy']
message='bus' if 'card' in pocket else '카드를 꺼내라'#질문
'''
#p.125-2
'''
pocket=str(input("What's in your pocket?:"))
if 'money' in pocket:
    print('taxi')
elif 'card' in pocket:
    print('texi')
else:
    print('walk')
'''
