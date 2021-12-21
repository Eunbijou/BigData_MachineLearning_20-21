# 이름, 국어, 영어, 수학을 입력 받아 이름, 국어, 영어, 수학, 합계, 평균, 등급을 출력
# 등급은 A, B, C, D, F로 한다.
name=input("이름 입력 : ")
kor=int(input("국어 점수 입력 : "))
eng=int(input("영어 점수 입력 : "))
math=int(input("수학 점수 입력 : "))

sum=kor+eng+math
avg=sum/3.


if avg>=90:
    grd="A"
elif avg>=80:
    grd="B"
elif avg>=70:
    grd="C"
elif avg>=60:
    grd="D"
else:
    grd="F"

    # print("{:10s}{:4s}{:4s}{:4s}{:4s}{:4s}"
    #       .format("이름","국어","영어","수학","합계","평균","등급"))
    # print("{:10s}{:4d}{:4d}{:4d}{:4.0f}{:4.0f}"
    #       .format(name, kor, eng, math, sum, avg, grd))

print("이름", "국어", "영어", "수학", "합계", "평균", "등급")
print( name, kor, eng, math, sum, avg, grd)