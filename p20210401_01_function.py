#내장함수
# data=[5,8,4,6]
# print(sum(data))

#사용자함수 sum정의:
# 매개변수:리스트, 반환값:합계
# def mysum(data):
#     s=0
#     for x in data:
#         s += x
#     #print(s)
#     return s
#
# data=[5,18,4,6]
# r = mysum(data)
#
# print('리턴값:', r)

#max, min함수
# data=[5,18,4,6]
# mx=max(data)
# print('가장큰값:', mx)
# mi = min(data)
# print('가장작은값:', mi)

#max값 사용자 함수
# def mymax(data):
#     mx = data[0]
#     for x in data:
#         if x > mx:
#             mx = x
#     return mx
# #전역변수
# data2 = [5, 18, 4, 6]
# print('가장큰값:',mymax(data2))
# data = [78, 8, 5, 16]
# print('큰값:',mymax())

#min값을 구하는 함수
# def mymin(mindata):
#     mi = mindata[0]
#     for x in mindata:
#         if x < mi:
#             mi = x
#     return mi
#
# data = [78, 8, 5, 16]
# result =mymin(data)
# print('가장작은값:', result)

#ord() 함수
#한글은 유니코드체계
# print(ord('A'), len('A'),'A'.encode(), len('A'.encode()))
# print(ord('김') , len('김'), '김'.encode(), len('김'.encode()))
# print(chr(44032))

#실습)사칙연산 함수
#매개변수 : 두수 ,반환값 : 결과
# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#리턴값은 한개만 가능
# def cal(a,b):
#     return a+b,a-b #튜플로 반환

# print('더하기:', add(10,20))
# print('빼기:', sub(10,20))
# print("계산:", cal(10,20)[0], cal(10,20)[1])

#실습)월급구하기
def salary(yearS,timeS,overtime):
    return yearS / 12 + timeS * overtime

yearS = int(input('월급:'))
timeS = int(input('시급은?'))
overtime = int(input('초과근무시간은?'))
print('월급:', salary(yearS,timeS,overtime))









