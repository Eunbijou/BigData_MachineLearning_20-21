# i = 1
# result = 0
# while i <= 1000:
#     if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
#         result += i
#     i += 1
#
# print(result)

i=1
x3sum=0
while(i<=1000):
    if i%3==0:
        x3sum+=i
    i+=1
print("1000까지의 3의 배수 합 :%d"%x3sum)