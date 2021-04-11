#조건문
# a=-10
# if a>0:
#     print('양수')
#     print(a)
# else:
#     print('음수')
#     print(a)
#
# print('프로그램 종료')

#실습)회원등급 출력
#a가 90보다 크면 good 아니면 try 출력
# a=int(input('점수는?'))
# if a>90:
#     print('good')
# else:
#     print('try')

#실습)비밀번호 체크
#비밀번호가 일치하면 '문이열립니다.'
#일치하지 않으면 '다시확인하세요'

# pw='1234' #기존 등록된 비밀번호
# inpw = input('비밀번호?')
# if pw==inpw:
#     print('문이열립니다.')
# else:
#     print('다시확인하세요.')

#어떤수가 짝수이면 '짝수' 홀수이면 '홀수' 출력
# a=int(input('숫자는?'))
# if a==0:
#     print('짝수도 홀수도 아닙니다.')
# elif a%2==0:
#     print('짝수')
# else:
#     print('홀수')

#실습)~90 A , 89~80 B, 79~70 C, 69~60 D, 59~ F
# a=int(input('점수는?'))
# if a>=90:
#     print('A')
# elif a>=80:
#     print('B')
# elif a>=70:
#     print('C')
# elif a>=60:
#     print('D')
# else:
#     print('F')

#실습)몸무게와 키를 입력받아서 비만여부출력
# weight=60.1
# height=165.5
# normal=(height-100)*0.9
# print('정상체중:', normal)
# if weight < normal*0.95:
#     print('미달')
# elif weight <= normal * 1.05:
#     print('정상')
# else:
#     print('비만')

#실습)계산기
#두수와 기호를 입력받아 사칙연산(+,-,*,/)를 출력
#1)
# 30 + 20 = 50
# a=30
# b=20
# sign='/'
# if sign=='+':
#     print(a+b)
# elif sign =='-':
#     print(a - b)
# elif sign =='*':
#     print(a * b)
# elif sign =='/':
#     print(a / b)
# else:
#     print('잘못된 기호')

#2)
# data=input('계산식은?').split()
# a=int(data[0])
# b=int(data[2])
# sign=data[1]
# if sign=='+':
#     print('%d + %d = %d'%(a,b,a+b))
# elif sign == '-':
#     print('%d - %d = %d'%(a,b,a-b))
# elif sign == '*':
#     print('%d * %d = %d'%(a,b,a*b))
# elif sign == '/':
#     print('%d / %d = %d'%(a,b,a/b))
# else:
#     print('잘못된 기호')

# 3)eval은 강력하지만 보안에 취약, 주의
import os
# print(os.listdir())
# data = input('계산식은?')
# print(eval(data))

#실습)두수를 입력을 받아서 큰수를 화면에 출력
# a=int(input('first?'))
# b=int(input('second?'))
# if a>b:
#     print(a)
# elif b>a:
#     print(b)
# else:
#     print('두수는 같다')

#실습)거스름돈계산
# amount = int(input('물품금액:'))
# pay = int(input('낸금액:'))
# if pay>amount:
#     print('거스름돈:', pay-amount)
# elif pay<amount:
#     print('부족금액:', amount-pay)
# else:
#     print('계산완료')

#논리연산자
# a=10;b=20
# print(a>0 and b>0)
# print(a>0 and b<0)
# print(a>0 or b<0)
# print(not (a>0))
# a=-10; b=10
# if a==0 or b==0:
#     print('0이 아닌수를 입력하세요')
# elif a>0 and b>0:
#     print('둘다 양수')
# elif a>0 or b>0:
#     print('둘중에 하나가 음수')
# else:
#     print('둘다 음수')

#1)
# price =({'1':['자장면', 5000],'2':['짬뽕',6000],'3':['설렁탕',8000],
#          '4':['비빔밥',10000],'5':['피자',12000],'6':['스파게티',9000]})
# print('-' * 22)
# print('[국제식당]오늘의 메뉴')
# print('-' * 22)
# print('1.자장면\n2.짬뽕\n3.설렁탕\n4.비빔밥\n5.피자\n6.스파게티')
# print('-' * 15)
# no = input('메뉴는?')
# print(price[no][0] ,'선택')
# print(price[no][1] ,'원')
# if no in ['1','2']: #in : 포함 여부
#     print('중식코너')
# elif no in ['3','4']:
#     print('한식코너')
# elif no in ['5', '6']:
#     print('양식코너')
# else:
#     print('다시 입력')
# 2)
price =({'1':['자장면', 5000,'중식'],'2':['짬뽕',6000,'중식'],'3':['설렁탕',8000,'한식'],
         '4':['비빔밥',10000,'한식'],'5':['피자',12000,'양식'],'6':['스파게티',9000,'양식']})
print('-' * 22)
print('[국제식당]오늘의 메뉴')
print('-' * 22)
print('1.자장면\n2.짬뽕\n3.설렁탕\n4.비빔밥\n5.피자\n6.스파게티')
print('-' * 15)
no = input('메뉴는?')
menukey = price.keys()
if no in menukey:
    print(price[no][0] ,'선택')
    print(price[no][1] ,'원')
    print(price[no][2] ,'코너')
else:
    print('다시입력해 주세요')















