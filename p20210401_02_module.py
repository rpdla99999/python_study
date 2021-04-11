#모듈
# import time
# print(time.localtime())
# print(time.localtime().tm_year,'년', end=' ',sep='')
# print(time.localtime().tm_mon,'월', end=' ',sep='')
# print(time.localtime().tm_mday,'일',sep='')

# from datetime import datetime
# now = datetime.now()
# print(now)
# print(now.strftime('%Y-%m-%d %H:%M:%S'))


#sleep함수 : 프로그램 실행 속도를 제어
# import time
# print('시작')
# time.sleep(3)
# print('3초지남')

#timer 만들기
# from time import sleep
# sec = int(input('몇초?'))
# print('타이머시작')
# for x in range(1,sec+1):
#     sleep(1)
#     print(x,'초')
#
# print('종료')

#난수모듈
#주사위 게임
# import random
# awin=0 #a이긴 횟수
# bwin=0 #b이긴 횟수
# while True:
#     a = random.randint(1,6)
#     b = random.randint(1,6)
#     print('A:', a, 'B:', b)
#     if a>b:
#         print('A승')
#
#     elif b>a:
#         print('B승')
#     else:
#         print('무승부')

import random
#sample()
# print(random.sample(range(1,46), 6))

#choice()
#print(random.choice(['가위','바위','보']))

#shuffle() :섞는다
# data=['나비','나비','벌','벌','꽃', '꽃']
# random.shuffle(data)
# print(data)

# import turtle
# turtle.shape('turtle')
# turtle.color('red')
# for x in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#
# turtle.done()


