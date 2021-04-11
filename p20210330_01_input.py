#사용자에게 입력받기
# a=input('이름은?')
# print('입력한 값은',a)

#실습)나이를 입력받아 화면에 출력
#입력한 값은 문자취급
# age=input('나이는?')
# print('당신의 나이는 ' + age + '입니다')

#실습)날씨를 입력받아 오늘의 날씨 출력
#예) 오늘의 날씨는 맑음
# txt='오늘의 날씨는'
# w=input('날씨:')
# print(txt,w,sep='*')

#도움말 출력
#help(print)

#사용자가 입력한값에 100을 더해서 출력
#a=input('숫자는?')
#a=int(a)#정수로 변환해서 반환해주는 함수
#a=float(a) #실수로 변환해서 반환해주는 함수
#print(a+100)


#실습)두수를 입력받아 사칙연산 프로그램
# 30 + 20 = 50
# 30 - 20 = 10
#1)
# a = int(input('첫번째수?'))
# b = int(input('두번째수?'))
# print('%d + %d = %d'%(a,b,a+b))
# print('%d - %d = %d'%(a,b,a-b))
# print('%d * %d = %d'%(a,b,a*b))
# print('%d / %d = %.2f'%(a,b,a/b))
#
# print('두수를 더한값은' , a+b , '입니다')

#2)
# data = input('두수는?').split() #두수를 분리
# a,b = map(int ,data) #data의 각값을 int함수를 적용한후 a,b에 대입
# print(a,'+', b, '=' , a+b)

#실습)원의넓이를 구하기
# r=float(input('반지름:'))
# print('원의넓이는', r**2 * 3.14)




























