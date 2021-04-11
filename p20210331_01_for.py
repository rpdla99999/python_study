#반복문:for
# for x in [1,20,30,7,9]:
#     print('python', x)

# data=['이선희','최불암','BTS']
# for x in data:
#     print(x)

# for x in [0,1,2]:
#     print(data[x])

#실습)0~9출력
# for x in [0,1,2,3,4,5,6,7,8,9]:
#     print(x)

#정수를 생성
#range(start,stop,step)
# print(list(range(10,101,3)))
# print(list(range(101)))#stop
# print(list(range(10,20))) #start,stop

# for x in range(0,10,2):
#     print(x)

#합계를 구하기
# s=0 #합계를 저장할 변수
# for x in range(1,10001):
#     s += x #s = s+x
# print(s)

#실습)사용자에게 숫자를 입력받아 1부터 그수까지 더하기
# s=0
# lastsu = int(input('마지막숫자는?'))
# for x in range(1,lastsu+1):
#     s += x
# print(s)

#break
#실습) 1부터 100까지 합이  2000이 넘을때의 그 수를 출력
# s=0
# for x in range(1,101):
#     s+=x
#     if s>2000:
#         break #반복문을 종료할때
#
# print('x=', x, 's=', s)

#실습)바보라는 글자가 발견되면 강퇴
# data = ['안녕', '반가워', '방가', '바', '오늘만나']
# bad = ['바보', '멍청이']
# for x in data:
#     print(x)
#     if x in bad:
#         print('강퇴')
#         flag=1
#         break
# else: #for문이정상수행했다면(break문을 실행하지 않았을때)
#     print('바른말 사용')


#continue:계속진행
# data=[3,4,6,8,7,10]
# for x in data:
#     if x%2==1: continue
#     print(x)

#실습)모든 점수 60이상 합격
#data = [65,88,45,90,70]
# data=input('점수는?').split()
#print(data)
# data = map(int , data)
# for x in data:
#     print(x)
#     if x<60:
#         print('불합격')
#         break
# else:
#     print('합격')

#실습)합계가 300점 이상이면 합격
s=0
data=[10,10,10,55,70]
for x in data:
    s +=x
    if s>=300:
        print('합격')
        break
else:
    print('불합격')






