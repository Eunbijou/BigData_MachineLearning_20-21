# 1부터 100까지의 짝수 합과 홀수 합을 출력
i=1
even=0
odd=0

while i <= 100:
    if i % 2 == 0:
        even += i
    else:
        odd += i
    i += 1

print("짝수 합 : %d"%even)
print("홀수 합 : %d"%odd)

