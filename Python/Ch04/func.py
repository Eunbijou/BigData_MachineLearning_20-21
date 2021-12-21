# 국어, 영어, 수학 점수를 입력 받아 합계 리턴
def sum(kor, eng, mat):
    total = kor+eng+mat
    return total

k=int(input("korean : "))
e=int(input("english : "))
m=int(input("math : "))

res=sum(k,e,m)
print("total="+res)

# 입력값 없는 함수
# 1. 말 그대로(결과가 필요 없는 경우)
# 2. 함수에서 입력 받아서 사용할 때 결과 값이 없는 함수
# 3. 입력 값이 없는 함수
# 4. 입력 값도 결과 값도 없는 함수
# 5. 함수에서 출력/저장이 끝난 경우
#
# 입력 값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
# 포인터(시작주소) 넘겨주는 의미, 리스트와 같은 것을 넘길 때




