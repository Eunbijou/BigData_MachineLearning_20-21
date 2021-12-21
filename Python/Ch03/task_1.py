# 가위바위보 게임
import random

user=int(input("가위[0] 바위[1] 보[2] 선택 :")) #사용자입력
com=random.randint(0,2) #컴퓨터 난수

res=user-com #비교

# 사용자 출력
if(user==0):
    print("사용자 : 가위")
elif(user==1):
    print("사용자 : 바위")
else:
    print("사용자 : 보")

# 컴퓨터 출력
if(com==0):
    print("컴퓨터 : 가위")
elif(com==1):
    print("컴퓨터 : 바위")
else:
    print("컴퓨터 : 보")

# 결과
if(res==-2 or res==1):
    print("이김")
elif(res==0):
    print("비김")
else:
    print("짐")