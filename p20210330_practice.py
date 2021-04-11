# a=input('이름은?')
# print(a)
# age=input('나이?')
# print('당신의 나이는 ' + age + ' 입니다')
# txt="오늘의 날씨는"
# w='맑음'
# z='입니다'
# print(txt,'*',w,z)
# a=int(input('숫자는?'))
# # a=int(a)
# # print(a+100)
# a=int(input('첫번째 수')); b=int(input('두번째 수'))
# print('%d + %d = %d'%(a,b,a+b))
# print('%d - %d = %d'%(a,b,a-b))
# print('%d * %d = %d'%(a,b,a*b))
# print('%d / %d = %.1f'%(a,b,a/b))

#적정체중구하기
# 적정 체중 구하기
# ➢ 이름/신장/몸무게를 입력 받고 적정체중여부를
# 출력해보자
# 평균체중 =(키-100) * 0.9
# 오차범위 : +- 5 %
# ➢ 출력 예) 당신은 적정 체중입니다
# 당신은 너무 말랐네요.
# 당신은 비만입니다.
# name=input('이름을 입력하세요')
# he=int(input('키를 입력하세요'))
# we=int(input('몸무게를 입력하세요'))
# aver=((he-100)*0.9)
# if we>aver*1.05:
#     print(name,'당신은 비만입니다')
# elif we<aver*0.95:
#     print(name,'당신은 기아입니다')
# else:
#     print(name, '당신은 정상입니다')

# import random
# print(random.randint(4,28))

k= '960715-1070612'
# print('성별:',k[7])
k[7]='남자'
print(k[7])
