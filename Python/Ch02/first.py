# a라는 변수, 변수는 기억장소의 이름. 저장되는 값에 따라 자료형 결정.
a=10 # lv = rv, lv는 반드시 변수 또는 저장소 /10=a (X)
b=20
print("a+b=", a+b) # 정수와 실수가 연산 => 실수
print("a-b=", a-b)
print("a*b=", a*b)
print("a/b=", a/b) # 실수 결과
print("a//b=", a//b) # 정수나눗셈 결과

a=10
b=3.0
print("a//b=", a//b) # 나머지 결과
print("a%b=", a%b) # 나머지 정수만 사용

# a를 반지름으로 하는 원둘레
a=5
print("a를 반지름으로 하는 원둘레", a**2*3.14)