print("hello world")
age = 4
print(str(age))
name = "심유정"
age = 30
is_adult = age >= 20

print(name + "은/는" + str(age)+ "살이고" + "어른이다" + str(is_adult))
print(name,"은/는" , age,"살이고", "어른이다", is_adult)
# ,쓸때는 빈칸이 들어간다

'''
이렇게 하면 여러문장이 주석처리가 됨
'''

station = "신도림"
print("지금" + station + " 행 열차가 들어오고 있습니다.")

print(2**3) #2^3 2의 3승
print(5%2) #나머지 구하기 2
print(10%3) #나머지 1
print(5//3) #몫을 구하기 1
print(10//3) #몫 3
print(10>3) #true
print(10<3) #false
print(4>=7) #false
print(3==3) #true
print(10<3) #false
print(5<=5) #true

print(3==3) #true
print(4==2) #false
print(3+4==7) #true

print(1 != 3) #true 1과 3은 같지않다
print(not(1!=3)) #false
print(3>0) and (3<5) # true
print((3>0) & (3<5)) #true
print((3>0) or (3<5)) #true
print((3>0) | (3<5)) #true

number = 5 + 6 * 3 #23
print(number) #23
number = number + 2
print(number) #25
number += 2
print(number) #27
number *= 2 
print(number) #54
number /= 2 
print(number) #27
number -= 2 
print(number) #25

number %= 5 
print(number) #0
# number %= 2 
# print(number) #1

print(abs(-5)) #절대값 5
print(pow(4,2)) #4^2 = 4*4 = 16
print(max(5,12)) #12
print(min(5,12)) #5
print(round(3.14)) #반올림 3
print(round(4.99)) #5


from math import *
print(floor(4.99)) #내림. 4
print(ceil(3.14)) #올림. 4
print(sqrt(16)) #제곱근 4

from random import *
print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # int 들어가면 정수값 구해짐 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)) #0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)) #0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 임의의 값 생성

#로또값 구하기
#로또는 1이상 45이하니까

print(int(random() * 45) +1) #1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 45)) # 1 ~ 45 이하의 임의 값 생성

print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성

#QUIZ) 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로함
#아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하라.

#조건1. 랜덤으로 날짜를 뽑아야함
#조건2. 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
#조건3. 매월 1~3일은 스터디 준비를 해야 하므로 제외

#(출력문 예제) 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

date=randint(4,28)
print(("오프라인 스터디 모임 날짜는 매월")+str(date)+("일로 선정되었습니다."))
print(int(random() * 28) + 4) # 4일~28일까지 랜덤

bag = '나는 가방입니다'
print(bag)
lol = "파이썬은 쉬워요"
print(lol)
sentence3 = """
나는 가방을 들고있고,
파이썬은 쉬워요
3줄까지 되나??오...
"""
print(sentence3)


jumin = "931015-1234567"
#필요한 정보만큼 잘라서 사용하기
print("성별: " + jumin[7]) # -는 제외하고 인덱스 0부터 시작해서 7번째를 가져옴
print("연: " + jumin[0:2 ]) # 0번째부터 2번째직전까지
print("월: " + jumin[2:4]) # (0부터 시작)2번째부터 4번째 직전까지
print("일: " + jumin[4:6]) # 4번째부터 6번째 직전까지
print("생년월일은 " + jumin[:6] + "이지롱") #처음부터 6직전까지
print("뒤 7자리 " + jumin[7:]) #7번째부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) 
# 맨 뒤에서 7번째부터 끝까지

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())#소문자로 실행
print(python.upper())#대문자로 실행
print(python[0].isupper())#파이썬의 0번째가 대문자인지 알려줌 true
print(len(python))#글자갯수 알려줌

