#연습문제
# 1)별찍기1
# print('♥국제별찍기♥')
# print('★' * 1)
# print('★' * 2)
# print('★' * 3)
# print('★' * 4)
# print('★' * 5)
# print('★' * 6)
#
# for x in range(1,12,2):
#     print('★' * x)

# 1)별찍기1
# print('★' * 6)
# print('★' * 5)
# print('★' * 4)
# print('★' * 3)
# print('★' * 2)
# print('★' * 1)
# for x in range(6,0,-1):
#     print('◆' * x)


# 1)별찍기3
# print(' ' * 5, end=''); print('★' * 1)
# print(' ' * 4, end=''); print('★' * 2)
# print(' ' * 3, end=''); print('★' * 3)
# print(' ' * 2, end=''); print('★' * 4)
# print(' ' * 1, end=''); print('★' * 5)
# print(' ' * 0, end=''); print('★' * 6)

#실습2)구구단 출력
# dan = int(input('단수는?'))
# for x in range(1,10):
#     print('%d * %d = %d'%(dan,x,dan*x))

#2~9단까지 출력
# for x in range(1,10):
#     for y in range(1,10):
#         print(x,y)

#실습3)
# last = int(input('마지막수는?'))
# for x in range(0, last+1, 6):
#     print(x, end='\t')
#
# print()
# for x in range(0,last+1):
#     if x%3==0:
#         print(x,end='\t')

#실습4)
# 반복
# 1)두수와 기호를 입력받는다
# 2)기호에 따라 계산
# 3)계속진행여부 입력
#1)
# while True:
#     a=int(input('first:'))
#     b=int(input('second:'))
#     sign = input('기호:')
#     if sign=='+':
#         print(a+b)
#     elif sign =='-':
#         print(a-b)
#     elif sign == '*':
#         print(a*b)
#     elif sign =='/':
#         print(a/b)
#     else:
#         print('잘못된 기호')
#
#     if input('종료(y)?')=='y': break

#2)
# while True:
#     a=input('first:')
#     if a=='q': break
#     a=int(a)
#     b=int(input('second:'))
#     # 원하는 기호가 입력될때까지 계속입력
#     while True:
#         sign = input('기호:')
#         if sign in ['+','-','*','/']:
#             break
#
#     if sign=='+':
#         print(a+b)
#     elif sign =='-':
#         print(a-b)
#     elif sign == '*':
#         print(a*b)
#     elif sign =='/':
#         print(a/b)
#     else:
#         print('잘못된 기호')
#실습5)
# dicA = {1:94, 2:87, 3:91, 4:75, 5:92}
# print(dicA.keys())
# print(dicA.values())
# print(dicA.items())
#
# for no,score in dicA.items():
#     if score>=90:
#         print(no,'번')

#실습6)
# 1)사원의 판매수량 입력
#2)히스토그램 그리기
#데이터구조: {'홍길동':10, '이순신':15, '김순희':5, '이철수':7}
data = ['홍길동','이순신','김순희','이철수']
qty={} #판매수량을 저장할 딕셔너리
for name in data:
    qty[name] = int(input(name + '?'))

print(qty)

for name, saleqty in qty.items():
    print(name, '*' * saleqty)











